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


job = {

    'logo': 'src/img/scg_logo.svg',
    'title': 'Figma Designer',
    'company': 'The Siam Cement Public Company Limited (SCG)',
    'location': 'Bangkok',
    'salary': ' 12,000 per month',
    'description': 'Join our UX team to create intuitive and delightful experiences for users ...',
    'skills': ['Ui Designer', 'Figma', 'Landing Page', 'User Research']}


# empty_c1, col_2, empty_c3 = st.columns([0.5, 9, 0.5])

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
# 			style='height: 155px; border-radius: 10px; padding: 140px 36px; margin-bottom: 20px;'>
# 			<div class='d-flex flex-row align-items-center' style='flex: 1;'>
# 			</div>
# 		</div>
# 		""", unsafe_allow_html=True)


# with col_2:
#     st.markdown("""
#     <style>
#     .stSelectbox {
#         width: 300px !important;
#         margin-left: auto;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     option = st.selectbox(
#         "How would you like to be contacted?",
#         ("Figma Designer", "UX/UI Designer"),
#         index=None,
#         placeholder="Position Applied",
#         label_visibility="collapsed"
#     )

#     st.markdown("<h4 style='color:#1E3A8A; font-size:20px; font-weight:600;'>Applied Process/ Activity Updated</h4>", unsafe_allow_html=True)

#     st.markdown("""
#     <style>
#     .card-container {
#         background-color: white;
#         border-radius: 10px;
#         box-shadow: 0px 2px 4px rgba(0,0,0,0.1);
#         padding: 24px 36px;
#         margin-bottom: 20px;
#     }

#     .progress-bar {
#         display: flex;
#         flex-direction: row;
#         align-items: center;
#         justify-content: space-between;
#         background: linear-gradient(to right, #FFBFAE 40%, #192768 60%);
#         height: 32px;
#         border-radius: 20px;
#         padding: 0 16px;
#         margin-bottom: 24px;
#     }

#     .progress-step {
#         width: 23px;
#         height: 23px;
#         border-radius: 50%;
#         background-color: #E5E7EB;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#     }

#     .progress-step.active {
#         background-color: #E5785B;
#     }

#     .progress-labels {
#         display: flex;
#         justify-content: space-between;
#         margin-top: 8px;
#         font-weight: 600;
#         font-size: 13px;
#     }

#     .job-info {
#         margin-top: 24px;
#     }

#     .job-title {
#         font-weight: 700;
#         text-decoration: underline;
#         font-size: 16px;
#         margin-bottom: 6px;
#     }

#     .company-info {
#         color: #6B7280;
#         font-size: 13px;
#         margin-bottom: 4px;
#     }

#     .status-info {
#         display: flex;
#         align-items: center;
#         gap: 8px;
#         font-size: 13px;
#     }

#     .status-icon {
#         width: 20px;
#         height: 20px;
#         background-color: #22C55E;
#         color: white;
#         border-radius: 50%;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         font-weight: bold;
#     }
#     </style>

#     <div class="card-container">
#         <div class="progress-bar">
#             <div class="progress-step active"></div>
#             <div class="progress-step active"></div>
#             <div class="progress-step"></div>
#             <div class="progress-step"></div>
#         </div>
#         <div class="progress-labels">
#             <span>Sent Resume</span>
#             <span>Read by HR</span>
#             <span>Interview Appointment</span>
#             <span>Interview Results</span>
#         </div>
#         <div class="job-info">
#             <div class="job-title">Figma Designer</div>
#             <div class="company-info">The Siam Cement Public Company Limited (SCG.)</div>
#             <div class="company-info">📍 Bangkok</div>
#             <div class="status-info">
#                 <div class="status-icon">✔</div>
#                 <div>
#                     <div>Read by HR</div>
#                     <div>Date: Sep 20, 2025</div>
#                 </div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


jobs = [
    {
        "position": "Figma Designer",
        "company": "The Siam Cement Public Company Limited (SCG.)",
        "location": "Bangkok",
        "status": "Read by HR",
        "date": "Sep 20, 2025",
        "progress": 2  # 1=Sent Resume, 2=Read by HR, 3=Interview Appointment, 4=Interview Results
    },
    {
        "position": "UX/UI Designer",
        "company": "The Siam Cement Public Company Limited (SCG.)",
        "location": "Bangkok",
        "status": "Sent Resume",
        "date": "Sep 20, 2025",
        "progress": 1
    }
]

# --- CSS ---
st.markdown("""
<style>
.stSelectbox {
    width: 300px !important;
	margin-left: auto;
}

h4 {
    color: #1E3A8A;
    font-size: 20px;
    font-weight: 600;
}

.card {
    background-color: #fff;
    border-radius: 10px;
    padding: 24px 32px;
    margin-bottom: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.progress-bar {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(to right, #FFBFAE 40%, #192768 60%);
    height: 32px;
    border-radius: 20px;
    padding: 0 16px;
    margin-bottom: 10px;
}

.progress-step {
    width: 23px;
    height: 23px;
    border-radius: 50%;
    background-color: #E5E7EB;
    display: flex;
    align-items: center;
    justify-content: center;
}

.progress-step.active {
    background-color: #E5785B;
}

.progress-labels {
    display: flex;
    justify-content: space-between;
    margin-top: 8px;
    font-weight: 700;
    font-size: 15px;
}

.job-title {
    font-size: 16px;
    font-weight: 700;
    text-decoration: underline;
    margin-bottom: 4px;
}

.company {
    color: gray;
    font-size: 14px;
    margin-bottom: 2px;
}

.location {
    font-size: 13px;
    color: #555;
}

.status {
    color: #16A34A;
    font-weight: 600;
    margin-top: 8px;
    font-size: 14px;
}

.date {
    color: #444;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
empty_c1, col2, empty_c3 = st.columns([0.5, 9, 0.5])


with col2:
	st.selectbox(
		"Position Applied",
		[job["position"] for job in jobs],
		index=None,
		placeholder="Position Applied",
		label_visibility="collapsed"
	)

	st.markdown("<h4>Applied Process</h4>", unsafe_allow_html=True)
	# --- For Loop: Render Each Job Card ---
	for job in jobs:
		# ✅ เพิ่มส่วนนี้
		if job["progress"] == 1:
			gradient = "linear-gradient(to right, #E5785B 0%, #FBC4B0 20%, #2E367D 30%, #2E367D 100%)"
		elif job["progress"] == 2:
			gradient = "linear-gradient(to right, #E5785B 0%, #FBC4B0 40%, #2E367D 50%, #2E367D 100%)"
		elif job["progress"] == 3:
			gradient = "linear-gradient(to right, #E5785B 0%, #FBC4B0 65%, #2E367D 75%, #2E367D 100%)"
		elif job["progress"] == 4:
			gradient = "linear-gradient(to right, #E5785B 0%, #FBC4B0 100%)"
		else:
			gradient = "linear-gradient(to right, #2E367D 100%)"

		# ไล่สีจากส้ม -> น้ำเงิน (gradient dynamic)
		# gradient = f"linear-gradient(to right, #E5785B {filled}, #1E3A8A {filled})"

		html = f"""
		<div class="card">
			<div class="progress-bar" style="background: {gradient};">
				<div class="progress-step {'active' if job['progress'] >= 1 else ''}"></div>
				<div class="progress-step {'active' if job['progress'] >= 2 else ''}"></div>
				<div class="progress-step {'active' if job['progress'] >= 3 else ''}"></div>
				<div class="progress-step {'active' if job['progress'] >= 4 else ''}"></div>
			</div>
			<div class="progress-labels">
				<p>Sent Resume</p>
				<p>Read by HR</p>
				<p>Interview Appointment</p>
				<p>Interview Results</p>
			</div>
			<div style="margin-top: 16px;">
				<div class="job-title">{job['position']}</div>
				<div class="company">{job['company']}</div>
				<div class="location">📍 {job['location']}</div>
				<div class="status">✅ {job['status']}</div>
				<div class="date">Date: {job['date']}</div>
			</div>
		</div>
		"""
		st.markdown(html, unsafe_allow_html=True)


# ---------------------------------------------------------------------------- #
script_footer()