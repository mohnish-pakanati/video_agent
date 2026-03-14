import logging
import os
import subprocess

import config

logger = logging.getLogger(__name__)


def render_video(state: dict) -> dict:
    """Re-encode the video to H.264/AAC for broad compatibility."""

    input_video = state["final_video_path"]

    if not os.path.isfile(input_video):
        raise FileNotFoundError(f"Input video for rendering not found: {input_video}")

    output_path = os.path.join(config.OUTPUT_DIR, "final_video.mp4")

    command = [
        config.FFMPEG_BIN, "-y",
        "-i", input_video,
        "-c:v", "libx264", "-preset", "medium", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        output_path,
    ]

    logger.info("Rendering final video with FFmpeg …")

    result = subprocess.run(command, capture_output=True, text=True, check=False)

    if result.returncode != 0:
        logger.error("FFmpeg stderr:\n%s", result.stderr)
        raise RuntimeError(f"FFmpeg render failed (exit {result.returncode}): {result.stderr[:500]}")

    if not os.path.isfile(output_path):
        raise FileNotFoundError(f"Rendered video not created: {output_path}")

    size_mb = os.path.getsize(output_path) / 1_000_000
    logger.info("Final video: %s (%.1f MB)", output_path, size_mb)

    state["final_video_path"] = output_path
    return state
