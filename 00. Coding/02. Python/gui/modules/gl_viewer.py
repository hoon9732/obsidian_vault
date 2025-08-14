# modules/gl_viewer.py
from __future__ import annotations

import math, json, ctypes, collections
from typing import Tuple

from OpenGL.GL import *
from PySide6.QtCore import Qt, QTimer, QPoint, Signal
from PySide6.QtGui import QMatrix4x4, QVector3D
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtOpenGLWidgets import QOpenGLWidget

from .scene_loader import load_scene, load_config, GLScene

# ------------------------------------------------------------------ shaders
VERT_MAIN = """
#version 330 core
layout(location = 0) in vec3 inPos;
layout(location = 1) in vec3 inNor;

uniform mat4 u_mvp;
uniform mat4 u_model;

out vec3 v_nor;

void main()
{
    gl_Position = u_mvp * vec4(inPos,1.0);
    v_nor = mat3(transpose(inverse(u_model))) * inNor;
}
"""

FRAG_MAIN = """
#version 330 core
in  vec3 v_nor;
out vec4 frag;

uniform vec3 u_lightDir;   // normalised world-space
uniform vec3 u_color;      // base colour (terrain, rocket, ocean, path)

void main()
{
    float diff = max(dot(normalize(v_nor), u_lightDir), 0.1);
    frag = vec4(u_color * diff, 1.0);
}
"""

VERT_SKY = """
#version 330 core
layout(location = 0) in vec3 inPos;
out vec3 v_dir;
uniform mat4 u_mvp;
void main()
{
    v_dir = inPos;               // direction = vertex position
    gl_Position = u_mvp * vec4(inPos,1.0);
}
"""

FRAG_SKY = """
#version 330 core
in vec3 v_dir;
out vec4 frag;
void main()
{
    float t = clamp(normalize(v_dir).y * 0.5 + 0.5, 0.0, 1.0);
    vec3 sky  = mix(vec3(0.05,0.07,0.2), vec3(0.35,0.55,0.9), pow(t,1.5));
    frag = vec4(sky, 1.0);
}
"""


# ------------------------------------------------------------------ helpers
def _compile(src: str, stype) -> int:
    sid = glCreateShader(stype)
    glShaderSource(sid, src)
    glCompileShader(sid)
    if glGetShaderiv(sid, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(sid).decode())
    return sid

def _build_program(vsrc: str, fsrc: str) -> int:
    pid = glCreateProgram()
    glAttachShader(pid, _compile(vsrc, GL_VERTEX_SHADER))
    glAttachShader(pid, _compile(fsrc, GL_FRAGMENT_SHADER))
    glLinkProgram(pid)
    if glGetProgramiv(pid, GL_LINK_STATUS) != GL_TRUE:
        raise RuntimeError(glGetProgramInfoLog(pid).decode())
    return pid


def _unit_cube_vao() -> int:
    """Return VAO for a cube centred at origin, size 2."""
    verts = [
        -1,-1,-1,   -1, 1,-1,    1, 1,-1,    1,-1,-1,   # back
        -1,-1, 1,   -1, 1, 1,    1, 1, 1,    1,-1, 1    # front
    ]
    idx  = [
        0,1,2, 0,2,3,  4,5,6, 4,6,7,  # Z
        0,4,7, 0,7,3,  1,5,6, 1,6,2,  # X
        0,1,5, 0,5,4,  3,2,6, 3,6,7   # Y
    ]
    verts = (ctypes.c_float * len(verts))(*verts)
    idx   = (ctypes.c_uint  * len(idx))(*idx)
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, ctypes.sizeof(verts), verts, GL_STATIC_DRAW)
    ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, ctypes.sizeof(idx), idx, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
    glBindVertexArray(0)
    return vao, len(idx)


# ------------------------------------------------------------------ widget
class GLWidget(QOpenGLWidget):
    telemetry = Signal(dict)

    HISTORY = 512                    # points kept for green trajectory

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.ClickFocus)

        self.cfg = load_config()
        cam = self.cfg.get("camera", {})
        self.theta = cam.get("theta", 45.0)
        self.phi   = cam.get("phi", 45.0)
        self.dist  = cam.get("dist",  10000.0)
        self.last_pos = QPoint()

        roc_cfg = self.cfg["rocket"]
        self.rocket_pos = QVector3D(*roc_cfg["start"])
        self.rocket_vel = QVector3D(0, 0, 0)
        self.time_since_launch = 0.0
        self.launched = False

        self.path = collections.deque(maxlen=self.HISTORY)  # stores QVector3D

        QTimer.singleShot(0, self._start_timer)

    # ---------------- OpenGL --------------------------------------------
    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)             # remove hidden back-faces
        glPolygonOffset(GL_FRONT_AND_BACK, GL_FILL)          # push filled polys forward
        # glEnable(GL_PROGRAM_POINT_SIZE)
        self.p_main = _build_program(VERT_MAIN, FRAG_MAIN)
        self.p_sky  = _build_program(VERT_SKY,  FRAG_SKY)

        self.scene, _ = load_scene()
        self.sky_vao, self.sky_count = _unit_cube_vao()

        self.proj = QMatrix4x4(); self.proj.perspective(60.0, 1.0, 1.0, 500000.0)

        # uniform handles
        glUseProgram(self.p_main)
        self.u_mvp   = glGetUniformLocation(self.p_main, "u_mvp")
        self.u_model = glGetUniformLocation(self.p_main, "u_model")
        self.u_light = glGetUniformLocation(self.p_main, "u_lightDir")
        self.u_color = glGetUniformLocation(self.p_main, "u_color")

        light_dir = self.cfg.get("sun_light", [0.7,0.8,0.4])
        glUniform3f(self.u_light, *light_dir)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        self.proj = QMatrix4x4()
        self.proj.perspective(60.0, w / h if h else 1.0, 1.0, 500000.0)

    def paintGL(self):
        glClearColor(0.05,0.05,0.1,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # ---- camera matrices -------------------------------------------
        view = QMatrix4x4()
        view.translate(-self.rocket_pos)
        view.translate(0,0,-self.dist)
        view.rotate(self.phi,1,0,0)
        view.rotate(self.theta,0,1,0)
        vp = self.proj * view

        # ---------------------------------------------------------------- SKYBOX
        glDepthMask(GL_FALSE)
        glUseProgram(self.p_sky)
        sky_mvp = self.proj * QMatrix4x4()  # identity view keeps cube centred
        glUniformMatrix4fv(glGetUniformLocation(self.p_sky,"u_mvp"),1,GL_FALSE,sky_mvp.data())
        # glBindVertexArray(self.sky_vao)
        glDrawElements(GL_TRIANGLES, self.sky_count, GL_UNSIGNED_INT, None)
        glDepthMask(GL_TRUE)

        # ---------------------------------------------------------------- OCEAN
        glUseProgram(self.p_main)
        glUniform3f(self.u_color, 0.0,0.25,0.45)
        glUniformMatrix4fv(self.u_mvp,1,GL_FALSE,vp.data())
        glUniformMatrix4fv(self.u_model,1,GL_FALSE,QMatrix4x4().data())
        glBindVertexArray(self.scene.ocean_vao)
        glDrawElements(GL_TRIANGLES, self.scene.ocean_count, GL_UNSIGNED_INT, None)

        # ---------------------------------------------------------------- TERRAIN
        glEnable(GL_POLYGON_OFFSET_FILL)
        glUniform3f(self.u_color, 0.05, 0.3, 0.05)          # dark green
        glBindVertexArray(self.scene.terr_vao)
        glDrawElements(GL_TRIANGLES, self.scene.terr_count, GL_UNSIGNED_INT, None)
        glDisable(GL_POLYGON_OFFSET_FILL)

        # ---------------------------------------------------------------- ROCKET (red)
        model = QMatrix4x4()
        model.translate(self.rocket_pos)
        model.rotate(-90,1,0,0)
        glUniform3f(self.u_color, 0.8,0.0,0.0)
        glUniformMatrix4fv(self.u_mvp,1,GL_FALSE,(vp*model).data())
        glUniformMatrix4fv(self.u_model,1,GL_FALSE,model.data())
        glBindVertexArray(self.scene.rocket_vao)
        glDrawElements(GL_TRIANGLES, self.scene.rocket_count, GL_UNSIGNED_INT, None)

        # ---------------------------------------------------------------- PATH (green line strip)
        if len(self.path) >= 2:
            pts = [coord for p in self.path for coord in (p.x(), p.y(), p.z())]
            pts_arr = (ctypes.c_float * len(pts))(*pts)
            glBindVertexArray(0)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glVertexPointer = glVertexAttribPointer  # alias for fixed pipeline style
            glEnableClientState(GL_VERTEX_ARRAY)
            glVertexPointer(3, GL_FLOAT, 0, pts_arr)
            glUseProgram(self.p_main)
            glUniform3f(self.u_color, 0.0,1.0,0.0)
            glUniformMatrix4fv(self.u_mvp,1,GL_FALSE,vp.data())
            glDrawArrays(GL_LINE_STRIP, 0, len(self.path))
            glDisableClientState(GL_VERTEX_ARRAY)

        glBindVertexArray(0)
        glUseProgram(0)

    # ---------------- interaction --------------------------------------
    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.last_pos = ev.pos()

    def mouseMoveEvent(self, ev):
        if ev.buttons() & Qt.LeftButton:
            dx, dy = ev.x()-self.last_pos.x(), ev.y()-self.last_pos.y()
            self.theta += dx * 0.3
            self.phi   = max(5, min(85, self.phi + dy * 0.3))
            self.last_pos = ev.pos()
            self.update()

    def wheelEvent(self, ev):
        self.dist *= 0.9 if ev.angleDelta().y() > 0 else 1.1
        self.dist = max(50.0, min(300000.0, self.dist))  # <— can zoom to 50 m
        self.update()

    # ---------------- animation ----------------------------------------
    def _start_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(16)

    def tick(self):
        if self.launched:
            roc = self.cfg["rocket"]
            up_a  = roc["launch_acc"]
            up_t  = roc["ascent_time"]
            dt = 0.016
            self.time_since_launch += dt

            if self.time_since_launch < up_t:               # powered
                self.rocket_vel.setY(self.rocket_vel.y() + up_a*dt)
            else:                                           # ballistic
                self.rocket_vel.setY(self.rocket_vel.y() - 9.81*dt)

            self.rocket_pos += self.rocket_vel * dt
            if self.rocket_pos.y() < 0:
                self.rocket_pos.setY(0)
                self.launched = False
                self.rocket_vel = QVector3D(0,0,0)

            # store history
            self.path.append(QVector3D(self.rocket_pos.x(), self.rocket_pos.y(), self.rocket_pos.z()))

            self.telemetry.emit({
                "altitude": self.rocket_pos.y(),
                "speed":    self.rocket_vel.length(),
                "accel":    up_a if self.time_since_launch < up_t else -9.81,
            })

        self.update()


# ------------------------------------------------------------------ window
class GLViewerWindow(QMainWindow):
    telemetry = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("3-D Viewer")
        self.resize(1280,720)

        self.gl = GLWidget(self)
        self.gl.telemetry.connect(self.telemetry)

        btn = QPushButton("Launch")
        btn.clicked.connect(self._toggle_launch)

        lay = QVBoxLayout()
        lay.addWidget(self.gl,1)
        lay.addWidget(btn)

        w = QWidget()
        w.setLayout(lay)
        self.setCentralWidget(w)

    def _toggle_launch(self):
        if not self.gl.launched:
            roc_cfg = self.gl.cfg["rocket"]
            self.gl.rocket_pos = QVector3D(*roc_cfg["start"])
            self.gl.rocket_vel = QVector3D(0,0,0)
            self.gl.path.clear()
            self.gl.time_since_launch = 0.0
        self.gl.launched = not self.gl.launched

    def closeEvent(self, ev):
        cam = {"theta": self.gl.theta, "phi": self.gl.phi, "dist": self.gl.dist}
        self.gl.cfg["camera"] = cam
        with open("assets/scene_config.json","w",encoding="utf-8") as f:
            json.dump(self.gl.cfg,f,indent=2)
        super().closeEvent(ev)
