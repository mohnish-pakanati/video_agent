"""Quick example showing how to invoke the pipeline from Python."""

from pipeline.runner import run_pipeline

text = "Happy Birthday! Your birthday is on the International Day of Happiness."
voice_sample = "inputs/jensen_voice.wav"
face_image = "inputs/jensen_face.jpg"
acting_prompt = "Confident, cinematic delivery with a warm smile."

try:
    video = run_pipeline(text, voice_sample, face_image, acting_prompt)
    print("Generated video:", video)
except Exception as e:
    print("Pipeline failed:", e)
