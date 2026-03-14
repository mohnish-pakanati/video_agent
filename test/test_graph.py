"""Verify the LangGraph pipeline compiles and the state schema is correct."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from agent.state import VideoAgentState
from agent.graph import build_graph
from utils.logging_setup import setup_logging

setup_logging()

# Check state schema has all expected fields
expected_fields = [
    "text", "acting_prompt", "reference_voice", "face_image",
    "audio_path", "raw_video_path", "final_video_path",
]

annotations = VideoAgentState.__annotations__
for field in expected_fields:
    assert field in annotations, f"Missing field in VideoAgentState: {field}"

print(f"State schema OK — {len(expected_fields)} fields")

# Check graph compiles
graph = build_graph()
print("Graph compiled OK")
print("Done.")
