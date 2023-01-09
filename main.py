import json
import streamlit as st


st.set_page_config("App Demo", "🚀", "wide", "expanded")

options = ["Text to Speech", "Speech to Text", "Video Demo"]
st_options = st.sidebar.selectbox("Select options", options)

if st_options == "Text to Speech":
    st.markdown("<h1 style='text-align: center; color: white;'>Text to Speech</h1>", unsafe_allow_html=True)
    file_upload = st.sidebar.file_uploader("Upload text file", type=["txt"])
    btn_submit = st.sidebar.button("Submit")
    if btn_submit and file_upload is not None:
        file_name = file_upload.name
        with open(f"resources/Text/{file_name}", "wb") as f:
            f.write(file_upload.getbuffer())            
            

if st_options == "Speech to Text":
    st.markdown("<h1 style='text-align: center; color: white;'>Speech to Text</h1>", unsafe_allow_html=True)
    file_upload = st.sidebar.file_uploader("Upload audio file", type=["mp3", "wav"])
    btn_submit = st.sidebar.button("Submit")
    if btn_submit and file_upload is not None:
        file_name = file_upload.name
        with open(f"resources/Audio/{file_name}", "wb") as f:
            f.write(file_upload.getbuffer())
            
if st_options == "Video Demo":
    with open("resources/url_demo.json", "r") as f:
        url_dict = json.load(f)
    st.markdown("<h1 style='text-align: center; color: white;'>Video Demo</h1>", unsafe_allow_html=True)
    options_demo = ["Xe cộ", "Khuôn mặt", "Container", "Khói lửa"]
    option_key = st.selectbox("Select options", options_demo)
    st.video(url_dict[option_key])
    

