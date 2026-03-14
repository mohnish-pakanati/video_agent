import logging

from langgraph.graph import StateGraph

from agent.state import VideoAgentState
from tools.voice_clone import generate_voice
from tools.video_generation import generate_video
from tools.lip_sync import run_lipsync
from tools.render import render_video

logger = logging.getLogger(__name__)


def build_graph():
    """Build and compile the LangGraph pipeline.

    Flow: voice_clone → video_generate → lip_sync → render → END
    """

    workflow = StateGraph(VideoAgentState)

    workflow.add_node("voice_clone", generate_voice)
    workflow.add_node("video_generate", generate_video)
    workflow.add_node("lip_sync", run_lipsync)
    workflow.add_node("render", render_video)

    workflow.set_entry_point("voice_clone")

    workflow.add_edge("voice_clone", "video_generate")
    workflow.add_edge("video_generate", "lip_sync")
    workflow.add_edge("lip_sync", "render")

    workflow.set_finish_point("render")

    graph = workflow.compile()
    logger.info("LangGraph pipeline compiled (4 nodes)")
    return graph
