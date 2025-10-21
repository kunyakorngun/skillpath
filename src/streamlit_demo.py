import streamlit as st
from function.public_function import load_css, load_image
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


# custom_css = """
# <style>
#     /* กำหนด CSS Class ที่เราจะใช้กับ <div> ของเรา */
#     .custom-padded-box {
#         /* สไตล์ตามที่ต้องการ */
#         border-radius: 16px; /* ขอบโค้งมน */
#         background-color: #e0f7fa; /* สีพื้นหลังอ่อนๆ (Light Cyan) */
#         border: 2px solid #00bcd4; /* ขอบสีฟ้า */
#         padding: 30px; /* เพิ่ม padding ภายในกล่อง */
#         margin-top: 15px;
#         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
#     }
# </style>
# """
# แทรก CSS เข้าไปในหน้าเว็บ
# st.markdown(custom_css, unsafe_allow_html=True)
# ------------------------------------------------------------------

recommended_job_config = {
	'scg_figma': {
		'logo': 'src/img/scg_logo.svg',
		'title': 'Figma Designer',
		'company': 'The Siam Cement Public Company Limited (SCG)',
		'location': 'Bangkok',
		'salary': '฿9,500 per month', 
		'description': 'We are looking for Figma designers who can help design the entire mobile application ...',
		'skills': ['Ui Designer', 'Figma', 'Landing Page', 'User Research']
	},
	'scg_ux': {
		'logo': 'src/img/scg_logo.svg',
		'title': 'UX Designer',
		'company': 'The Siam Cement Public Company Limited (SCG)',
		'location': 'Bangkok',
		'salary': '฿12,000 per month',
		'description': 'Join our UX team to create intuitive and delightful experiences for users ...',
  		'skills': ['Ui Designer', 'Figma', 'Landing Page']
	},
	'scg_ug': {
		'logo': 'src/img/scg_logo.svg',
		'title': 'UX Designer',
		'company': 'The Siam Cement Public Company Limited (SCG)',
		'location': 'Bangkok',
		'salary': '฿12,000 per month',
		'description': 'Join our UX team to create intuitive and delightful experiences for users ...',
  		'skills': ['Ui Designer', 'Figma']
	},
	'scg_ui': {
		'logo': 'src/img/scg_logo.svg',
		'title': 'UX Designer',
		'company': 'The Siam Cement Public Company Limited (SCG)',
		'location': 'Bangkok',
		'salary': '฿12,000 per month',
		'description': 'Join our UX team to create intuitive and delightful experiences for users ...',
		'skills': ['Ui Designer', 'Figma']
	}
}

empty_c1, col_2, col_3, empty_c4 = st.columns([0.5, 5.5, 3.5, 0.5])

# Display job cards
for key, job in recommended_job_config.items():
	with col_2:
		if key == list(recommended_job_config.keys())[0]:
			st.markdown("<h4 style='color:#1E3A8A; font-size:20px; font-weight:600;'>Recommend Job</h4>",unsafe_allow_html=True)
		st.markdown(f"""
		<div class='d-flex flex-row bg-white text-dark' 
			style='height: 155px; border-radius: 10px; padding: 18px 36px; margin-bottom: 20px;'>
			<div class='d-flex flex-row align-items-center' style='flex: 1;'>
				<div style='margin: 20px;'>
					<img src="data:image/svg+xml;base64,{load_image(job['logo'])}" width="50"/>
				</div>
				<div>
					<p style='margin: 0; font-weight: bold; font-size: 18px;'>{job['title']}</p>
					<p style='margin: 0;'>{job['company']}</p>
					<p style='margin: 5px 0 0 0;'>
						<img src="data:image/svg+xml;base64,{load_image("src/img/Location.svg")}" 
							width="14" style="vertical-align: middle;"/> {job['location']}
					</p>
					<p style='margin: 0; color: #333;'>{job['salary']}</p>
					<p style='margin: 5px 0 0 0; color: #666; font-size: 14px;'>{job['description']}</p>
				</div>
			</div>
		</div>
		""", unsafe_allow_html=True)

def create_skill_badge(skills: list):
    badges_html = ""
    for skill in skills:
        badges_html += f"""
        <div style='
            display: inline-block;
            background-color: rgb(219, 222, 229);
            color: rgb(101, 101, 101);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 14px;
            font-weight: 500;
            margin: 0;'>{skill}</div>
        """
    return badges_html  # คืนค่า HTML เป็น string

for key, job in recommended_job_config.items():
    with col_3:
        if key == list(recommended_job_config.keys())[0]:
            st.markdown("<h4 style='color:#1E3A8A; font-size:20px; font-weight:600;'>Skill Matching</h4>",unsafe_allow_html=True)
        st.markdown(f"""
        <div style='
            background-color: white;
            color: black;
            height: 155px;
            border-radius: 10px;
            padding: 18px 36px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
            '>
            <div style='
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                justify-content: flex-start;
                align-items: center;
                overflow: auto;
                padding-top: 8px;'>
                {create_skill_badge(job['skills'])}
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------------------------- #

script_footer()