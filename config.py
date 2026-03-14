import os

# ---------------------------------------------------------------------------
# Central configuration — all paths and settings read from environment
# variables with sensible local defaults.
# ---------------------------------------------------------------------------

SADTALKER_ROOT = os.environ.get("SADTALKER_ROOT", os.path.join(".", "SadTalker"))
WAV2LIP_ROOT = os.environ.get("WAV2LIP_ROOT", os.path.join(".", "Wav2Lip"))
WAV2LIP_CHECKPOINT = os.environ.get(
    "WAV2LIP_CHECKPOINT",
    os.path.join(".", "Wav2Lip", "checkpoints", "wav2lip_gan.pth"),
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", os.path.join(".", "outputs"))
INPUT_DIR = os.environ.get("INPUT_DIR", os.path.join(".", "inputs"))
MODEL_DIR = os.environ.get("MODEL_DIR", os.path.join(".", "models"))

XTTS_MODEL = os.environ.get("XTTS_MODEL", "tts_models/multilingual/multi-dataset/xtts_v2")
FFMPEG_BIN = os.environ.get("FFMPEG_BIN", "ffmpeg")

# "auto" | "cpu" | "cuda"
DEVICE = os.environ.get("DEVICE", "auto")

# Set to "false" to skip the Wav2Lip lip-sync step
WAV2LIP_ENABLED = os.environ.get("WAV2LIP_ENABLED", "true").lower() == "true"

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")


def ensure_dirs():
    """Create required directories if they don't exist."""
    for d in (OUTPUT_DIR, INPUT_DIR, MODEL_DIR):
        os.makedirs(d, exist_ok=True)
