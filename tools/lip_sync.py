import subprocess

def run_lipsync(state):

    video = state["raw_video_path"]
    audio = state["audio_path"]

    final_video = "outputs/final_video.mp4"

    command = [
        "python",
        "Wav2Lip/inference.py",
        "--face", video,
        "--audio", audio,
        "--outfile", final_video
    ]

    subprocess.run(command)

    state["final_video_path"] = final_video

    return state