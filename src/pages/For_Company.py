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

# # --- Function: Skill Badges ---
# def create_skill_badge(skills: list):
#     badges_html = ""
#     for skill in skills:
#         badges_html += f"""
#         <div style='
#             display: inline-block;
#             background-color: rgb(243, 243, 243);
#             color: rgb(101, 101, 101);
#             padding: 6px 14px;
#             border-radius: 9999px;
#             font-size: 13px;
#             font-weight: 500;
#             margin-right: 8px;
#             margin-bottom: 6px;'>{skill}</div>
#         """
#     return badges_html

# # --- Layout: 3 Columns (ซ้าย กลาง ขวา) ---
# empty_c13, col_23= st.columns([8, 2])

# with col_23:
    # st.selectbox(
    #         "Position Applied",
    #         [job["position"] for job in jobs],
    #         index=None,
    #         placeholder="Position Applied",
    #         label_visibility="collapsed"
    #     )

#     st.markdown("<h4 style='color:#1E3A8A; font-size:20px; font-weight:600;'>Applied Process / Activity Updated</h4>", unsafe_allow_html=True)

#     # --- Render Job Cards ---
#     for job in jobs:
#         st.markdown(f"""
#         <div style='
#             background-color: white;
#             color: black;
#             height: 155px;
#             border-radius: 10px;
#             padding: 18px 36px;
#             display: flex;
#             flex-direction: row;
#             align-items: center;
#             justify-content: space-between;
#             box-shadow: 0 2px 6px rgba(0,0,0,0.05);
#             margin-bottom: 20px;'>
#             <div style='flex: 8; display: flex; flex-direction: column; justify-content: space-between; height: 100%;'>
#                 <div style='line-height: 1.6;'>
#                     <div><b>Name:</b> {job["name"]}</div>
#                     <div><b>Position:</b> {job["position"]}</div>
#                 </div>
#                 <div>
#                     <button style='
#                         padding: 6px 18px;
#                         background-color: #E5E7EB;
#                         border: none;
#                         border-radius: 6px;
#                         color: #4B5563;
#                         font-weight: 500;
#                         cursor: pointer;'>View Resume</button>
#                 </div>
#             </div>
#             <div style='flex: 8; display: flex; flex-direction: column; justify-content: space-between; height: 100%;'>
#                 <div>
#                     <b>Skills</b>
#                     <div style='
#                         display: flex;
#                         flex-wrap: wrap;
#                         gap: 8px;
#                         margin-top: 8px;
#                         flex-direction: row;
#                         align-items: center;
#                         '>
#                         {create_skill_badge(job["skills"])}
#         </div>
#         <div style='
#                 display: flex;
#                 flex-direction: row;
#                 align-items: center;
#                 gap: 40px;
#                 margin-top: 10px;'>
#                 <div class='status-info' style='display:flex; align-items:center; gap:8px; cursor:pointer;'>
#                     <div class='status-icon' style='
#                         width: 24px;
#                         height: 24px;
#                         background-color: #22C55E;
#                         color: white;
#                         border-radius: 50%;
#                         display: flex;
#                         align-items: center;
#                         justify-content: center;
#                         font-weight: bold;
#                         font-size:14px;'>✔</div>
#                     <span style='font-weight:500;'>Approve</span>
#         <div class='status-info' style='display:flex; align-items:center; gap:8px; cursor:pointer; padding-left: 55px;'>
#                     <div class='status-icon' style='
#                         width: 24px;
#                         height: 24px;
#                         background-color: #EF4444;
#                         color: white;
#                         border-radius: 50%;
#                         display: flex;
#                         align-items: center;
#                         justify-content: center;
#                         font-weight: bold;
#                         font-size:14px;'>✖</div>
#                     <span style='font-weight:500;'>Reject</span>
#                 </div>
#                 </div>
#         """, unsafe_allow_html=True)


import streamlit as st
import psycopg2

# --- Database update functions ---
def update_postgres(progress_value: int):
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="postgres",
            user="skillpath",
            password="skillpath123",
            port=5432
        )
        cur = conn.cursor()
        cur.execute("UPDATE applied_process SET progress = %s WHERE id = 1;", (progress_value,))
        conn.commit()
        cur.close()
        conn.close()
        st.success(f"✅ Updated progress to {progress_value}")
    except Exception as e:
        st.error(f"Database error: {e}")

# --- Sample job list ---
jobs = [
    {
        "name": "Laura Sullivan",
        "position": "Data Scientist",
        "skills": ['Python', 'Machine Learning', 'SQL', 'Statistics', 'Visualization']
    },
    {
        "name": "Jonathan Lee",
        "position": "Data Engineer",
        "skills": ['Python', 'SQL', 'ETL', 'Docker']
    }
]


with stylable_container(
    key="search_position",
    css_styles=["""
        {
            background: none; 
        }"""]
):
    col1, col2 = st.columns([8,2])
    with col2:
        selected_position = st.selectbox(
            "Position Applied",
            [job["position"] for job in jobs],
            index=None,
            placeholder="Position Applied",
            label_visibility="collapsed"
        )

# --- Function: Skill Badges ---
# def create_skill_badge(skills: list):
#     badges_html = ""
#     for skill in skills:
#         badges_html += f"""
#         <div style='
#             display: inline-block;
#             background-color: rgb(243, 243, 243);
#             color: rgb(101, 101, 101);
#             padding: 6px 14px;
#             border-radius: 9999px;
#             font-size: 13px;
#             font-weight: 500;
#             margin-right: 8px;
#             margin-bottom: 6px;'>{skill}</div>
#         """
#     return badges_html

# # --- Layout ---
# st.title("Applied Process / Activity Updated")

# for i, job in enumerate(jobs):
#     with st.container():
#         st.markdown(f"""
#         <div style='
#             background-color: white;
#             color: black;
#             border-radius: 10px;
#             padding: 18px 36px;
#             box-shadow: 0 2px 6px rgba(0,0,0,0.05);
#             margin-bottom: 20px;'>
#             <div><b>Name:</b> {job["name"]}</div>
#             <div><b>Position:</b> {job["position"]}</div>
#             <div style='margin-top:10px;'><b>Skills</b></div>
#             <div style='display:flex; flex-wrap:wrap; gap:8px; margin-top:8px;'>
#                 {create_skill_badge(job["skills"])}
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#         # --- Action buttons (View Resume / Approve) ---
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("📄 View Resume", key=f"view_{i}"):
#                 update_postgres(3)
#                 st.rerun()

#         with col2:
#             if st.button("✅ Approve", key=f"approve_{i}"):
#                 update_postgres(4)
#                 st.rerun()


def create_skill_badge(skills: list):
    badges_html = ""
    for skill in skills:
        badges_html += f"""
        <div style='
            display: inline-block;
            background-color: #F3F3F3;
            color: #555;
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 13px;
            margin-right: 8px;
            margin-bottom: 6px;
            font-weight: 500;'>
            {skill}
        </div>
        """
    return badges_html


# ---------- Layout ----------

st.markdown("<h4 style='color:#1E3A8A; font-size:35px; font-weight:600;'>Candidate Profile</h4>", unsafe_allow_html=True)

for i, job in enumerate(jobs):
    with stylable_container(
        key=f"search_position{i}",
        css_styles=["""
            {
               background: white !important;
               border-radius: 10px;
               padding: 6px 8px 20px 8px;
               box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            }"""]
    ):
        with st.container():
            # st.markdown("""
            # <style>
            # .st-emotion-cache-18kf3ut {
            #     background: white !important;
            #     border-radius: 10px;
            # }
            # </style>
            # """, unsafe_allow_html=True)
            st.markdown(f"""
            <div style='
                background-color: white;
                padding: 24px 32px;'>
                <div style="display: flex; justify-content: space-between; align-items: flex-start; width: 100%; ">
                    <div style="flex: 1;">
                        <div style="font-size:15px;"><b>Name:</b> {job["name"]}</div>
                        <div style="font-size:15px; margin-top:6px;"><b>Position:</b> {job["position"]}</div>
                    </div>
                    <div style="flex: 1.2; padding-left: 40px;">
                        <b>Skills:</b>
                        <div style="display:flex; align-items: flex-start; margin-top:6px;">
                            {create_skill_badge(job["skills"])}
            """, unsafe_allow_html=True)

            # ------------ buttons functionality -------------
            col_1,col1, col2, col3, col4 = st.columns([0.1,4,0.9,0.9,3])

            # with col1:
            #     if st.button("View Resume", key=f"view_{i}"):
            #         update_postgres(2)
            #         st.rerun()
            with col1:
                with stylable_container(
                    key=f"viewrsm{i}",
                    css_styles="""
                    botton{
                        margin-left:26px;
                    }"""
                ):
                
                    if st.button("View Resume", key=f"view_{i}"):
                        update_postgres(3)
                        st.rerun()
            
            with col2:
                if st.button("✔ Approve", key=f"approve_{i}"):
                    update_postgres(4)
                    st.rerun()

            with col3:
                if st.button("✖ Reject", key=f"reject_{i}"):
                    update_postgres(0)
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------- #
script_footer()