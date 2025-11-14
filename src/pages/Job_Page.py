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

recommended_job_config = {
	'scg_figma': {
		'logo': 'src/img/scg_logo.svg',
		'title': 'Data Scientist',
		'company': 'The Siam Cement Public Company Limited (SCG)',
		'location': 'Bangkok',
		'salary': '฿9,500 per month', 
		'description': 'We are looking for Figma designers who can help design the entire mobile application ...',
		'skills': ['Python', 'Machine Learning', 'SQL', 'Statistics', 'Visualization']
	}}
job = {

    'logo': 'src/img/scg_logo.svg',
    'title': 'Data Scientist',
    'company': 'The Siam Cement Public Company Limited (SCG)',
    'location': 'Bangkok',
    'salary': ' 12,000 per month',
    'description': 'Join our UX team to create intuitive and delightful experiences for users ...',
    'skills': ['Python', 'Machine Learning', 'SQL', 'Statistics', 'Visualization']}


empty_c1, col_2, col_3, empty_c4 = st.columns([0.5, 6, 3, 0.5])

# ------------------------------------ Job Detail ----------------------------------- #

# with col_2:
#     st.markdown(f"""
# 		<div class='d-flex flex-column bg-white text-dark' 
# 			style='height: 795px; border-radius: 10px; padding: 15px 36px; margin-bottom: 20px; margin-right: 10px; margin-top: 20px; box-shadow: 0px 4px 8px rgba(0,0,0,0.05);'>
# 			<div class='d-flex flex-row align-items-start' style='flex: 1;'>
#             <div style='margin: 25px 0px;'>
# 					<img src="data:image/svg+xml;base64,{load_image('src/img/image_91.svg')}" style="width: 80%; height: auto;">
# 				</div>
# 				<div style="margin-top: 25px;">
# 					<p style='margin: 0; font-weight: bold; font-size: 20px; color: black; text-decoration: none;'>{job['title']}</p>
# 					<p style='margin: 0;'>{job['company']}</p>
# 					<p style='margin: 5px 0 0 0;'>
# 						<img src="data:image/svg+xml;base64,{load_image("src/img/Location.svg")}" 
# 							width="14" style="vertical-align: middle;"/> {job['location']}
# 					</p>
# 					<p style='margin: 0; color: #333;'>{job['salary']}</p>
# 					<p style='margin: 5px 0 0 0; color: #666; font-size: 14px;'>{job['description']}</p>
# 				</div>        
# 			</div>
# 		</div>
# 		""", unsafe_allow_html=True)

with col_2:
    st.markdown(f"""
		<div class='d-flex flex-column bg-white text-dark' 
			style='height: 795px; border-radius: 10px; padding: 15px 65px; margin-bottom: 20px; margin-right: 10px; margin-top: 20px; box-shadow: 0px 4px 8px rgba(0,0,0,0.05);'>
			<div class='d-flex flex-row align-items-start'>
            <div style='margin: 20px 0px;'>
					<img src="data:image/svg+xml;base64,{load_image('src/img/logo_big.svg')}" style="width: 80%; height: auto;">
				</div>
				<div style="margin-top: 25px;">
					<p style='margin: 0; font-weight: bold; font-size: 20px; color: black; text-decoration: none;'>{job['title']}</p>
					<p style='margin: 0;'>{job['company']}</p>
					<p style='margin: 1px; margin-top: 5px; font-size: 15px;'>
						<img src="data:image/svg+xml;base64,{load_image("src/img/Location.svg")}" 
							width="18" style="vertical-align: middle; "/> Bangkok
					</p>
                    <p style='margin: 1px; font-size: 15px;'>
						<img src="data:image/svg+xml;base64,{load_image("src/img/PermanentJob.svg")}" 
							width="18" style="vertical-align: middle;"/> IT
					</p>
                    <p style='margin: 1px; font-size: 15px;'>
						<img src="data:image/svg+xml;base64,{load_image("src/img/Clock.svg")}" 
							width="18" style="vertical-align: middle;"/> Internship (Full-Time)
					</p>
					<p style='margin: 1; font-size: 15px;'>
                        <img src="data:image/svg+xml;base64,{load_image("src/img/Stack_of_Money.svg")}" 
							width="18" style="vertical-align: middle;"/> 9,500 per month</p>
				</div>       
			</div>
            <div style='display: flex; gap: 10px; margin-top: 5px;'>
            <a href="/Apply_Job" target="_self"
                style='
                    background-color: #E5795B;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 8px 65px;
                    font-weight: 500;
                    cursor: pointer;
                    text-decoration: none;
                '>Apply</a>
                <button style='
                    background-color: #E4E7F0;
                    color: #192768;
                    border: none;
                    border-radius: 5px;
                    padding: 8px 65px;
                    font-weight: 500;
                    cursor: pointer;
                '>Favorite</button>
            </div>
            <hr style='border: none; border-top: 1px solid #ccc; margin: 25px 0px;'>
            <div style='padding: 24px 36px; flex: 1; overflow-y: auto;'>
            <p style='font-weight: 700; font-size: 17px; margin-bottom: 6px;'>Job Responsibilities:</p>
            <p style='font-size: 15px; color: #555; line-height: 1.6;'>
            We are looking for Data Scientists who can help analyze data and drive data-driven decision-making.<br>
            • Data Analysis & Modeling – Collecting, cleaning, and analyzing data to extract actionable insights.<br>
            • Developing Predictive Models – Building machine learning models to support business objectives.<br>
            • Collaborating with Teams – Working closely with product managers, engineers, and stakeholders to define requirements and deliver solutions.<br>
            • Data Visualization & Reporting – Creating dashboards and reports to communicate findings effectively.<br>
            <p style='font-weight: 700; font-size: 17px; margin-top: 24px; margin-bottom: 6px;'>Requirements:</p>
            <p style='font-size: 15px; color: #555; line-height: 1.6;'>
            • Fluent in English<br>
            • Excellent at communication and teamwork<br>
            • Passionate about solving problems<br>
            • Proactive and self-motivated<br>
            • Able to manage multiple priorities<br>
        </p>
        </p>
        </div>
		</div>
		""", unsafe_allow_html=True)



# --------------------------- Skill Match & Company -------------------------- #
# with col_3:
#     st.markdown(f"""
# 		<div class='d-flex flex-row bg-white text-dark' 
# 			style='height: 300px; border-radius: 10px; padding-top: 20px; padding-bottom: 40px; margin-bottom: 15px; margin-left: 15px; margin-right: 15px; margin-top: 20px;'>
# 			<div class='d-flex flex-row align-items-center' style='flex: 1;'>
# 			</div>
# 		</div>
#         <div class='d-flex flex-row bg-white text-dark' 
# 			style='height: 490px; border-radius: 10px; padding-top: 20px; padding-bottom: 40px; margin-bottom: 15px; margin-left: 15px; margin-right: 15px; '>
# 			<div class='d-flex flex-row align-items-center' style='flex: 1;'>
# 			</div>
# 		</div>
# 		""", unsafe_allow_html=True)

def create_skill_badge(skills: list):
    badges_html = ""
    for skill in skills:
        badges_html += f"""
        <div style='
            display: inline-block;
            background-color: rgb(219, 222, 229);
            color: rgb(101, 101, 101);
            padding: 6px 14px;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 500;
            overflow: auto;
            margin: 0;'>{skill}</div>
        """
    return badges_html  # คืนค่า HTML เป็น string


with col_3:
    for key, job in recommended_job_config.items():
        if key == list(recommended_job_config.keys())[0]:
            st.markdown(f"""
                <div style='
                    background-color: white;
                    border-radius: 12px;
                    padding: 24px;
                    box-shadow: 0px 4px 8px rgba(0,0,0,0.05);
                    margin: 20px 15px;
                '>
                    <div style='font-weight: 700; font-size: 18px; color: black; margin-top: 5px; margin-bottom: 10px;'>
                        Skill Matching
                    </div>
                    <div style='
                        width: 100%;
                        height: 1px;
                        background-color: #bbb;
                        margin-top: 3px;
                        margin-bottom: 20px;
                    '></div>
                    <div style='
                        display: flex;
                        flex-direction: column;
                        gap: 10px;
                        justify-content: flex-start;
                        align-items: stretch;
                    '>
                        {create_skill_badge(job['skills'])}
                """, unsafe_allow_html=True)
            # st.markdown(f"""
            #     <div class='d-flex flex-row bg-white text-dark' 
            #         style='height: 300px; border-radius: 10px; padding-top: 20px; padding-bottom: 40px; margin-bottom: 15px; margin-left: 15px; margin-right: 15px; margin-top: 20px;'>
            #         <div class='d-flex flex-row align-items-center' style='flex: 0.5;'></div>
            #         <div style='
            #             display: flex; flex-flow: column wrap; gap: 10px; justify-content: flex-start; align-items: stretch; overflow: auto; padding-top: 8px; flex-wrap: nowrap; flex-direction: column;'>
            #             {create_skill_badge(job['skills'])}
            #         </div>
            #     </div>
            #     """, unsafe_allow_html=True)
    # st.markdown(f"""
    #             <div class='d-flex flex-row bg-white text-dark' 
    #                 style='height: 490px; border-radius: 10px; padding-top: 20px; padding-bottom: 40px; margin-bottom: 15px; margin-left: 15px; margin-right: 15px; box-shadow: 0px 4px 8px rgba(0,0,0,0.05);'>
    #                 <div class='d-flex flex-row align-items-center' style='flex: 1;'>
    #                 </div>
    #             </div>
    #             """, unsafe_allow_html=True)
    st.markdown(f"""
                <div style='
                    background-color: white;
                    border-radius: 16px;
                    overflow: hidden;
                    width: 440px;
                    height: 490px;
                    margin-left: 15px;
                    height: 490px;
                    box-shadow: 0px 4px 8px rgba(0,0,0,0.05);
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: flex-start;
                '>
                    <div style="
                        background-size: cover;
                        background-position: center;
                        height: 50%;
                        width: 100%;
                        position: relative;
                    ">
                    <img src="data:image/svg+xml;base64,{load_image('src/img/image_90.svg')}"
                                style="width: 100%; height: auto;">
                        <div style="
                            position: absolute;
                            bottom: -60px;
                            left: 50%;
                            transform: translateX(-50%);
                            width: 105px;
                            height: 100px;
                            background-color: white;
                            border: 0.5px solid #ddd;
                            border-radius: 8px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        ">
                            <img src="data:image/svg+xml;base64,{load_image('src/img/image_91.svg')}"
                                style="width: 100%; height: auto;">
                        </div>
                    </div>
                    <div style='
                        flex: 1;
                        padding-top: 70px;
                        padding-left: 25px;
                        padding-right: 25px;
                        padding-bottom: 25px;
                        text-align: center;
                    '>
                        <div style='font-weight: 700; font-size: 18px; margin-bottom: 4px;'>
                            The Siam Cement Public Company Limited
                        </div>
                        <div style='color: #777; font-size: 13px; margin-bottom: 16px;'>
                            1 Siam Cement Road, Bangsue, Bangkok 10800
                        </div>
                        <div style='font-size: 14px; color: #555; line-height: 1.5;'>
                            SCG restructured its business groups with an Agile Organization model,
                            fostering new businesses with high growth potential aligning with global
                            trends and business conditions. This adjustment enables SCG to quickly
                            adapt to ever-changing customer demands.
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)     



# ---------------------------------------------------------------------------- #
script_footer()