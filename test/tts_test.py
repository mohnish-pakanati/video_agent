"""Smoke test for voice cloning via the tools.voice_clone module."""

import os
import sys

# Allow imports from project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import config
from utils.logging_setup import setup_logging
from tools.voice_clone import generate_voice

setup_logging()
config.ensure_dirs()

state = {
    "text": "Hello. This is a test of the voice cloning system.",
    "acting_prompt": "",
    "reference_voice": os.path.join(config.OUTPUT_DIR, "speaker.wav"),
    "face_image": "",
    "audio_path": "",
    "raw_video_path": "",
    "final_video_path": "",
}

result = generate_voice(state)
print("Audio generated:", result["audio_path"])
