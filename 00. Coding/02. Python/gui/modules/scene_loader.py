# modules/scene_loader.py
from __future__ import annotations


import ctypes
import numpy as np
import json, pathlib
from osgeo import gdal
from typing import Tuple
from OpenGL.GL import *

BASE_Y_OFFSET = 0.0            # shift terrain up/down if sea level ≠ 0
CFG_PATH = pathlib.Path("assets/scene_config.json")
class GLScene:
    """Contains VAO ids & draw counts for terrain + rocket."""
    def __init__(self):
        self.terr_vao: int = 0
        self.terr_count: int = 0
        self.rocket_vao: int = 0
        self.rocket_count: int = 0

def load_config() -> dict:
    if CFG_PATH.exists():
        with CFG_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    else:                              # first run → write defaults
        CFG_PATH.write_text(json.dumps({}, indent=2))
        return {}

def _vao_from_arrays(vertices: np.ndarray, indices: np.ndarray) -> Tuple[int, int]:
    """Create VAO with a single vbo (pos+normal) & ibo.  Returns (vao, index_count)."""
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    ibo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    stride = 6 * 4  # 3 pos + 3 normal, float32
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(12))

    glBindVertexArray(0)
    return vao, indices.size

def load_simple_obj(path: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Return (vpos, vnor) from an OBJ containing only 'v', 'vn', 'f' lines.
    Faces must be triangles (v//vn or v/vt/vn or v//).
    """
    v, vn, idx_v, idx_n = [], [], [], []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("v "):
                v.append([float(x) for x in line.strip().split()[1:4]])
            elif line.startswith("vn "):
                vn.append([float(x) for x in line.strip().split()[1:4]])
            elif line.startswith("f"):
                parts = line.strip().split()[1:]
                for p in parts:
                    fields = p.split("/")
                    idx_v.append(int(fields[0]) - 1)
                    if len(fields) >= 3 and fields[2]:
                        idx_n.append(int(fields[2]) - 1)
    v = np.asarray(v, dtype=np.float32)
    vn = np.asarray(vn, dtype=np.float32) if vn else np.zeros_like(v)
    # expand per-index
    vpos = v[idx_v]
    vnor = vn[idx_n] if len(idx_n) == len(idx_v) else np.zeros_like(vpos)
    return vpos, vnor

# -------------------------------------------------------------------------
def load_scene() -> GLScene:
    cfg = load_config()
    sc = GLScene()
    # ---- TERRAIN --------------------------------------------------------
    dem_path = "assets/dem.tif"
    ds = gdal.Open(dem_path, gdal.GA_ReadOnly)
    band = ds.GetRasterBand(1)
    cols = ds.RasterXSize
    rows = ds.RasterYSize
    # z = ds.GetRasterBand(1).ReadAsArray().astype(np.float32)
    data = band.ReadRaster(0, 0, cols, rows, buf_type=gdal.GDT_Float32)
    z = np.frombuffer(data, dtype=np.float32).reshape(rows, cols)
    gt = ds.GetGeoTransform()
    sx, sy = gt[1], abs(gt[5])
    vs = cfg.get("terrain", {}).get("vertical_scale", 1.0)
    vo = cfg.get("terrain", {}).get("vertical_offset", 0.0)   # <— NEW
    z = z * vs + vo

    h, w = z.shape
    xs, zs = np.meshgrid(np.arange(w)*sx, np.arange(h)*sy)  # 2-D grids
    verts = np.stack([xs, z, zs], axis=-1)                  # (h,w,3)
    # flat-shade normal = cross(Δx, Δy)
    dzdx = np.gradient(z, axis=1) / sx
    dzdy = np.gradient(z, axis=0) / sy
    nx = -dzdx
    ny = np.ones_like(z)
    nz = -dzdy
    normals = np.stack([nx, ny, nz], axis=-1)
    normals /= np.linalg.norm(normals, axis=-1, keepdims=True)+1e-8

    vert_flat = np.concatenate([verts, normals], axis=-1).astype(np.float32).reshape(-1,6)

    # indices for GL_TRIANGLES using grid strips
    idx = []
    for r in range(h-1):
        for c in range(w-1):
            v0 = r*w + c
            v1 = v0 + 1
            v2 = v0 + w
            v3 = v2 + 1
            idx.extend([v0,v2,v1,  v1,v2,v3])
    idx = np.asarray(idx, dtype=np.uint32)

    sc.terr_vao, sc.terr_count = _vao_from_arrays(vert_flat, idx)

    # ---- ROCKET ---------------------------------------------------------
    vpos, vnor = load_simple_obj("assets/rocket.obj")
    v = np.hstack([vpos, vnor])                # (n,6)
    indices = np.arange(len(v), dtype=np.uint32)
    sc.rocket_vao, sc.rocket_count = _vao_from_arrays(v, indices)

    # ---- OCEAN PLANE ----------------------------------------------------
    ocean_verts = np.array([
        [-200000, 0, -200000, 0,1,0],
        [ 200000, 0, -200000, 0,1,0],
        [ 200000, 0,  200000, 0,1,0],
        [-200000, 0,  200000, 0,1,0],
    ], np.float32)
    ocean_idx = np.array([0,1,2, 0,2,3], np.uint32)
    sc.ocean_vao, sc.ocean_count = _vao_from_arrays(ocean_verts, ocean_idx)

    return sc, cfg
