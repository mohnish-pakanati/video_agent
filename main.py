from pipeline.runner import run_pipeline

text = "Happy Birthday! Your birthday is on the International Day of Happiness."

voice_sample = "inputs/jensen_voice.wav"
face_image = "inputs/jensen_face.jpg"

video = run_pipeline(text, voice_sample, face_image)

print("Generated video:", video)