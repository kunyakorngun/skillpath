import streamlit as st
import base64

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_image(image_path):
    with open(image_path, "rb") as f:
        contents = f.read()
        data_url = base64.b64encode(contents).decode("utf-8")
    return data_url