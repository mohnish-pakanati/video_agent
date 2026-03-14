import os
import tempfile

import streamlit as st

from pipeline.runner import run_pipeline

st.title("AI Cinematic Talking Avatar")
st.write("Generate a cinematic talking video using voice cloning and AI animation.")

text_input = st.text_area(
    "Dialogue",
    "Happy Birthday! Your birthday is on the International Day of Happiness.",
)

acting_prompt = st.text_area(
    "Performance Prompt (How should the character behave?)",
    "Confident, cinematic delivery with a warm smile and natural head movement.",
)

voice_file = st.file_uploader("Upload reference voice sample", type=["wav"])
image_file = st.file_uploader("Upload face image", type=["jpg", "png"])

if st.button("Generate Video"):
    if voice_file is None or image_file is None:
        st.warning("Please upload both a voice sample and a face image.")
    else:
        # Write uploads to temp files with correct suffixes
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as vf:
            vf.write(voice_file.read())
            voice_path = vf.name

        ext = os.path.splitext(image_file.name)[1] or ".jpg"
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as imf:
            imf.write(image_file.read())
            image_path = imf.name

        try:
            with st.spinner("Directing the AI actor …"):
                video_path = run_pipeline(
                    text=text_input,
                    voice_ref=voice_path,
                    face_image=image_path,
                    acting_prompt=acting_prompt,
                )

            st.success("Video generated!")
            with open(video_path, "rb") as video_file:
                st.video(video_file.read())

        except Exception as e:
            st.error(f"Pipeline failed: {e}")

        finally:
            # Clean up temp files
            for p in (voice_path, image_path):
                if os.path.isfile(p):
                    os.unlink(p)
