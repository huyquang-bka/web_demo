import cv2
import streamlit as st
from apis import text_to_speech, speech_to_text, clip
from tools import base64_to_image


st.set_page_config("App Demo", "🚀", "wide", "expanded")

options = ["Chuyển đổi văn bản sang giọng nói", "Chuyển đổi giọng nói sang văn bản", "Tìm kiếm hình ảnh bằng từ khóa"]
st_options = st.sidebar.selectbox("Select options", options)

if st_options == options[0]:
    st.markdown("<h1 style='text-align: center; color: white;'>Chuyển đổi văn bản sang giọng nói</h1>", unsafe_allow_html=True)
    txt_input = st.text_area("Input text")
    type_voice = st.selectbox("Select voice", [1, 2, 3])
    btn_submit = st.button("Submit")
    if btn_submit:
        if txt_input == "":
            st.error("Vui lòng nhập văn bản")
        else:
            with st.spinner("Processing..."):
                type_voice = type_voice + 1
                file_name = text_to_speech({"text": txt_input, "voice_id": type_voice})
            full_path = fr"\\PC198\output\{file_name}"
            try:
                st.audio(full_path)
            except OSError as er:
                pass

if st_options == options[1]:
    st.markdown("<h1 style='text-align: center; color: white;'>Chuyển đổi giọng nói sang văn bản</h1>", unsafe_allow_html=True)
    file_upload = st.sidebar.file_uploader("Upload audio file", type=["mp3", "wav", "m4a"])
    btn_submit = st.sidebar.button("Submit")
    if btn_submit and file_upload is not None:
        file_name = file_upload.name
        with open(f"resources/Audio/{file_name}", "wb") as f:
            f.write(file_upload.getbuffer())
        with st.spinner("Processing..."):
            text = speech_to_text(f"resources/Audio/{file_name}")
            if text is not None:
                st.write(text)
            else:
                st.error("Không nhận diện được giọng nói")
            
if st_options == options[2]:
    st.markdown("<h1 style='text-align: center; color: white;'>Tìm kiếm hình ảnh bằng từ khóa</h1>", unsafe_allow_html=True)
    text_input = st.text_area("Input text", placeholder="Nhập từ khóa, ví dụ: a photo of red Honda car")
    num_image = st.slider("Select number of image", 1, 10, 5)
    btn_submit = st.button("Submit")
    if btn_submit:
        if text_input == "":
            st.error("Vui lòng nhập từ khóa")
        else:
            payload = {"text": text_input, "num_image": num_image}
            with st.spinner("Processing..."):
                list_image = clip(payload)
            if list_image is not None:
                col1, col2, col3 = st.columns(3)
                for i, image in enumerate(list_image):
                    img = base64_to_image(image)
                    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    rgb_img = cv2.resize(rgb_img, dsize=(1280, 720))
                    if i % 3 == 0:
                        col1.image(rgb_img, use_column_width=True)
                    elif i % 3 == 1:
                        col2.image(rgb_img, use_column_width=True)
                    else:
                        col3.image(rgb_img, use_column_width=True)
            else:
                st.error("Không tìm thấy hình ảnh phù hợp")
            
# if st_options == "Video Demo":
#     with open("resources/url_demo.json", "r") as f:
#         url_dict = json.load(f)
#     st.markdown("<h1 style='text-align: center; color: white;'>Video Demo</h1>", unsafe_allow_html=True)
#     options_demo = ["Xe cộ", "Khuôn mặt", "Container", "Khói lửa"]
#     option_key = st.selectbox("Select options", options_demo)
#     st.video(url_dict[option_key])
