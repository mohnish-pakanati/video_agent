import subprocess

def generate_video(state):

    image = state["face_image"]
    audio = state["audio_path"]

    output_video = "outputs/generated_face.mp4"

    command = [
        "python",
        "SadTalker/inference.py",
        "--driven_audio", audio,
        "--source_image", image,
        "--result_dir", "outputs"
    ]

    subprocess.run(command)

    state["raw_video_path"] = output_video

    return state