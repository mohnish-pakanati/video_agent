from agent.graph import build_graph

def run_pipeline(text, voice_ref, face_image):

    graph = build_graph()

    state = {
        "text": text,
        "reference_voice": voice_ref,
        "face_image": face_image,
        "audio_path": "",
        "raw_video_path": "",
        "final_video_path": ""
    }

    result = graph.invoke(state)

    return result["final_video_path"]