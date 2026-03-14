import logging

import config
from agent.graph import build_graph
from utils.logging_setup import setup_logging

logger = logging.getLogger(__name__)


def run_pipeline(
    text: str,
    voice_ref: str,
    face_image: str,
    acting_prompt: str = "",
) -> str:
    """Run the full video-generation pipeline and return the final video path."""

    setup_logging()
    config.ensure_dirs()

    state = {
        "text": text,
        "acting_prompt": acting_prompt,
        "reference_voice": voice_ref,
        "face_image": face_image,
        "audio_path": "",
        "raw_video_path": "",
        "final_video_path": "",
    }

    logger.info("Starting pipeline — text=%d chars, voice=%s, image=%s",
                len(text), voice_ref, face_image)

    graph = build_graph()
    result = graph.invoke(state)

    final_path = result["final_video_path"]
    logger.info("Pipeline complete — output: %s", final_path)
    return final_path
