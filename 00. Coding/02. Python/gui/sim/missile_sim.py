import os, sys, json, math
from dataclasses import dataclass
from typing import List, Tuple, Optional
import numpy as np
import logging
logging.getLogger("trimesh").setLevel(logging.CRITICAL)  # quiet trimesh

# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# ---- third-party (optional) ----
_LOADED_TRIMESH = True
try:
    import trimesh
except Exception:
    _LOADED_TRIMESH = False

'''
# pyassimp stays optional & disabled unless you pass --use-assimp / env
_USE_ASSIMP = ("--use-assimp" in sys.argv) or (os.environ.get("PYMISSILE_USE_ASSIMP") == "1")
_LOADED_ASSIMP = False
if _USE_ASSIMP:
    if sys.platform == "win32":
        for dll in [
            os.path.abspath(r"./third_party/assimp/assimp-vc143-mt.dll"),
            os.path.abspath(r"./third_party/assimp/assimp-vc142-mt.dll"),
            os.path.abspath(r"./third_party/assimp/assimp-5.dll"),
            os.path.abspath(r"./third_party/assimp/assimp.dll"),
        ]:
            if os.path.exists(dll):
                try:
                    os.add_dll_directory(os.path.dirname(dll))
                    import ctypes; ctypes.CDLL(dll)
                    break
                except Exception:
                    pass
    try:
        import pyassimp
        _LOADED_ASSIMP = True
    except Exception as e:
        print("[pyassimp] disabled:", e)
        _LOADED_ASSIMP = False
'''


# heightmap reader
_LOADED_MPL = True
try:
    from matplotlib import image as mpl_image
except Exception:
    _LOADED_MPL = False

# ---------------------------
# Config & Sim Data Classes
# ---------------------------

@dataclass
class SunConfig:
    azimuth_deg: float = 45.0
    elevation_deg: float = 25.0
    intensity: float = 1.0

@dataclass
class RocketConfig:
    dry_mass: float = 50.0
    propellant_mass: float = 50.0
    Cd: float = 0.5
    A_ref: float = 0.05
    rho_air: float = 1.225
    g: float = 9.81
    thrust_curve: List[Tuple[float, float]] = None
    launch_azimuth_deg: float = 10.0
    launch_elevation_deg: float = 90.0
    initial_pos: Tuple[float, float, float] = (0.0, 0.1, 0.0)
    thrust_aligns_with_velocity: bool = False  # use body axis (manual steer)

    # RCS controls
    rcs_force_N: float = 1200.0
    yaw_inertia: float = 300.0
    pitch_inertia: float = 400.0
    rcs_damping: float = 0.6   # 0..1 per second

@dataclass
class CameraConfig:
    distance: float = 12.0
    min_distance: float = 4.0
    max_distance: float = 200.0
    fov_deg: float = 60.0

@dataclass
class GroundConfig:
    tile_size: float = 50.0
    color_ocean: Tuple[float, float, float] = (0.1, 0.3, 0.7)
    color_land: Tuple[float, float, float] = (0.0, 0.65, 0.0)
    heightmap_path: str = ""
    heightmap_vertical_scale: float = 0.02
    heightmap_downsample_to: int = 256

@dataclass
class ModelConfig:
    path: str = ""
    scale: float = 1.0
    forward_axis: str = "Y"
    pre_rotate_deg: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    length_estimate_m: float = 10.0
    engine_drop_m: float = 0.15   # NEW: lower the plume below the tail (meters)

@dataclass
class GraphicsConfig:
    msaa: bool = True

@dataclass
class AppConfig:
    sun: SunConfig
    rocket: RocketConfig
    camera: CameraConfig
    ground: GroundConfig
    model: ModelConfig
    graphics: GraphicsConfig

# ---------------------------
# Globals
# ---------------------------

g_cfg: AppConfig = None
g_base_dir = os.path.dirname(os.path.abspath(__file__))

# Simulation state
g_time = 0.0
g_paused = False
g_has_launched = False
g_aborted = False

g_pos = np.array([0.0, 0.0, 0.0], dtype=np.float32)
g_vel = np.array([0.0, 0.0, 0.0], dtype=np.float32)
g_acc = np.zeros(3, dtype=np.float32)

g_yaw, g_pitch, g_roll = 0.0, 0.0, 0.0
g_yaw_rate, g_pitch_rate = 0.0, 0.0

g_mass0 = 0.0
g_burn_time = 0.0

# Camera orbit
g_cam_yaw = 0.0
g_cam_pitch = math.radians(20.0)
g_cam_dist = 12.0
g_mouse_down = False
g_last_mouse = (0, 0)

# Controls
g_ctrl_left = False
g_ctrl_right = False
g_ctrl_up = False
g_ctrl_down = False

# GL
g_win_w, g_win_h = 1280, 720
g_missile_dl = None
g_heightmap_dl = None

# Heightmap
g_hm_present = False
g_hm_size = (0, 0)
g_hm_scale = 1.0
g_hm_z_scale = 0.02

# Sun
g_sun_az = 45.0
g_sun_el = 25.0
g_sun_int = 1.0

# View Mode
g_view_mode_rcs = False  # False=world, True=align-to-missile

# ---------------------------
# Utility
# ---------------------------

def clamp(v, vmin, vmax): return max(vmin, min(vmax, v))
def deg2rad(d): return d * math.pi / 180.0
def rad2deg(r): return r * 180.0 / math.pi

def piecewise_linear(curve: List[Tuple[float, float]], t: float) -> float:
    if not curve:
        return 0.0
    if t <= curve[0][0]:
        return curve[0][1]
    if t >= curve[-1][0]:
        return curve[-1][1]
    for i in range(len(curve)-1):
        t0, v0 = curve[i]; t1, v1 = curve[i+1]
        if t0 <= t <= t1:
            a = (t - t0) / (t1 - t0 + 1e-9)
            return v0*(1.0 - a) + v1*a
    return curve[-1][1]

def yaw_pitch_from_vec(v: np.ndarray) -> Tuple[float, float]:
    vx, vy, vz = v
    hlen = math.sqrt(vx*vx + vz*vz)
    yaw = math.atan2(vx, vz)
    pitch = math.atan2(vy, hlen)
    return yaw, pitch

def axis_angle_from_to(src: np.ndarray, dst: np.ndarray) -> Tuple[float, np.ndarray]:
    s = src / (np.linalg.norm(src) + 1e-9)
    d = dst / (np.linalg.norm(dst) + 1e-9)
    dot = float(np.clip(np.dot(s, d), -1.0, 1.0))
    angle = math.acos(dot)
    axis = np.cross(s, d)
    n = np.linalg.norm(axis)
    if n < 1e-8:
        axis = np.array([0.0, 1.0, 0.0]) if abs(s[1]) < 0.9 else np.array([1.0, 0.0, 0.0])
    else:
        axis = axis / n
    return angle, axis

def sun_dir_from_az_el(az_deg: float, el_deg: float) -> np.ndarray:
    az = deg2rad(az_deg); el = deg2rad(el_deg)
    x = math.cos(el) * math.sin(az)
    y = math.sin(el)
    z = math.cos(el) * math.cos(az)
    return np.array([x, y, z], dtype=np.float32)

def resolve_path(p: str) -> str:
    if not p: return ""
    if os.path.isabs(p) and os.path.isfile(p): return p
    for base in (g_base_dir, os.path.dirname(os.path.abspath(__file__)), os.getcwd()):
        cand = os.path.abspath(os.path.join(base, p))
        if os.path.isfile(cand):
            return cand
    return p

# ---------------------------
# Model Loading
# ---------------------------

def _compute_vertex_normals_simple(verts: np.ndarray, faces: np.ndarray) -> np.ndarray:
    norms = np.zeros_like(verts, dtype=np.float32)
    for f in faces:
        i0,i1,i2 = int(f[0]), int(f[1]), int(f[2])
        v0,v1,v2 = verts[i0], verts[i1], verts[i2]
        n = np.cross(v1 - v0, v2 - v0)
        norms[i0] += n; norms[i1] += n; norms[i2] += n
    lens = np.linalg.norm(norms, axis=1) + 1e-9
    norms /= lens[:,None]
    return norms

g_model_len_m = 10.0
g_tail_offset_local = 0.0  # distance from model origin to tail along forward axis

def build_missile_display_list(model_cfg: ModelConfig) -> int:
    global g_model_len_m, g_tail_offset_local
    dl = glGenLists(1)
    glNewList(dl, GL_COMPILE)

    loaded = False
    path = resolve_path(model_cfg.path)
    if path and os.path.isfile(path) and _LOADED_TRIMESH:
        try:
            obj = trimesh.load(path, skip_materials=True)
            mesh = obj.to_mesh() if isinstance(obj, trimesh.Scene) else obj
            try: mesh.remove_unreferenced_vertices()
            except Exception: pass
            try: mesh = mesh.triangulate()
            except Exception: pass
            try: mesh.apply_scale(model_cfg.scale)
            except Exception: pass

            verts = np.asarray(mesh.vertices, dtype=np.float32)
            faces = np.asarray(mesh.faces, dtype=np.int32)
            norms = _compute_vertex_normals_simple(verts, faces)

            bbox_min = verts.min(axis=0); bbox_max = verts.max(axis=0)
            if model_cfg.forward_axis.upper() == "Z":
                g_model_len_m = float(bbox_max[2] - bbox_min[2])
                g_tail_offset_local = float(bbox_min[2])   # tail = min Z
            else:
                g_model_len_m = float(bbox_max[1] - bbox_min[1])
                g_tail_offset_local = float(bbox_min[1])   # tail = min Y

            print(f"[model] loaded '{path}' verts={len(verts)} faces={len(faces)} len~{g_model_len_m:.2f}m tail_off={g_tail_offset_local:.2f}")
            glEnable(GL_NORMALIZE)
            glBegin(GL_TRIANGLES)
            for f in faces:
                for idx in (int(f[0]), int(f[1]), int(f[2])):
                    n = norms[idx]; v = verts[idx]
                    glNormal3f(float(n[0]), float(n[1]), float(n[2]))
                    glVertex3f(float(v[0]), float(v[1]), float(v[2]))
            glEnd()
            loaded = True
        except Exception as e:
            print("[model] trimesh load failed:", e)

    if not loaded and _LOADED_ASSIMP and path and os.path.isfile(path):
        try:
            scene = pyassimp.load(path)
            for m in scene.meshes:
                verts = np.asarray(m.vertices, dtype=np.float32) * model_cfg.scale
                faces = np.asarray(m.faces, dtype=np.int32)
                norms = _compute_vertex_normals_simple(verts, faces)
                glEnable(GL_NORMALIZE)
                glBegin(GL_TRIANGLES)
                for f in faces:
                    for idx in (int(f[0]), int(f[1]), int(f[2])):
                        n = norms[idx]; v = verts[idx]
                        glNormal3f(float(n[0]), float(n[1]), float(n[2]))
                        glVertex3f(float(v[0]), float(v[1]), float(v[2]))
                glEnd()
            pyassimp.release(scene)
            loaded = True
        except Exception as e:
            print("[model] pyassimp load failed:", e)

    if not loaded:
        print("[model] using fallback primitive (check path/installation)")
        quad = gluNewQuadric()
        glPushMatrix()
        glScalef(model_cfg.scale, model_cfg.scale, model_cfg.scale)
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [0.85,0.85,0.9,1.0])
        glPushMatrix(); glRotatef(90, -1, 0, 0); gluCylinder(quad, 0.2, 0.2, 2.0, 24, 1); glPopMatrix()
        glPushMatrix(); glTranslatef(0, 0, 2.0); glRotatef(-90, 1, 0, 0); glutSolidCone(0.25, 0.6, 24, 1); glPopMatrix()
        gluDeleteQuadric(quad)
        glPopMatrix()
        g_model_len_m = 2.6
        g_tail_offset_local = 0.0

    glEndList()
    if g_cfg.model.length_estimate_m <= 0.0:
        g_cfg.model.length_estimate_m = max(0.5, g_model_len_m)
    return dl

# ---------------------------
# Heightmap
# ---------------------------

def try_build_heightmap_display_list(ground_cfg: GroundConfig) -> Optional[int]:
    global g_hm_present, g_hm_size, g_hm_scale, g_hm_z_scale
    path = resolve_path(ground_cfg.heightmap_path)
    if not path or not os.path.isfile(path) or not _LOADED_MPL:
        g_hm_present = False
        return None
    try:
        img = mpl_image.imread(path)
    except Exception as e:
        print("[heightmap] failed to read:", e)
        g_hm_present = False
        return None

    try:
        if img.ndim == 3: img = img[..., 0]
        H, W = img.shape
        target = max(16, int(ground_cfg.heightmap_downsample_to))
        step_h = max(1, H // target); step_w = max(1, W // target)
        raw = img[::step_h, ::step_w].astype(np.float32); H, W = raw.shape

        land = (raw > 0.0)
        mn, mx = float(np.nanmin(raw)), float(np.nanmax(raw))
        img01 = np.zeros_like(raw, dtype=np.float32) if mx - mn < 1e-9 else (raw - mn) / (mx - mn)

        g_hm_size = (H, W)
        g_hm_scale = 1.0
        g_hm_z_scale = max(1e-5, ground_cfg.heightmap_vertical_scale)

        dl = glGenLists(1)
        glNewList(dl, GL_COMPILE)
        glDisable(GL_LIGHTING)
        glBegin(GL_TRIANGLES)
        for y in range(H - 1):
            for x in range(W - 1):
                wx  = (x   - W/2) * g_hm_scale
                wz  = (y   - H/2) * g_hm_scale
                wx1 = (x+1 - W/2) * g_hm_scale
                wz1 = (y+1 - H/2) * g_hm_scale

                h00 = img01[y, x]   * g_hm_z_scale + 0.005
                h10 = img01[y, x+1] * g_hm_z_scale + 0.005
                h01 = img01[y+1, x] * g_hm_z_scale + 0.005
                h11 = img01[y+1, x+1]*g_hm_z_scale + 0.005

                c00 = (0.0, 0.65, 0.0) if land[y, x]     else (0.02, 0.06, 0.20)
                c10 = (0.0, 0.65, 0.0) if land[y, x+1]   else (0.02, 0.06, 0.20)
                c01 = (0.0, 0.65, 0.0) if land[y+1, x]   else (0.02, 0.06, 0.20)
                c11 = (0.0, 0.65, 0.0) if land[y+1, x+1] else (0.02, 0.06, 0.20)

                glColor3f(*c00); glVertex3f(wx,  h00, wz)
                glColor3f(*c10); glVertex3f(wx1, h10, wz)
                glColor3f(*c01); glVertex3f(wx,  h01, wz1)
                glColor3f(*c10); glVertex3f(wx1, h10, wz)
                glColor3f(*c11); glVertex3f(wx1, h11, wz1)
                glColor3f(*c01); glVertex3f(wx,  h01, wz1)
        glEnd()
        glEnable(GL_LIGHTING)
        glEndList()

        g_hm_present = True
        print(f"[heightmap] loaded '{path}' -> {H}x{W}, land_pixels={int(land.sum())}")
        return dl
    except Exception as e:
        print("[heightmap] failed:", e)
        g_hm_present = False
        return None

# ---------------------------
# Physics / Simulation
# ---------------------------

def reset_sim():
    global g_time, g_paused, g_pos, g_vel, g_yaw, g_pitch, g_roll, g_yaw_rate, g_pitch_rate
    global g_cam_dist, g_cam_yaw, g_cam_pitch, g_has_launched, g_aborted
    g_time = 0.0
    g_paused = False
    g_has_launched = False
    g_aborted = False

    rc = g_cfg.rocket
    g_pos = np.array(rc.initial_pos, dtype=np.float32)
    g_pos[1] = max(g_pos[1], 0.20)  # lift off the pad a bit

    fwd = sun_dir_from_az_el(rc.launch_azimuth_deg, rc.launch_elevation_deg)
    g_yaw, g_pitch = yaw_pitch_from_vec(fwd)
    g_roll = 0.0
    g_yaw_rate = 0.0
    g_pitch_rate = 0.0
    g_vel[:] = 0.0

    g_cam_dist = g_cfg.camera.distance
    g_cam_yaw = 0.0
    g_cam_pitch = deg2rad(20.0)

def current_mass(t: float) -> float:
    rc = g_cfg.rocket
    prop_mass = rc.propellant_mass
    if g_burn_time > 1e-6:
        burned = clamp(t / g_burn_time, 0.0, 1.0) * prop_mass
    else:
        burned = 0.0
    return rc.dry_mass + (prop_mass - burned)

def current_thrust(t: float) -> float:
    if not g_has_launched or g_aborted:
        return 0.0
    return piecewise_linear(g_cfg.rocket.thrust_curve, t)

def body_forward_from_angles(yaw: float, pitch: float) -> np.ndarray:
    return np.array([
        math.sin(yaw) * math.cos(pitch),
        math.sin(pitch),
        math.cos(yaw) * math.cos(pitch)
    ], dtype=np.float32)

def step_sim(dt: float):
    global g_time, g_pos, g_vel, g_acc, g_yaw, g_pitch, g_yaw_rate, g_pitch_rate

    if g_paused:
        return
    if g_has_launched and not g_aborted:
        g_time += dt

    rc = g_cfg.rocket

    # --- RCS control torques -> angular rates ---
    lever = max(0.2, g_cfg.model.length_estimate_m * 0.5)
    torque_yaw = 0.0
    torque_pitch = 0.0

    # Left key should yaw nose LEFT (negative yaw here). Flames appear on LEFT at tail.
    if g_ctrl_left:  torque_yaw   -= rc.rcs_force_N * lever
    if g_ctrl_right: torque_yaw   += rc.rcs_force_N * lever
    # Up key pitch UP, Down pitch DOWN
    if g_ctrl_up:    torque_pitch += rc.rcs_force_N * lever
    if g_ctrl_down:  torque_pitch -= rc.rcs_force_N * lever

    yaw_acc   = torque_yaw   / max(1e-3, rc.yaw_inertia)
    pitch_acc = torque_pitch / max(1e-3, rc.pitch_inertia)

    # integrate angular rates + damping
    g_yaw_rate   += yaw_acc * dt
    g_pitch_rate += pitch_acc * dt
    damp = max(0.0, min(1.0, rc.rcs_damping))
    g_yaw_rate   *= (1.0 - damp * dt)
    g_pitch_rate *= (1.0 - damp * dt)

    g_yaw   += g_yaw_rate * dt
    g_pitch += g_pitch_rate * dt
    g_pitch = clamp(g_pitch, deg2rad(-89.0), deg2rad(89.0))

    # --- Forces and motion ---
    thrustN = current_thrust(g_time)
    m = current_mass(g_time)
    v = g_vel
    speed = float(np.linalg.norm(v))

    body_fwd = body_forward_from_angles(g_yaw, g_pitch)
    thrust_dir = body_fwd
    vel_dir = (v / (speed + 1e-9)) if speed > 1e-6 else body_fwd

    F_thrust = thrust_dir * thrustN
    F_drag   = -0.5 * rc.rho_air * rc.Cd * rc.A_ref * (speed**2) * vel_dir if speed > 1e-5 else np.zeros(3, np.float32)
    F_grav   = np.array([0.0, -rc.g * m, 0.0], dtype=np.float32)

    a = (F_thrust + F_drag + F_grav) / (m + 1e-9)
    g_acc = a.copy()
    g_vel = g_vel + a * dt
    g_pos = g_pos + g_vel * dt

    # Ocean collision / ground friction
    if g_pos[1] < 0.0:
        g_pos[1] = 0.0
    if g_pos[1] == 0.0:
        if g_vel[1] < 0.0: g_vel[1] = 0.0
        ground_mu = 12.0
        damp = max(0.0, min(1.0, ground_mu * dt))
        g_vel[0] *= (1.0 - damp)
        g_vel[2] *= (1.0 - damp)

# ---------------------------
# Commands
# ---------------------------

def cmd_launch():
    global g_has_launched, g_aborted, g_time, g_vel, g_yaw, g_pitch
    g_has_launched = True
    g_aborted = False
    g_time = 0.0
    # seed initial motion along configured launch direction
    fwd = sun_dir_from_az_el(g_cfg.rocket.launch_azimuth_deg, g_cfg.rocket.launch_elevation_deg)
    g_yaw, g_pitch = yaw_pitch_from_vec(fwd)
    g_vel[:] = fwd * 0.2

def cmd_center():
    global g_cam_yaw, g_cam_pitch, g_cam_dist, g_view_mode_rcs
    g_view_mode_rcs = False
    g_cam_yaw = 0.0
    g_cam_pitch = deg2rad(20.0)
    g_cam_dist = g_cfg.camera.distance

def cmd_align_to_missile():
    global g_cam_yaw, g_cam_pitch, g_view_mode_rcs
    g_view_mode_rcs = True
    g_cam_yaw = g_yaw
    g_cam_pitch = g_pitch

# ---------------------------
# Rendering
# ---------------------------

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    sdir = sun_dir_from_az_el(g_sun_az, g_sun_el)
    glLightfv(GL_LIGHT0, GL_POSITION, [sdir[0], sdir[1], sdir[2], 0.0])
    amb = 0.2 * g_sun_int
    dif = 0.8 * g_sun_int
    glLightfv(GL_LIGHT0, GL_AMBIENT,  [amb, amb, amb, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  [dif, dif, dif, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])

def draw_sun_disc():
    sdir = sun_dir_from_az_el(g_sun_az, g_sun_el)
    pos = sdir * 1000.0
    glPushMatrix()
    glDisable(GL_LIGHTING)
    glColor3f(1.0, 1.0, 0.9)
    glTranslatef(pos[0], pos[1], pos[2])
    glutSolidSphere(5.0, 16, 8)
    glEnable(GL_LIGHTING)
    glPopMatrix()

def draw_endless_ocean():
    tsize = g_cfg.ground.tile_size
    half_tiles = 6
    ox = math.floor(g_pos[0] / tsize) * tsize
    oz = math.floor(g_pos[2] / tsize) * tsize

    glDisable(GL_LIGHTING)
    glColor3f(0.02, 0.06, 0.20)
    for i in range(-half_tiles, half_tiles+1):
        for j in range(-half_tiles, half_tiles+1):
            x0 = ox + i * tsize; z0 = oz + j * tsize
            x1 = x0 + tsize;     z1 = z0 + tsize
            glBegin(GL_QUADS)
            glVertex3f(x0, 0.0, z0)
            glVertex3f(x1, 0.0, z0)
            glVertex3f(x1, 0.0, z1)
            glVertex3f(x0, 0.0, z1)
            glEnd()

    # grid lines every 10 m
    glColor4f(1.0, 1.0, 1.0, 0.08)
    glEnable(GL_BLEND); glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    step = tsize / 5.0
    N = half_tiles * 5
    glBegin(GL_LINES)
    for k in range(-N, N+1):
        x = ox + k * step
        glVertex3f(x, 0.001, oz - N*step); glVertex3f(x, 0.001, oz + N*step)
        z = oz + k * step
        glVertex3f(ox - N*step, 0.001, z); glVertex3f(ox + N*step, 0.001, z)
    glEnd()
    glDisable(GL_BLEND)
    glEnable(GL_LIGHTING)

def draw_world_axes_at_base(length=5.0):
    glDisable(GL_LIGHTING)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(1,0,0); glVertex3f(g_pos[0], g_pos[1], g_pos[2]); glVertex3f(g_pos[0]+length, g_pos[1], g_pos[2])  # X
    glColor3f(0,1,0); glVertex3f(g_pos[0], g_pos[1], g_pos[2]); glVertex3f(g_pos[0], g_pos[1]+length, g_pos[2])  # Y
    glColor3f(0,0,1); glVertex3f(g_pos[0], g_pos[1], g_pos[2]); glVertex3f(g_pos[0], g_pos[1], g_pos[2]+length)  # Z
    glEnd()
    glEnable(GL_LIGHTING)

def draw_heightmap():
    if g_heightmap_dl and g_hm_present:
        glCallList(g_heightmap_dl)

def draw_small_flame(dir_local: np.ndarray, length=0.6, radius=0.05, alpha=0.7):
    # rotate from -Z to dir_local
    src = np.array([0,0,-1], dtype=np.float32)
    dst = dir_local / (np.linalg.norm(dir_local) + 1e-9)
    ang, axis = axis_angle_from_to(src, dst)
    glPushMatrix()
    glRotatef(rad2deg(ang), axis[0], axis[1], axis[2])

    glDisable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glDepthMask(False)

    seg = 12
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(seg + 1):
        a = 2.0 * math.pi * i / seg
        nx = math.cos(a) * radius
        ny = math.sin(a) * radius
        glColor4f(1.0, 0.85, 0.3, alpha); glVertex3f(nx, ny, -0.03)
        glColor4f(1.0, 0.35, 0.0, 0.0);  glVertex3f(nx * 0.2, ny * 0.2, -length)
    glEnd()

    glDepthMask(True)
    glDisable(GL_BLEND)
    glEnable(GL_LIGHTING)
    glPopMatrix()

def draw_missile():
    glPushMatrix()

    # 1) Move to world tail (bottom)
    glTranslatef(g_pos[0], g_pos[1], g_pos[2])

    # 2) Shift so the tail sits at the origin in model space
    if g_cfg.model.forward_axis.upper() == "Z":
        glTranslatef(0.0, 0.0, -g_tail_offset_local)
    else:
        glTranslatef(0.0, -g_tail_offset_local, 0.0)

    # 3) Asset pre-rotation
    rx, ry, rz = g_cfg.model.pre_rotate_deg
    glRotatef(rx, 1, 0, 0); glRotatef(ry, 0, 1, 0); glRotatef(rz, 0, 0, 1)

    # 4) Align model forward to body forward
    model_forward = np.array([0,0,1], dtype=np.float32) if g_cfg.model.forward_axis.upper()=="Z" \
                    else np.array([0,1,0], dtype=np.float32)
    body_forward  = body_forward_from_angles(g_yaw, g_pitch)
    angle, axis = axis_angle_from_to(model_forward, body_forward)
    glRotatef(rad2deg(angle), axis[0], axis[1], axis[2])

    # 5) Material + geometry
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [0.85, 0.85, 0.9, 1.0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 32.0)
    was_cull = glIsEnabled(GL_CULL_FACE)
    if was_cull: glDisable(GL_CULL_FACE)
    glCallList(g_missile_dl)

    # 6) Main engine plume (only after launch & thrust > 1N)
    if g_has_launched and current_thrust(g_time) > 1.0:
        tail_dir_local = - (np.array([0,0,1], np.float32) if g_cfg.model.forward_axis.upper()=="Z"
                            else np.array([0,1,0], np.float32))
        glPushMatrix()
        drop = max(0.0, float(g_cfg.model.engine_drop_m))

        if g_cfg.model.forward_axis.upper()=="Z":
            # first: drop plume visually "below" the rocket (−Y in model space)
            glTranslatef(0.0, -drop, 0.0)
            # then: push a hair along −Z to avoid z-fighting with the tail rim
            glTranslatef(0.0, 0.0, -0.02)
        else:
            # forward is +Y, so −0.02 already goes “up the nozzle”; still drop by −Y
            glTranslatef(0.0, -(drop + 0.02), 0.0)

        draw_small_flame(
            tail_dir_local,
            length=min(6.0, 0.0025*current_thrust(g_time)+0.6),
            radius=0.18,
            alpha=0.85
        )
        glPopMatrix()

    # 7) RCS puffs (left/right at tail, up/down at nose)
    off_lat = max(0.05, g_cfg.model.length_estimate_m * 0.05)
    nose_fwd = max(0.2, g_cfg.model.length_estimate_m)
    if g_ctrl_left:
        glPushMatrix(); glTranslatef(+off_lat, 0.0, 0.0); draw_small_flame(np.array([+1,0,0], np.float32), length=0.7, radius=0.07, alpha=0.8); glPopMatrix()
    if g_ctrl_right:
        glPushMatrix(); glTranslatef(-off_lat, 0.0, 0.0); draw_small_flame(np.array([-1,0,0], np.float32), length=0.7, radius=0.07, alpha=0.8); glPopMatrix()
    if g_ctrl_up:
        if g_cfg.model.forward_axis.upper()=="Z":
            glPushMatrix(); glTranslatef(0.0, -off_lat, nose_fwd); draw_small_flame(np.array([0,-1,0], np.float32), length=0.7, radius=0.07, alpha=0.8); glPopMatrix()
        else:
            glPushMatrix(); glTranslatef(0.0, nose_fwd, -off_lat); draw_small_flame(np.array([0,-1,0], np.float32), length=0.7, radius=0.07, alpha=0.8); glPopMatrix()
    if g_ctrl_down:
        if g_cfg.model.forward_axis.upper()=="Z":
            glPushMatrix(); glTranslatef(0.0, +off_lat, nose_fwd); draw_small_flame(np.array([0,+1,0], np.float32), length=0.7, radius=0.07, alpha=0.8); glPopMatrix()
        else:
            glPushMatrix(); glTranslatef(0.0, nose_fwd, +off_lat); draw_small_flame(np.array([0,+1,0], np.float32), length=0.7, radius=0.07, alpha=0.8); glPopMatrix()

    if was_cull: glEnable(GL_CULL_FACE)
    glPopMatrix()

def set_perspective():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(g_cfg.camera.fov_deg, max(1, g_win_w) / float(max(1, g_win_h)), 0.1, 5000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def place_camera():
    r = g_cam_dist; cy = g_cam_pitch; cx = g_cam_yaw
    target = g_pos.copy()
    eye = target + np.array([
        r * math.sin(cx) * math.cos(cy),
        r * math.sin(cy),
        r * math.cos(cx) * math.cos(cy)
    ], dtype=np.float32)
    gluLookAt(eye[0], eye[1], eye[2], target[0], target[1], target[2], 0.0, 1.0, 0.0)

def draw_text_2d(x_px, y_px, s, font=GLUT_BITMAP_9_BY_15):
    glMatrixMode(GL_PROJECTION); glPushMatrix(); glLoadIdentity(); gluOrtho2D(0, g_win_w, 0, g_win_h)
    glMatrixMode(GL_MODELVIEW);  glPushMatrix(); glLoadIdentity()
    glDisable(GL_LIGHTING)
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(x_px, y_px)
    for ch in s:
        glutBitmapCharacter(font, ord(ch))
    glEnable(GL_LIGHTING)
    glPopMatrix(); glMatrixMode(GL_PROJECTION); glPopMatrix(); glMatrixMode(GL_MODELVIEW)

def draw_hud():
    alt = g_pos[1]
    thrust = current_thrust(g_time)
    mass = current_mass(g_time)
    pos = g_pos
    speed = float(np.linalg.norm(g_vel))
    acc   = float(np.linalg.norm(g_acc))
    yaw_deg = rad2deg(g_yaw); pitch_deg = rad2deg(g_pitch); roll_deg = rad2deg(g_roll)

    lines = [
        f"t = {g_time:6.2f} s   (Launch={'Yes' if g_has_launched else 'No'})",
        f"Altitude (y): {alt:8.2f} m",
        f"Velocity |v|: {speed:8.2f} m/s",
        f"Accel    |a|: {acc:8.2f} m/s^2",
        f"Position (x,y,z): ({pos[0]:.2f}, {pos[1]:.2f}, {pos[2]:.2f})",
        f"Orientation (yaw,pitch,roll): ({yaw_deg:.1f}, {pitch_deg:.1f}, {roll_deg:.1f}) deg",
        f"Thrust: {thrust:8.1f} N   Mass: {mass:7.2f} kg",
    ]
    pad = 12
    y = g_win_h - pad - 15
    for line in lines:
        w = len(line) * 9
        draw_text_2d(g_win_w - w - pad, y, line)
        y -= 18

def draw_controls_hint():
    lines = [
        "SPACE: Pause/Resume   L: Launch   R: Reset   C: Center Camera   A: Align to Missile",
        "Arrows: Steer (RCS)   Mouse: Drag=Orbit, Wheel=Zoom   [ / ]: Sun Az   ; / ': Sun El",
        "Grid: 10 m spacing, tiles 50 m. 1 unit = 1 m.",
    ]
    x = 12; y = 12
    for i, line in enumerate(lines):
        draw_text_2d(x, y + i*18, line)

# ---------------------------
# GLUT Callbacks
# ---------------------------

def on_display():
    glViewport(0, 0, g_win_w, g_win_h)
    sky_base = 0.55
    sky = sky_base + 0.25 * max(0.0, math.sin(deg2rad(g_sun_el)))
    glClearColor(0.4*sky, 0.6*sky, 0.9*sky, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    set_perspective()
    place_camera()
    setup_lighting()

    # fog
    glEnable(GL_FOG)
    glFogfv(GL_FOG_COLOR, (0.52, 0.70, 0.90, 1.0))
    glFogi(GL_FOG_MODE, GL_EXP2)
    glFogf(GL_FOG_DENSITY, 0.0022)

    draw_sun_disc()
    draw_endless_ocean()
    draw_heightmap()
    draw_missile()
    draw_world_axes_at_base(length=5.0)
    draw_hud()
    draw_controls_hint()

    glutSwapBuffers()

def on_reshape(w, h):
    global g_win_w, g_win_h
    g_win_w, g_win_h = max(1, w), max(1, h)

def on_timer(val):
    step_sim(1.0/60.0)
    glutPostRedisplay()
    glutTimerFunc(16, on_timer, 0)
    # **Fix:** only auto-align camera to missile in RCS view when NOT dragging
    if g_view_mode_rcs and not g_mouse_down:
        g_cam_yaw = g_yaw
        g_cam_pitch = g_pitch

def on_mouse(button, state, x, y):
    global g_mouse_down, g_last_mouse, g_cam_dist
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        g_mouse_down = True; g_last_mouse = (x, y); return
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        g_mouse_down = False
    if button == 3 and state == GLUT_DOWN:
        g_cam_dist = clamp(g_cam_dist * 0.9, g_cfg.camera.min_distance, g_cfg.camera.max_distance)
    elif button == 4 and state == GLUT_DOWN:
        g_cam_dist = clamp(g_cam_dist / 0.9, g_cfg.camera.min_distance, g_cfg.camera.max_distance)

def on_motion(x, y):
    global g_cam_yaw, g_cam_pitch, g_last_mouse
    if g_mouse_down:
        dx = x - g_last_mouse[0]; dy = y - g_last_mouse[1]
        g_last_mouse = (x, y)
        g_cam_yaw += dx * 0.005
        g_cam_pitch += -dy * 0.005
        g_cam_pitch = clamp(g_cam_pitch, deg2rad(-80), deg2rad(80))

def on_keyboard(key, x, y):
    global g_paused, g_cam_dist, g_sun_az, g_sun_el
    k = key.decode('utf-8') if isinstance(key, bytes) else key
    if k == ' ':
        g_paused = not g_paused
    elif k in ('l', 'L'):
        cmd_launch()
    elif k in ('r', 'R'):
        reset_sim()
    elif k in ('c','C'):
        cmd_center()
    elif k in ('a','A'):
        cmd_align_to_missile()
    elif k == '+':
        g_cam_dist = clamp(g_cam_dist * 0.9, g_cfg.camera.min_distance, g_cfg.camera.max_distance)
    elif k == '-':
        g_cam_dist = clamp(g_cam_dist / 0.9, g_cfg.camera.min_distance, g_cfg.camera.max_distance)
    elif k == '[':
        g_sun_az -= 0.5
    elif k == ']':
        g_sun_az += 0.5
    elif k == ';':
        g_sun_el = clamp(g_sun_el - 0.5, -5.0, 89.0)
    elif k == "'":
        g_sun_el = clamp(g_sun_el + 0.5, -5.0, 89.0)

def on_special(key, x, y):
    global g_ctrl_left, g_ctrl_right, g_ctrl_up, g_ctrl_down
    if key == GLUT_KEY_LEFT:  g_ctrl_left  = True
    if key == GLUT_KEY_RIGHT: g_ctrl_right = True
    if key == GLUT_KEY_UP:    g_ctrl_up    = True
    if key == GLUT_KEY_DOWN:  g_ctrl_down  = True

def on_special_up(key, x, y):
    global g_ctrl_left, g_ctrl_right, g_ctrl_up, g_ctrl_down
    if key == GLUT_KEY_LEFT:  g_ctrl_left  = False
    if key == GLUT_KEY_RIGHT: g_ctrl_right = False
    if key == GLUT_KEY_UP:    g_ctrl_up    = False
    if key == GLUT_KEY_DOWN:  g_ctrl_down  = False

# ---------------------------
# Init & Main
# ---------------------------

def load_config(path: Optional[str]) -> AppConfig:
    default = {
        "sun": {"azimuth_deg": 45.0, "elevation_deg": 25.0, "intensity": 1.0},
        "rocket": {
            "dry_mass": 50.0, "propellant_mass": 50.0, "Cd": 0.5, "A_ref": 0.05,
            "rho_air": 1.225, "g": 9.81,
            "thrust_curve": [[0, 2500], [2, 2400], [4, 1800], [6, 800], [7, 200], [8, 0]],
            "launch_azimuth_deg": 10.0, "launch_elevation_deg": 90.0,
            "initial_pos": [0.0, 0.1, 0.0],
            "thrust_aligns_with_velocity": False,
            "rcs_force_N": 1200.0, "yaw_inertia": 300.0, "pitch_inertia": 400.0, "rcs_damping": 0.6
        },
        "camera": {"distance": 12.0, "min_distance": 4.0, "max_distance": 200.0, "fov_deg": 60.0},
        "ground": {
            "tile_size": 50.0,
            "color_ocean": [0.1, 0.3, 0.7],
            "color_land": [0.0, 0.65, 0.0],
            "heightmap_path": "assets/0811.tif",
            "heightmap_vertical_scale": 0.02,
            "heightmap_downsample_to": 256
        },
        "model": {
        "path": "assets/rocket.obj",
        "scale": 1.0,
        "forward_axis": "Y",
        "pre_rotate_deg": [0.0, 0.0, 0.0],
        "length_estimate_m": 10.0,
        "engine_drop_m": 1.0
        },
        "graphics": {"msaa": True}
    }
    if path and os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            user = json.load(f)
        def merge(a, b):
            for k, v in b.items():
                if isinstance(v, dict) and k in a and isinstance(a[k], dict):
                    merge(a[k], v)
                else:
                    a[k] = v
        merge(default, user)

    sun = SunConfig(**default["sun"])
    rock = RocketConfig(**default["rocket"])
    cam = CameraConfig(**default["camera"])
    grd = GroundConfig(**default["ground"])
    mdl = ModelConfig(**default["model"])
    gfx = GraphicsConfig(**default["graphics"])
    return AppConfig(sun, rock, cam, grd, mdl, gfx)

def main():
    global g_cfg, g_missile_dl, g_heightmap_dl, g_mass0, g_burn_time
    global g_cam_dist, g_sun_az, g_sun_el, g_sun_int, g_base_dir

    # Parse args (optional)
    cfg_path = None
    if "--config" in sys.argv:
        i = sys.argv.index("--config")
        if i + 1 < len(sys.argv):
            cfg_path = sys.argv[i+1]
    # Autoload config.json if present
    if not cfg_path:
        candidate = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        if os.path.isfile(candidate):
            cfg_path = candidate

    g_base_dir = os.path.dirname(os.path.abspath(cfg_path)) if cfg_path else os.path.dirname(os.path.abspath(__file__))
    g_cfg = load_config(cfg_path)

    # Requested quick shrink x0.01
    g_cfg.model.scale *= 0.01

    # Resolve assets
    g_cfg.model.path = resolve_path(g_cfg.model.path)
    g_cfg.ground.heightmap_path = resolve_path(g_cfg.ground.heightmap_path)
    print(f"[paths] model: {g_cfg.model.path}")
    print(f"[paths] heightmap: {g_cfg.ground.heightmap_path}")

    # Derived
    g_sun_az = g_cfg.sun.azimuth_deg
    g_sun_el = g_cfg.sun.elevation_deg
    g_sun_int = g_cfg.sun.intensity

    tc = g_cfg.rocket.thrust_curve or [[0,0]]
    g_burn_time = tc[-1][0]
    g_mass0 = g_cfg.rocket.dry_mass + g_cfg.rocket.propellant_mass

    # GLUT
    glutInit(sys.argv)
    display_mode = GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH
    if g_cfg.graphics.msaa and hasattr(GLUT, 'GLUT_MULTISAMPLE'):
        display_mode |= GLUT_MULTISAMPLE
    glutInitDisplayMode(display_mode)
    glutInitWindowSize(g_win_w, g_win_h)
    glutCreateWindow(b"Missile Launch Simulation (PyOpenGL)")

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    # Load
    g_missile_dl = build_missile_display_list(g_cfg.model)
    g_heightmap_dl = try_build_heightmap_display_list(g_cfg.ground)

    reset_sim()

    # Hooks
    glutDisplayFunc(on_display)
    glutReshapeFunc(on_reshape)
    glutMouseFunc(on_mouse)
    glutMotionFunc(on_motion)
    glutKeyboardFunc(on_keyboard)
    glutSpecialFunc(on_special)
    try:
        glutSpecialUpFunc(on_special_up)  # if your GLUT lacks this, it’s fine
    except Exception:
        pass
    glutTimerFunc(16, on_timer, 0)

    print("Controls: SPACE=pause/resume, L=launch, R=reset, C=world view, A=align to missile, arrows=steer, mouse drag=orbit, wheel=zoom, +/-=zoom, [ ]=sun az, ; '=sun el")
    print("Note: model scale x0.01 at startup. Grid lines = 10 m; tiles = 50 m.")
    glutMainLoop()

if __name__ == "__main__":
    main()
