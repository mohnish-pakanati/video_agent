import streamlit as st
from pipeline.runner import run_pipeline
import tempfile

st.title("AI Cinematic Talking Avatar")

st.write("Generate a cinematic talking video using voice cloning and AI animation.")

text_input = st.text_area(
    "Dialogue",
    "Happy Birthday! Your birthday is on the International Day of Happiness."
)

acting_prompt = st.text_area(
    "Performance Prompt (How should the character behave?)",
    "Confident, cinematic delivery with a warm smile and natural head movement."
)

voice_file = st.file_uploader(
    "Upload reference voice sample",
    type=["wav"]
)

image_file = st.file_uploader(
    "Upload face image",
    type=["jpg","png"]
)

if st.button("Generate Video"):

    if voice_file is None or image_file is None:
        st.warning("Please upload both voice and image.")

    else:

        with tempfile.NamedTemporaryFile(delete=False) as vf:
            vf.write(voice_file.read())
            voice_path = vf.name

        with tempfile.NamedTemporaryFile(delete=False) as imf:
            imf.write(image_file.read())
            image_path = imf.name

        with st.spinner("Directing the AI actor..."):

            video_path = run_pipeline(
                text=text_input,
                voice_ref=voice_path,
                face_image=image_path,
                acting_prompt=acting_prompt
            )

        st.success("Video generated!")

        with open(video_path, "rb") as video_file:
            st.video(video_file.read())