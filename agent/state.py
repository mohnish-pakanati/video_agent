from typing import TypedDict

class VideoAgentState(TypedDict):
    text: str
    reference_voice: str
    face_image: str
    
    audio_path: str
    raw_video_path: str
    final_video_path: str