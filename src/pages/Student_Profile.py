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

empty_c1, col_2, empty_c3 = st.columns([0.5, 9, 0.5])

with col_2:
    st.markdown("<h4 style='color:#1E3A8A; font-size:35px; font-weight:600;'>This is your personal space</h4>", unsafe_allow_html=True)
    st.markdown(f"""
		<div style='
			background-color: white;
			color: #111827;
			border-radius: 10px;
			padding: 25px 36px;
			margin-top: 15px;
			box-shadow: 0 4px 8px rgba(0,0,0,0.05);
			display: flex;
			flex-direction: column;
			gap: 20px;
			width: 100%;
   			height: 950px;'>
			<div style='display: flex; justify-content: space-between; align-items: flex-start;'>
				<div style='display: flex; align-items: center; gap: 16px;'>
					<img src="data:image/svg+xml;base64,{load_image('src/img/image_5.svg')}" style="width: 60px; height: 60px; border-radius: 50%;">
					<div style='display:flex; flex-direction:column;'>
						<span style='font-size:18px; font-weight:600;'>Laura Sullivan</span>
						<a href='mailto:Laura.Sullivan@gmail.com' style='font-size:14px; color:#1E3A8A; text-decoration:none;'>Laura.Sullivan@gmail.com</a>
					</div>
				</div>
				<button style='
					background-color: #EA6B4B;
					color: white;
					border: none;
					border-radius: 6px;
					padding: 8px 20px;
					font-weight: 600;
					cursor: pointer;'>Edit</button>
			</div>
			<div style='display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px;'>
				<div>
					<label style='font-weight:500;'>Full Name</label>
					<input type='text' value='Laura Sullivan' style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
				</div>
				<div>
					<label style='font-weight:500;'>Skill</label>
					<input type='text' value='Python,   Machine Learning,   SQL,   Statistics,   Visualization' style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
				</div>
				<div>
					<label style='font-weight:500;'>Age</label>
					<input type='text' value='21' style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
				</div>
				<div>
					<label style='font-weight:500;'>Phone</label>
					<input type='text' placeholder='xxx xxx xxxx' style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
				</div>
				<div>
					<label style='font-weight:500;'>Address</label>
					<input type='text' placeholder='Your Address' style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
				</div>
				<div>
					<label style='font-weight:500;'>Internship period</label>
					<input type='text' placeholder='XX-XX-XXXX  -  XX-XX-XXXX' style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
				</div>
				<div>
					<label style='font-weight:500;'>Education</label>
					<select style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
						<option>University</option>
					</select>
					<select style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB; margin-top:8px;'>
						<option>Faculty</option>
					</select>
					<select style='width:100%; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB; margin-top:8px;'>
						<option>Major</option>
					</select>
				<div>
					<label style='font-weight:500; padding-top:15px;'>Resume</label>
					<div style='display:flex; flex-direction:row; align-items:center; gap:12px;'>
						<input type='text' value='laura_resume.pdf' style='flex:1; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
						<button style='
							background-color:#EA6B4B;
							color:white;
							border:none;
							border-radius:6px;
							padding:10px 16px;
							font-weight:600;
							cursor:pointer;'>Upload your files</button>
					</div>
					<label style='font-weight:500; padding-top:15px;'>Transcript</label>
					<div style='display:flex; flex-direction:row; align-items:center; gap:12px;'>
						<input type='text' value='laura_Transcript.pdf' style='flex:1; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
						<button style='
							background-color:#EA6B4B;
							color:white;
							border:none;
							border-radius:6px;
							padding:10px 16px;
							font-weight:600;
							cursor:pointer;'>Upload your files</button>
					</div>
					<label style='font-weight:500; padding-top:15px;'>Certificate</label>
					<div style='display:flex; flex-direction:row; align-items:center; gap:12px;'>
						<input type='text' value='laura_Certificate.pdf' style='flex:1; padding:10px; border-radius:6px; border:1px solid #E5E7EB; background-color:#F9FAFB;'>
						<button style='
							background-color:#EA6B4B;
							color:white;
							border:none;
							border-radius:6px;
							padding:10px 16px;
							font-weight:600;
							cursor:pointer;'>Upload your files</button>
					</div>
				</div>
			</div>
		</div>
		""", unsafe_allow_html=True)

		
		

# ---------------------------------------------------------------------------- #
script_footer()