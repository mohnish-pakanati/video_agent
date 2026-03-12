from langgraph.graph import StateGraph
from agent.state import VideoAgentState

from tools.voice_clone import generate_voice
from tools.video_generation import generate_video
from tools.lip_sync import run_lipsync

def build_graph():

    workflow = StateGraph(VideoAgentState)

    workflow.add_node("voice_clone", generate_voice)
    workflow.add_node("video_generate", generate_video)
    workflow.add_node("lip_sync", run_lipsync)

    workflow.set_entry_point("voice_clone")

    workflow.add_edge("voice_clone", "video_generate")
    workflow.add_edge("video_generate", "lip_sync")

    workflow.set_finish_point("lip_sync")

    return workflow.compile()