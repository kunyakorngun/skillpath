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

# jobs = [
#     {
#         "position": "Figma Designer",
#         "company": "The Siam Cement Public Company Limited (SCG.)",
#         "location": "Bangkok",
#         "status": "Read by HR",
#         "date": "Sep 20, 2025",
#         "progress": 2  # 1=Sent Resume, 2=Read by HR, 3=Interview Appointment, 4=Interview Results
#     },
#     {
#         "position": "UX/UI Designer",
#         "company": "The Siam Cement Public Company Limited (SCG.)",
#         "location": "Bangkok",
#         "status": "Sent Resume",
#         "date": "Sep 20, 2025",
#         "progress": 1
#     }
# ]

# empty_c1, col_2, empty_c3 = st.columns([0.5, 9, 0.5])

# # st.markdown("""
# # 		<style>
# # 		.stSelectbox {
# # 			width: 300px !important;
# # 			margin-left: auto;
# # 		}
# # 		</style>
# # 		""", unsafe_allow_html=True)

# # with col2:
# # 	st.selectbox(
# # 		"Position Applied",
# # 		[job["position"] for job in jobs],
# # 		index=None,
# # 		placeholder="Candidate Profile",
# # 		label_visibility="collapsed"
# # 	)
 
# # 	st.markdown("<h4>Applied Process</h4>", unsafe_allow_html=True)

# with col_2:
# 		st.markdown("""
# 		<style>
# 		.stSelectbox {
# 			width: 300px;
# 			margin-left: auto;
# 		}
# 		</style>
# 		""", unsafe_allow_html=True)
# 		option = st.selectbox(
# 					"How would you like to be contacted?",
# 					("Figma Designer", "UX/UI Designer"),
# 					index=None,
# 					placeholder="Position Applied",
# 					label_visibility="collapsed")
# 		st.markdown("<h4 style='color:#1E3A8A; font-size:20px; font-weight:600;'>Applied Process/ Activity Updated</h4>",unsafe_allow_html=True)
# 		st.markdown(f"""
# 		<div class='d-flex flex-row bg-white text-dark' 
# 			style='height: 155px; border-radius: 10px; padding: 100px 36px; margin-bottom: 20px;'>
# 			<div class='d-flex flex-row align-items-center' style='flex: 1;'>
# 			</div>
# 		</div>
# 		""", unsafe_allow_html=True)



jobs = [
    {
        "name": "Christina Jolo",
        "position": "Data Scientist",
        "skills": ['Python', 'Machine Learning', 'SQL', 'Statistics', 'Visualization']
    },
    {
        "name": "Jonathan Lee",
        "position": "Data Engineer",
        "skills": ['Python', 'SQL', 'ETL', 'Docker']
    }
]

# --- Function: Skill Badges ---
def create_skill_badge(skills: list):
    badges_html = ""
    for skill in skills:
        badges_html += f"""
        <div style='
            display: inline-block;
            background-color: rgb(243, 243, 243);
            color: rgb(101, 101, 101);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 13px;
            font-weight: 500;
            margin-right: 8px;
            margin-bottom: 6px;'>{skill}</div>
        """
    return badges_html

# --- Layout: 3 Columns (ซ้าย กลาง ขวา) ---
empty_c1, col_2, empty_c3 = st.columns([0.5, 9, 0.5])

with col_2:
    st.markdown("""
    <style>
    .stSelectbox {
        width: 300px !important;
        margin-left: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    st.selectbox(
        "Position Applied",
        [job["position"] for job in jobs],
        index=None,
        placeholder="Position Applied",
        label_visibility="collapsed"
    )

    st.markdown("<h4 style='color:#1E3A8A; font-size:20px; font-weight:600;'>Applied Process / Activity Updated</h4>", unsafe_allow_html=True)

    # --- Render Job Cards ---
    for job in jobs:
        st.markdown(f"""
        <div style='
            background-color: white;
            color: black;
            height: 155px;
            border-radius: 10px;
            padding: 18px 36px;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;'>
            <div style='flex: 8; display: flex; flex-direction: column; justify-content: space-between; height: 100%;'>
                <div style='line-height: 1.6;'>
                    <div><b>Name:</b> {job["name"]}</div>
                    <div><b>Position:</b> {job["position"]}</div>
                </div>
                <div>
                    <button style='
                        padding: 6px 18px;
                        background-color: #E5E7EB;
                        border: none;
                        border-radius: 6px;
                        color: #4B5563;
                        font-weight: 500;
                        cursor: pointer;'>View Resume</button>
                </div>
            </div>
            <div style='flex: 8; display: flex; flex-direction: column; justify-content: space-between; height: 100%;'>
                <div>
                    <b>Skills</b>
                    <div style='
                        display: flex;
                        flex-wrap: wrap;
                        gap: 8px;
                        margin-top: 8px;
                        flex-direction: row;
                        align-items: center;
                        '>
                        {create_skill_badge(job["skills"])}
        </div>
        <div style='
                display: flex;
                flex-direction: row;
                align-items: center;
                gap: 40px;
                margin-top: 10px;'>
                <div class='status-info' style='display:flex; align-items:center; gap:8px; cursor:pointer;'>
                    <div class='status-icon' style='
                        width: 24px;
                        height: 24px;
                        background-color: #22C55E;
                        color: white;
                        border-radius: 50%;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-weight: bold;
                        font-size:14px;'>✔</div>
                    <span style='font-weight:500;'>Approve</span>
        <div class='status-info' style='display:flex; align-items:center; gap:8px; cursor:pointer; padding-left: 55px;'>
                    <div class='status-icon' style='
                        width: 24px;
                        height: 24px;
                        background-color: #EF4444;
                        color: white;
                        border-radius: 50%;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-weight: bold;
                        font-size:14px;'>✖</div>
                    <span style='font-weight:500;'>Reject</span>
                </div>
                </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------------------------- #
script_footer()