import streamlit as st
from function.public_function import load_css, load_image
from widget.widget import navbar, script_footer
from streamlit_extras.stylable_container import stylable_container
from clean.neo4j_skillpath import Neo4jSkillPath
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
	page_icon="🧊",
	layout="wide"
)

load_css("src/style/hide_header.css")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

navbar()

neo4jskillpath = Neo4jSkillPath("neo4j://neo4j:7687", "neo4j", os.getenv("NEO4J_PASSWORD"), os.getenv("NEO4J_DB_NAME"))


# ---------------------------------------------------------------------------- #
#                                     Body                                     #
# ---------------------------------------------------------------------------- #

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


recommended_job_config = {
	'scg_Data Scientist': {
		'logo': 'src/img/scg_logo.svg',
		'title': 'Data Scientist',
		'company': 'The Siam Cement Public Company Limited (SCG)',
		'location': 'Bangkok',
		'salary': '฿9,500 per month', 
		'description': 'We are looking for Data Scientist who can help design the entire Model ...',
		'skills': ['Python', 'Machine Learning', 'SQL', 'Statistics', 'Visualization']
	},
	'scg_Data Engineer': {
		'logo': 'src/img/scg_logo.svg',
		'title': 'Data Engineer',
		'company': 'The Siam Cement Public Company Limited (SCG)',
		'location': 'Bangkok',
		'salary': '฿12,000 per month',
		'description': 'Join our DE team to create intuitive and delightful experiences for users ...',
  		'skills': ['Python', 'SQL', 'ETL', 'Docker']
	},
	'ptt_Machine Learning Engineer': {
		'logo': 'src/img/ptt_logo.svg',
		'title': 'Machine Learning Engineer',
		'company': 'PTT Public Company Limited (PTT)',
		'location': 'Bangkok',
		'salary': '฿12,000 per month',
		'description': 'Join our Machine Learning Engineer to create intuitive and delightful experiences for users ...',
  		'skills': ['Python', 'MLOps', 'Docker']
	},
	'ptt_Data Analyst': {
		'logo': 'src/img/ptt_logo.svg',
		'title': 'Data Analyst',
		'company': 'PTT Public Company Limited (PTT)',
		'location': 'Bangkok',
		'salary': '฿5,000 per month',
		'description': 'Join our Data Analyst team to create intuitive and delightful experiences for users ...',
		'skills': ['Python', 'SQL', 'Visualization']
	},
	'scg_Business Analyst': {
		'logo': 'src/img/scg_logo.svg',
		'title': 'Business Analyst',
		'company': 'The Siam Cement Public Company Limited (SCG)',
		'location': 'Bangkok',
		'salary': '฿7,000 per month',
		'description': 'Join our Business Analyst team to create intuitive and delightful experiences for users ...',
		'skills': ['SQL', 'Visualization']
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
					<a href="/Job_Page" target="_self" style='margin: 0; font-weight: bold; font-size: 18px; color: black; text-decoration: none;'>{job['title']}</a>
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


# ------------------------------ matching neo4j ------------------------------ #

# ------------------------------------ end ----------------------------------- #

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