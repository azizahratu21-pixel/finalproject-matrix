# image_processing.py
import streamlit as st
from PIL import Image
import numpy as np
import math
from languages import LANG

# ----------------------
# PAGE CONFIG
# ----------------------
st.set_page_config(layout="wide")

# ----------------------
# LANGUAGE (GLOBAL STATE)
# ----------------------
if "lang" not in st.session_state:
    st.session_state.lang = "id"

T = LANG[st.session_state.lang]

# ----------------------
# CSS
# ----------------------
page_bg = """
<style>
html, body, [class*="css"]  {
    background-color: #DDE5D5 !important;   
}

.stApp {
    background-color: #DDE5D5 !important;
}

header[data-testid="stHeader"] {
    background-color: #DDE5D5 !important;
}

main[data-testid="stMain"] {
    background-color: #DDE5D5 !important;
    padding-top: 0 !important;
}

.block-container {
    background-color: #DDE5D5 !important;
}

[data-testid="stSidebar"] {
    background-color: #DDE5D5 !important;
}

.feature-box {
    background-color: #C3D1C0;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------------------
# TITLE
# ----------------------
st.title(T["ip_title"])

# ======================================================
# Utility functions (NO TRANSLATION – PURE NUMERICS)
# ======================================================
def pil_to_np(img: Image.Image):
    arr = np.array(img.convert("RGBA")).astype(np.float32) / 255.0
    return arr

def np_to_pil(arr: np.ndarray):
    arr8 = np.clip(arr * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(arr8, mode="RGBA")

def make_translation(tx, ty):
    M = np.eye(3)
    M[0, 2] = tx
    M[1, 2] = ty
    return M

def make_scaling(sx, sy):
    M = np.eye(3)
    M[0, 0] = sx
    M[1, 1] = sy
    return M

def make_rotation(deg):
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    return np.array([[c, -s, 0],
                     [s,  c, 0],
                     [0,  0, 1]], dtype=float)

def make_shear(shx, shy):
    M = np.eye(3)
    M[0, 1] = shx
    M[1, 0] = shy
    return M

def make_reflection(axis):
    if axis == "x-axis":
        return np.array([[1,0,0],[0,-1,0],[0,0,1]], float)
    if axis == "y-axis":
        return np.array([[-1,0,0],[0,1,0],[0,0,1]], float)
    if axis == "origin":
        return np.array([[-1,0,0],[0,-1,0],[0,0,1]], float)
    if axis == "y=x":
        return np.array([[0,1,0],[1,0,0],[0,0,1]], float)
    return np.eye(3)

def bilinear_sample(img, x, y):
    h, w = img.shape[:2]
    if x < 0 or x >= w-1 or y < 0 or y >= h-1:
        return np.array([0,0,0,0], dtype=np.float32)
    x0, y0 = int(x), int(y)
    dx, dy = x-x0, y-y0
    top = (1-dx)*img[y0,x0] + dx*img[y0,x0+1]
    bottom = (1-dx)*img[y0+1,x0] + dx*img[y0+1,x0+1]
    return (1-dy)*top + dy*bottom

def warp_image(src_img, M, out_shape=None):
    h, w = src_img.shape[:2]
    out_h, out_w = out_shape if out_shape else (h, w)
    dst = np.zeros((out_h, out_w, 4), dtype=np.float32)
    invM = np.linalg.inv(M)

    for j in range(out_h):
        for i in range(out_w):
            src = invM @ np.array([i, j, 1.0])
            dst[j, i] = bilinear_sample(src_img, src[0], src[1])
    return dst

def conv2d_image(img, kernel):
    kh, kw = kernel.shape
    pad = kh // 2
    rgb, alpha = img[..., :3], img[..., 3:]
    padded = np.pad(rgb, ((pad,pad),(pad,pad),(0,0)), mode="edge")
    out = np.zeros_like(rgb)

    for y in range(rgb.shape[0]):
        for x in range(rgb.shape[1]):
            region = padded[y:y+kh, x:x+kw]
            out[y,x] = (region * kernel[...,None]).sum(axis=(0,1))

    return np.concatenate([np.clip(out,0,1), alpha], axis=2)

# ======================================================
# UI
# ======================================================
col1, col2 = st.columns([1, 2])

with col1:
    uploaded = st.file_uploader(T["upload_image"], type=["png","jpg","jpeg"])

    st.markdown(T["transform_order"])
    order_mode = st.radio(
        T["order_mode"],
        (T["preset_order"], T["custom_order"])
    )

    choices = ["Translation","Scaling","Rotation","Shearing","Reflection"]
    order = choices if order_mode == T["preset_order"] else \
            st.multiselect(T["select_order"], choices, default=choices)

    st.markdown("---")
    st.subheader(T["translation"])
    t_enable = st.checkbox(T["enable_translation"])
    tx = st.number_input("tx", 0.0)
    ty = st.number_input("ty", 0.0)

    st.subheader(T["scaling"])
    s_enable = st.checkbox(T["enable_scaling"])
    sx = st.number_input("sx", 1.0)
    sy = st.number_input("sy", 1.0)
    scale_center = st.checkbox(T["scale_center"], True)

    st.subheader(T["rotation"])
    r_enable = st.checkbox(T["enable_rotation"])
    angle = st.slider(T["angle"], -360, 360, 0)

    st.subheader(T["shearing"])
    sh_enable = st.checkbox(T["enable_shearing"])
    shx = st.number_input("shx", 0.0)
    shy = st.number_input("shy", 0.0)

    st.subheader(T["reflection"])
    rf_enable = st.checkbox(T["enable_reflection"])
    rf_axis = st.selectbox(T["axis"], ["x-axis","y-axis","origin","y=x"])

    st.markdown("---")
    st.subheader(T["filters"])
    apply_blur = st.checkbox(T["blur"])
    apply_sharpen = st.checkbox(T["sharpen"])

    do_apply = st.button(T["apply"])

with col2:
    st.subheader(T["preview"])

    if uploaded is None:
        st.info(T["upload_hint"])
    else:
        img = Image.open(uploaded).convert("RGBA")
        src = pil_to_np(img)
        h, w = src.shape[:2]
        cx, cy = (w-1)/2, (h-1)/2

        M_total = np.eye(3)
        for step in order:
            if step=="Translation" and t_enable:
                M_total = make_translation(tx,ty) @ M_total
            if step=="Scaling" and s_enable:
                if scale_center:
                    M = make_translation(cx,cy) @ make_scaling(sx,sy) @ make_translation(-cx,-cy)
                else:
                    M = make_scaling(sx,sy)
                M_total = M @ M_total
            if step=="Rotation" and r_enable:
                M = make_translation(cx,cy) @ make_rotation(angle) @ make_translation(-cx,-cy)
                M_total = M @ M_total
            if step=="Shearing" and sh_enable:
                M_total = make_shear(shx,shy) @ M_total
            if step=="Reflection" and rf_enable:
                M = make_translation(cx,cy) @ make_reflection(rf_axis) @ make_translation(-cx,-cy)
                M_total = M @ M_total

        out = warp_image(src, M_total)
        if apply_blur:
            out = conv2d_image(out, np.ones((3,3))/9)
        if apply_sharpen:
            out = conv2d_image(out, np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]))

        c1, c2 = st.columns(2)
        c1.image(np_to_pil(src), caption=T["original"])
        c2.image(np_to_pil(out), caption=T["result"])

        st.markdown(T["matrix_used"])
        st.write(np.round(M_total, 5))
