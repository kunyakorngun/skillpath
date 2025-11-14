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

# ------------------------------------ Job Apply ----------------------------------- #

# with col_2:
#     st.markdown("<h4 style='color:#1E3A8A; font-size:35px; font-weight:600;'>Apply Job</h4>", unsafe_allow_html=True)
#     st.markdown(f"""
# 		<div class='d-flex flex-column bg-white text-dark' 
# 			style='height: 1000px; border-radius: 10px; padding: 15px 36px; margin-bottom: 20px; margin-right: 10px; margin-top: 20px; box-shadow: 0px 4px 8px rgba(0,0,0,0.05);'>
# 		<div style='display: flex; align-items: center; gap: 16px;'>
# 					<img src="data:image/svg+xml;base64,{load_image('src/img/image_5.svg')}" style="width: 60px; height: 60px;">
# 					<div style='display:flex; flex-direction:column;'>
# 						<span style='font-size:18px; font-weight:600;'>Laura Sullivan</span>
# 						<a href='mailto:Laura.Sullivan@gmail.com' style='font-size:14px; color:#1E3A8A; text-decoration:none;'>Laura.Sullivan@gmail.com</a>
# 					</div>
#         </div>
# 		""", unsafe_allow_html=True)



# with col_2:
#     st.markdown("<h4 style='color:#1E3A8A; font-size:35px; font-weight:600;'>Apply Job</h4>", unsafe_allow_html=True)
#     st.markdown(f"""
#     <div style='
#         background-color: white;
#         color: #111827;
#         border-radius: 10px;
#         padding: 25px 36px;
#         margin-top: 20px;
#         margin-bottom: 20px;
#         box-shadow: 0px 4px 8px rgba(0,0,0,0.05);
#         font-family: "Segoe UI", sans-serif;
#         height: 1050px;'>
#         <div style='display: flex; align-items: center; gap: 16px;'>
#             <img src="data:image/svg+xml;base64,{load_image('src/img/image_91.svg')}" style="width: 60px; height: 60px;">
#             <div style='display:flex; flex-direction:column;'>
#                 <span style='font-size:18px; font-weight:600;'>Data Scientist</span>
#                 <span style='font-size:13px; color:#6B7280;'>The Siam Cement Public Company Limited (SCG.)</span>
#             </div>
#         </div>
#         <div style='background-color:#F3F4F6; border-radius:4px; margin-top:20px;'>
#             <div style='background-color:#D1D5DB; font-weight:600; padding:6px 10px; border-radius:4px 4px 0 0;'>PERSONAL INFORMATION</div>
#             <div style='padding:15px 20px; background-color:white; border-radius:0 0 4px 4px;'>
#                 <div style='display:flex; justify-content:space-between; align-items:center;'>
#                     <div></div>
#                     <div style='display:flex; align-items:center; gap:6px;'>
#                         <label class="switch">
#                             <input type="checkbox" check>
#                             <span class="slider round"></span>
#                         </label>
#                         <label style='font-size:13px;'>Use old data</label>
#                     </div>
#                 </div>
#                 <div style='display:grid; grid-template-columns: repeat(3, 1fr); gap:10px; margin-top:10px; font-size:13px; align-items: end;'>
#                     <div>First Name: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>Last Name: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>Age:</br><input type='text' style='width:40%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>Email:</br><input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>Phone Number: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>Year of Study:</br><input type='text' style='width:40%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>University: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>Degree’s: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>GPAX:</br><input type='text' style='width:40%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>Faculty: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
#                     <div>Major:</br><input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div> 
#                     <div></div>
#                 </div>
#             </div>
#         </div>
#         <div style='background-color:#F3F4F6; border-radius:4px; margin-top:25px;'>
#             <div style='background-color:#D1D5DB; font-weight:600; padding:6px 10px; border-radius:4px 4px 0 0;'>MORE INFORMATION</div>
#             <div style='padding:15px 20px; background-color:white; border-radius:0 0 4px 4px;'>
#                 <div style='display:flex; justify-content:space-between; align-items:center;'>
#                     <div></div>
#                     <div style='display:flex; align-items:center; gap:6px;'>
#                         <label class="switch">
#                             <input type="checkbox" check>
#                             <span class="slider round"></span>
#                         </label>
#                         <label style='font-size:13px;'>Use old data</label>
#                     </div>
#                 </div>
#                 <div style='display:flex; flex-direction:column; gap:10px; margin-top:10px;'>
#                     <button style='display:flex; justify-content:space-between; align-items:center; width:100%; background-color:#fff; border:1px solid #9CA3AF; border-radius:4px; padding:8px 12px; font-weight:500;'>EXPERIENCES <span>+</span></button>
#                     <button style='display:flex; justify-content:space-between; align-items:center; width:100%; background-color:#fff; border:1px solid #9CA3AF; border-radius:4px; padding:8px 12px; font-weight:500;'>SKILLS <span>+</span></button>
#                     <button style='display:flex; justify-content:space-between; align-items:center; width:100%; background-color:#fff; border:1px solid #9CA3AF; border-radius:4px; padding:8px 12px; font-weight:500;'>LANGUAGE <span>+</span></button>
#                     <button style='display:flex; justify-content:space-between; align-items:center; width:100%; background-color:#fff; border:1px solid #9CA3AF; border-radius:4px; padding:8px 12px; font-weight:500;'>CERTIFICATE <span>+</span></button>
#                 </div>
#             <div>
#             <div style='font-family: Arial, sans-serif;'>
#                 <div style='display:flex; flex-direction:row; gap:40px;'>
#                     <div style='flex:1; display:flex; flex-direction:column;'>
#                         <label style='font-weight:500; padding-top:15px;'>Resume <span style="color:red;">*</span></label>
#                         <div style='display:flex; flex-direction:row; align-items:center; gap:12px;'>
#                             <input type='text' value='' style='
#                                 flex:1; 
#                                 padding:8px; 
#                                 border-radius:4px; 
#                                 border:1px solid #D1D5DB; 
#                                 background-color:#FFFFFF;
#                                 font-size:14px;'>
#                             <button style='
#                                 background-color:#1E3A8A; 
#                                 color:white; 
#                                 border:none; 
#                                 border-radius:4px; 
#                                 padding:8px 16px; 
#                                 font-weight:600; 
#                                 cursor:pointer;'>+ Add file</button>
#                         </div>
#                     </div>
#                     <div style='flex:1; display:flex; flex-direction:column;'>
#                         <label style='font-weight:500; padding-top:15px;'>Transcript <span style="color:red;">*</span></label>
#                         <div style='display:flex; flex-direction:row; align-items:center; gap:12px;'>
#                             <input type='text' value='' style='
#                                 flex:1; 
#                                 padding:8px; 
#                                 border-radius:4px; 
#                                 border:1px solid #D1D5DB; 
#                                 background-color:#FFFFFF;
#                                 font-size:14px;'>
#                             <button style='
#                                 background-color:#1E3A8A; 
#                                 color:white; 
#                                 border:none; 
#                                 border-radius:4px; 
#                                 padding:8px 16px; 
#                                 font-weight:600; 
#                                 cursor:pointer;'>+ Add file</button>
#                         </div>
#                     </div>
#                 </div>
#                 <div>
#             <div style='font-family: Arial, sans-serif;'>
#                 <div style='display:flex; flex-direction:row; gap:40px;'>
#                     <div style='flex:1; display:flex; flex-direction:column;'>
#                         <label style='font-weight:500; padding-top:15px;'>Resume <span style="color:red;">*</span></label>
#                         <div style='display:flex; flex-direction:row; align-items:center; gap:12px;'>
#                             <input type='text' value='' style='
#                                 flex:1; 
#                                 padding:8px; 
#                                 border-radius:4px; 
#                                 border:1px solid #D1D5DB; 
#                                 background-color:#FFFFFF;
#                                 font-size:14px;'>
#                             <button style='
#                                 background-color:#1E3A8A; 
#                                 color:white; 
#                                 border:none; 
#                                 border-radius:4px; 
#                                 padding:8px 16px; 
#                                 font-weight:600; 
#                                 cursor:pointer;'>+ Add file</button>
#                         </div>
#                     </div>
#                     <div style='flex:1; display:flex; flex-direction:column;'>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         <div style='display:flex; justify-content:space-between; align-items:center; margin-top: 61px;'>
#             <a href='#' style='font-size:13px; color:#1E3A8A; text-decoration:none;'></a>
#             <a href="/My_Job_Applied" target="_self"
#             style='background-color:#EA6B4B; color:white; border:none; border-radius:6px;
#                     padding:8px 31px; font-weight:600; cursor:pointer; text-decoration:none;
#                     display:inline-block;'>
#             Apply
#             </a>
#         </div>
#     </div>
#     <style>
#     .switch {{
#       position: relative;
#       display: inline-block;
#       width: 38px;
#       height: 20px;
#     }}
#     .switch input {{opacity: 0; width: 0; height: 0;}}
#     .slider {{
#       position: absolute;
#       cursor: pointer;
#       top: 0; left: 0; right: 0; bottom: 0;
#       background-color: #ccc;
#       transition: .3s;
#       border-radius: 34px;
#     }}
#     .slider:before {{
#       position: absolute;
#       content: "";
#       height: 14px; width: 14px;
#       left: 3px; bottom: 3px;
#       background-color: white;
#       transition: .3s;
#       border-radius: 50%;
#     }}
#     input:checked + .slider {{
#       background-color: #EA6B4B;
#     }}
#     input:checked + .slider:before {{
#       transform: translateX(18px);
#     }}
#     </style>
#     """, unsafe_allow_html=True)


import streamlit as st
import psycopg2
from function.public_function import load_css, load_image
from widget.widget import navbar, script_footer

# --------------------------------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------------------------------
st.set_page_config(layout="wide")
load_css("src/style/hide_header.css")
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" '
    'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True
)
navbar()

# --------------------------------------------------------------------------------
# FUNCTION: Update PostgreSQL
# --------------------------------------------------------------------------------
def update_postgres(progress_value: int):
    """อัปเดตค่า progress ในฐานข้อมูล"""
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
        # หลังอัปเดตสำเร็จ ให้ redirect ไปหน้า My_Job_Applied
        st.markdown('<meta http-equiv="refresh" content="0; url=/My_Job_Applied" />', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Database error: {e}")

# --------------------------------------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------------------------------------
empty_c1, col_2, empty_c3 = st.columns([0.5, 9, 0.5])

with col_2:
    st.markdown("<h4 style='color:#1E3A8A; font-size:35px; font-weight:600;'>Apply Job</h4>", unsafe_allow_html=True)
    
    
    with st.container(border=True):
        st.markdown(f"""
        <div style='background-color: white;'>
            <div style='display: flex; align-items: center; gap: 16px;'>
                <img src="data:image/svg+xml;base64,{load_image('src/img/image_91.svg')}" style="width: 60px; height: 60px;">
                <div style='display:flex; flex-direction:column;'>
                    <span style='font-size:18px; font-weight:600;'>Data Scientist</span>
                    <span style='font-size:13px; color:#6B7280;'>The Siam Cement Public Company Limited (SCG.)</span>
                </div>
            </div>
            <div style='background-color:#F3F4F6; border-radius:4px; margin-top:20px;'>
                <div style='background-color:#D1D5DB; font-weight:600; padding:6px 10px; border-radius:4px 4px 0 0;'>
                    PERSONAL INFORMATION
                </div>
                <div style='padding:15px 20px; background-color:white; border-radius:0 0 4px 4px;'>
                    <div style='display:flex; justify-content:space-between; align-items:center;'>
                        <div></div>
                        <div style='display:flex; align-items:center; gap:6px;'>
                            <label class="switch">
                                <input type="checkbox" checked>
                                <span class="slider round"></span>
                            </label>
                            <label style='font-size:13px;'>Use old data</label>
                        </div>
                    </div>
                    <div style='display:grid; grid-template-columns: repeat(3, 1fr); gap:10px; margin-top:10px; font-size:13px; align-items: end;'>
                        <div>First Name: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>Last Name: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>Age:</br><input type='text' style='width:40%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>Email:</br><input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>Phone Number: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>Year of Study:</br><input type='text' style='width:40%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>University: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>Degree’s: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>GPAX:</br><input type='text' style='width:40%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>Faculty: <input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div>
                        <div>Major:</br><input type='text' style='width:90%; border:none; border-bottom:1px solid #9CA3AF;'></div> 
                        <div></div>
                    </div>
                </div>
            </div>
            <div style='background-color:#F3F4F6; border-radius:4px; margin-top:25px;'>
                <div style='background-color:#D1D5DB; font-weight:600; padding:6px 10px; border-radius:4px 4px 0 0;'>MORE INFORMATION</div>
                <div style='padding:15px 20px; background-color:white; border-radius:0 0 4px 4px;'>
                    <div style='display:flex; justify-content:space-between; align-items:center;'>
                        <div></div>
                        <div style='display:flex; align-items:center; gap:6px;'>
                            <label class="switch">
                                <input type="checkbox" checked>
                                <span class="slider round"></span>
                            </label>
                            <label style='font-size:13px;'>Use old data</label>
                        </div>
                    </div>
                    <div style='display:flex; flex-direction:column; gap:10px; margin-top:10px;'>
                        <button style='display:flex; justify-content:space-between; align-items:center; width:100%; background-color:#fff; border:1px solid #9CA3AF; border-radius:4px; padding:8px 12px; font-weight:500;'>EXPERIENCES <span>+</span></button>
                        <button style='display:flex; justify-content:space-between; align-items:center; width:100%; background-color:#fff; border:1px solid #9CA3AF; border-radius:4px; padding:8px 12px; font-weight:500;'>SKILLS <span>+</span></button>
                        <button style='display:flex; justify-content:space-between; align-items:center; width:100%; background-color:#fff; border:1px solid #9CA3AF; border-radius:4px; padding:8px 12px; font-weight:500;'>LANGUAGE <span>+</span></button>
                        <button style='display:flex; justify-content:space-between; align-items:center; width:100%; background-color:#fff; border:1px solid #9CA3AF; border-radius:4px; padding:8px 12px; font-weight:500;'>CERTIFICATE <span>+</span></button>
                    </div>
                    <div style='display:flex; flex-direction:row; gap:40px; margin-top:20px;'>
                        <div style='flex:1; display:flex; flex-direction:column;'>
                            <label style='font-weight:500; padding-top:15px;'>Resume <span style="color:red;">*</span></label>
                            <div style='display:flex; flex-direction:row; align-items:center; gap:12px;'>
                                <input type='text' style='flex:1; padding:8px; border-radius:4px; border:1px solid #D1D5DB; background-color:#FFFFFF; font-size:14px;'>
                                <button style='background-color:#1E3A8A; color:white; border:none; border-radius:4px; padding:8px 16px; font-weight:600; cursor:pointer;'>+ Add file</button>
                            </div>
                        </div>
                        <div style='flex:1; display:flex; flex-direction:column;'>
                            <label style='font-weight:500; padding-top:15px;'>Transcript <span style="color:red;">*</span></label>
                            <div style='display:flex; flex-direction:row; align-items:center; gap:12px;'>
                                <input type='text' style='flex:1; padding:8px; border-radius:4px; border:1px solid #D1D5DB; background-color:#FFFFFF; font-size:14px;'>
                                <button style='background-color:#1E3A8A; color:white; border:none; border-radius:4px; padding:8px 16px; font-weight:600; cursor:pointer;'>+ Add file</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # --------------------------------------------------------------------------------
        # Apply Button (กดแล้วอัปเดต progress = 2 และ redirect)
        # --------------------------------------------------------------------------------
        empty_c3, col_6, col_4, col_5= st.columns([3.9, 5, 1, 0.1])
        with col_4:
            with stylable_container(
                key="apply_btn",
                css_styles="""
                botton{
                    background-color: #e5785b;
                    color: white;
                    border: none;
                    border-radius: 3px;
                }"""
            ):
                if st.button("Apply", key="apply_btn", width="stretch"):
                    update_postgres(2)
                st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------------------------------------
script_footer()

