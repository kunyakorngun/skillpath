import streamlit as st
from function.public_function import load_css, load_image
from widget.widget import navbar, script_footer
from streamlit_extras.stylable_container import stylable_container


st.set_page_config(
	layout="wide"
)
load_css("src/style/hide_header.css")
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
navbar()

st.title("For Company")


# ---------------------------------------------------------------------------- #
script_footer()