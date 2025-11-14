import streamlit as st
from function.public_function import load_css, load_image

# def navbar():
#     return st.markdown("""
#     <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background: linear-gradient(90deg, rgb(229, 120, 91) 0%, rgb(25, 39, 104) 50%);">
#     <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
#     <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#         <span class="navbar-toggler-icon"></span>
#     </button>
#     <div class="collapse navbar-collapse" id="navbarNav">
#         <ul class="navbar-nav">
#         <li class="nav-item active">
#             <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
#         </li>
#         <li class="nav-item">
#             <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
#         </li>
#         <li class="nav-item">
#             <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
#         </li>
#         </ul>
#     </div>
#     </nav>
#     """, unsafe_allow_html=True)

# def navbar():
#     return st.markdown("""
#     <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background: linear-gradient(90deg, rgb(229, 120, 91) 0%, rgb(25, 39, 104) 50%);">
#     <div style="margin-left: 40px; ">
# 		<img src="data:image/svg+xml;base64,{load_image('src/img/scg_logo.svg')}" width="50"/>
# 	</div>
#     <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#         <p class="navbar-toggler-icon"></p>
#     </button>
#     <div class="collapse navbar-collapse" id="navbarNav">
#         <ul class="navbar-nav">
#         <div style="margin-left: 258px;    margin-top: 6px; margin-bottom: 6px; background-color: rgb(255, 255, 255);padding: 1px 62px 1px 167px; background-color: rgba(255,255,255,100); border-radius: 5px; display: flex;align-items: center;">
# 		<span style="color: black; font-weight: regular; font-size: 16px;">Home</span>
# 	</div>
#     <ul style="display: flex; list-style: none; margin: 0; padding: 0; gap: 10px; justify-content: flex-end;">
#         <li class="nav-item active" style="margin-left: 75px; ">
#             <a class="nav-link disabled"> Home <span class="sr-only">(current)</span></a>
#         </li>
#         <li class="nav-item active">
#             <a class="nav-link disabled"> My Job Applied <span class="sr-only">(current)</span></a>
#         </li>
#         <li class="nav-item active">
#             <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
#         </li>
#         </ul>
#     </ul>
#     </div>
#     </nav>
#     """, unsafe_allow_html=True)


#--------------------------- navbar ที่ใช้ได้ ---------------------------#
# def navbar():
#     return st.markdown(f"""
#         <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background: linear-gradient(90deg, rgb(229, 120, 91) 0%, rgb(25, 39, 104) 50%);">
#         <div class="container-fluid d-flex justify-content-between align-items-center">
#             <div class="navbar-left d-flex align-items-center">
#             <img src="data:image/svg+xml;base64,{load_image('src/img/skillpath.svg')}" alt="Logo" width="90">
#             </div>
#             <div class="navbar-center">
#             <ul class="navbar-nav mx-auto bg-white rounded-pill px-3 py-1 " style="border-radius: 5px; line-height: 1px;">
#                 <li class="nav-item px-3">
#                 <a class="nav-link text-dark font-weight-meduim">Home</a>
#                 </li>
#                 <li class="nav-item px-3">
#                 <a class="nav-link text-dark font-weight-meduim">My Job Applied</a>
#                 </li>
#             </ul>
#             </div>
#             <div class="navbar-right d-flex align-items-center">
#             <a class="nav-link text-white mx-2">For Company</a>
#             <a class="nav-link text-white mx-2">My Profile</a>
#             <img src="data:image/svg+xml;base64,{load_image('src/img/Bell.svg')}" alt="Logo" width="17" style="margin: 6px;">
#             <img src="data:image/svg+xml;base64,{load_image('src/img/bookmark.svg')}" alt="Logo" width="17" style="margin: 6px;">
#             <img src="data:image/svg+xml;base64,{load_image('src/img/letter.svg')}" alt="Logo" width="17" style="margin: 6px;">
#             <img src="data:image/svg+xml;base64,{load_image('src/img/Frame.svg')}" alt="User" width="20" style="margin: 6px;">
#             </div>

#         </div>
#         </nav>
#     """, unsafe_allow_html=True)

def navbar():
    st.markdown(f"""
        <nav class="navbar fixed-top navbar-expand-lg navbar-dark"
            style="background: linear-gradient(90deg, rgb(229, 120, 91) 0%, rgb(25, 39, 104) 50%);
                   padding: 10px 40px;">
            <div class="container-fluid d-flex justify-content-between align-items-center">
                <div class="navbar-left d-flex align-items-center">
                    <img src="data:image/svg+xml;base64,{load_image('src/img/skillpath.svg')}" width="90">
                </div>
                <div class="navbar-center">
                    <ul class="navbar-nav mx-auto bg-white rounded-pill px-3 py-1" style="border-radius: 5px; line-height: 1px;">
                        <li class="nav-item px-3">
                            <a class="nav-link text-dark font-weight-medium" style='text-decoration: none;' target="_self" href="/">Home</a>
                        </li>
                        <li class="nav-item px-3">
                            <a class="nav-link text-dark font-weight-medium" style='text-decoration: none;' target="_self" href="/My_Job_Applied">My Job Applied</a>
                        </li>
                    </ul>
                </div>
                <div class="navbar-right d-flex align-items-center">
                    <a class="nav-link text-white font-weight-medium" style='text-decoration: none;' target="_self" href="/For_Company">For Company</a>
                    <a class="nav-link text-white font-weight-medium" style='text-decoration: none;' target="_self" href="/Student_Profile">My Profile</a>
                    <img src="data:image/svg+xml;base64,{load_image('src/img/Bell.svg')}" width="17" style="margin: 6px;">
                    <img src="data:image/svg+xml;base64,{load_image('src/img/bookmark.svg')}" width="17" style="margin: 6px;">
                    <img src="data:image/svg+xml;base64,{load_image('src/img/letter.svg')}" width="17" style="margin: 6px;">
                    <img src="data:image/svg+xml;base64,{load_image('src/img/Frame.svg')}" width="20" style="margin: 6px;">
                </div>
            </div>
        </nav>
        <br><br><br>
    """, unsafe_allow_html=True)

def script_footer():
    return st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)