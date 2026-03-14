import glob
import logging
import os
import subprocess
import sys

import config

logger = logging.getLogger(__name__)


def generate_video(state: dict) -> dict:
    """Run SadTalker to generate a talking-face video from an image and audio."""

    image = state["face_image"]
    audio = state["audio_path"]

    if not os.path.isfile(image):
        raise FileNotFoundError(f"Face image not found: {image}")
    if not os.path.isfile(audio):
        raise FileNotFoundError(f"Audio file not found: {audio}")

    inference_script = os.path.join(config.SADTALKER_ROOT, "inference.py")
    if not os.path.isfile(inference_script):
        raise FileNotFoundError(
            f"SadTalker inference.py not found at {inference_script}. "
            f"Set SADTALKER_ROOT env var to the SadTalker repo directory."
        )

    result_dir = os.path.join(config.OUTPUT_DIR, "sadtalker")
    os.makedirs(result_dir, exist_ok=True)

    command = [
        sys.executable,
        inference_script,
        "--driven_audio", audio,
        "--source_image", image,
        "--result_dir", result_dir,
        "--enhancer", "gfpgan",
    ]

    logger.info("Running SadTalker: %s", " ".join(command))

    result = subprocess.run(command, capture_output=True, text=True, check=False)
    logger.debug("SadTalker stdout:\n%s", result.stdout)

    if result.returncode != 0:
        logger.error("SadTalker stderr:\n%s", result.stderr)
        raise RuntimeError(f"SadTalker failed (exit {result.returncode}): {result.stderr[:500]}")

    # SadTalker outputs to a timestamped subdirectory — find the newest mp4.
    mp4_files = glob.glob(os.path.join(result_dir, "**", "*.mp4"), recursive=True)
    if not mp4_files:
        raise FileNotFoundError(f"No .mp4 files found in SadTalker output dir: {result_dir}")

    output_video = max(mp4_files, key=os.path.getmtime)
    logger.info("SadTalker output video: %s", output_video)

    state["raw_video_path"] = output_video
    return state
