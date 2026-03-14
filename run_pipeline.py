"""CLI entry point for the AI video generation pipeline.

Usage:
    python run_pipeline.py \
        --text "Hello world" \
        --voice inputs/sample.wav \
        --image inputs/face.jpg \
        --prompt "confident cinematic delivery"
"""

import argparse
import sys

from pipeline.runner import run_pipeline


def main():
    parser = argparse.ArgumentParser(description="AI Video Generation Pipeline")
    parser.add_argument("--text", required=True, help="Dialogue text to speak")
    parser.add_argument("--voice", required=True, help="Path to reference voice WAV file")
    parser.add_argument("--image", required=True, help="Path to face image (jpg/png)")
    parser.add_argument("--prompt", default="", help="Acting / performance prompt")
    args = parser.parse_args()

    try:
        result = run_pipeline(args.text, args.voice, args.image, args.prompt)
        print(f"Video generated: {result}")
    except Exception as e:
        print(f"Pipeline failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
