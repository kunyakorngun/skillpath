import streamlit as st
from function.public_function import load_css
from widget.widget import navbar, script_footer
from streamlit_extras.stylable_container import stylable_container


st.set_page_config(
	page_icon="🧊",
	layout="wide"
)

load_css("src/style/hide_header.css")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

navbar()

# ---------------------------------------------------------------------------- #
#                                     Body                                     #
# ---------------------------------------------------------------------------- #

# empty_c1, col_2, col_3, col_4, col_5, empty_c6 = st.columns(6)
# with col_2:
#     keywords = st.text_input("What", placeholder="Enter keywords")
# with col_3:
#     option = st.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone"),
#     index=None,
#     placeholder="Any classification",
#     label_visibility="hidden")
# with col_4:
#     city = st.text_input("Where", placeholder="Enter city ")
# with col_5:
#     st.write("Column 5")

with st.form("my_form", border=False): #st.form ฟอร์มสำหรบัใส่ข้อความที่มีการส่งไปจริงๆ
	empty_c1, col_2, col_3, col_4, col_5, empty_c6 = st.columns(6)
	with col_2:
		keywords = st.text_input("What", placeholder="Enter keywords")
	with col_3:
		option = st.selectbox(
		"How would you like to be contacted?",
		("Email", "Home phone", "Mobile phone"),
		index=None,
		placeholder="Any classification",
		label_visibility="hidden")
	with col_4:
		city = st.text_input("Where", placeholder="Enter city ")
	with col_5:
		with stylable_container(
			key="submit_style",
			css_styles="""
				button {
					background-color: #E5785B;
					color: white;
					border-radius: 5px;
					margin-top: 28px;
				}
				button:hover {
					background-color: rgb(229 120 91 / 65%) !important;
				}
				""",
		):
			submitted = st.form_submit_button("Submit", width="stretch")



# ---------------------------------------------------------------------------- #

script_footer()