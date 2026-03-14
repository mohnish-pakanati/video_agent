import logging
import os
import subprocess
import sys

import config

logger = logging.getLogger(__name__)


def run_lipsync(state: dict) -> dict:
    """Refine lip sync with Wav2Lip. Skipped when WAV2LIP_ENABLED is False."""

    if not config.WAV2LIP_ENABLED:
        logger.info("Wav2Lip disabled — skipping lip-sync step.")
        state["final_video_path"] = state["raw_video_path"]
        return state

    video = state["raw_video_path"]
    audio = state["audio_path"]

    if not os.path.isfile(video):
        raise FileNotFoundError(f"Raw video not found: {video}")
    if not os.path.isfile(audio):
        raise FileNotFoundError(f"Audio file not found: {audio}")

    inference_script = os.path.join(config.WAV2LIP_ROOT, "inference.py")
    if not os.path.isfile(inference_script):
        raise FileNotFoundError(
            f"Wav2Lip inference.py not found at {inference_script}. "
            f"Set WAV2LIP_ROOT env var to the Wav2Lip repo directory."
        )

    checkpoint = config.WAV2LIP_CHECKPOINT
    if not os.path.isfile(checkpoint):
        raise FileNotFoundError(
            f"Wav2Lip checkpoint not found: {checkpoint}. "
            f"Download it and set WAV2LIP_CHECKPOINT env var."
        )

    final_video = os.path.join(config.OUTPUT_DIR, "lipsync_output.mp4")

    command = [
        sys.executable,
        inference_script,
        "--checkpoint_path", checkpoint,
        "--face", video,
        "--audio", audio,
        "--outfile", final_video,
    ]

    logger.info("Running Wav2Lip: %s", " ".join(command))

    result = subprocess.run(command, capture_output=True, text=True, check=False)
    logger.debug("Wav2Lip stdout:\n%s", result.stdout)

    if result.returncode != 0:
        logger.error("Wav2Lip stderr:\n%s", result.stderr)
        raise RuntimeError(f"Wav2Lip failed (exit {result.returncode}): {result.stderr[:500]}")

    if not os.path.isfile(final_video):
        raise FileNotFoundError(f"Wav2Lip output not created: {final_video}")

    logger.info("Wav2Lip output video: %s", final_video)
    state["final_video_path"] = final_video
    return state
