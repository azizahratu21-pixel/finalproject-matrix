
# app.py
import streamlit as st
from PIL import Image
import numpy as np
from languages import LANG

# ----------------------
# PAGE CONFIG
# ----------------------
st.set_page_config(
    page_title="Matrix Transformations in Image Processing",
    layout="wide"
)

# ----------------------
# LANGUAGE STATE + SWITCHER
# ----------------------
if "lang" not in st.session_state:
    st.session_state.lang = "id"

lang_choice = st.sidebar.radio(
    "Language / Bahasa",
    ["id", "en"],
    index=0 if st.session_state.lang == "id" else 1
)
st.session_state.lang = lang_choice

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
# CONTENT
# ----------------------
st.title(T["app_title"])

st.markdown(T["app_intro"])

st.header(T["matrix_brief_title"])
st.markdown(T["matrix_brief_desc"])

st.header(T["conv_brief_title"])
st.markdown(T["conv_brief_desc"])

st.write("---")
st.info(T["cta_image_page"])


