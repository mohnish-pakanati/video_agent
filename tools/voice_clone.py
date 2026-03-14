import logging
import os

from TTS.api import TTS

import config
from utils.device import get_device

logger = logging.getLogger(__name__)

# Lazy singleton — the XTTS model is large; load once and reuse.
_tts_instance = None


def _get_tts():
    global _tts_instance
    if _tts_instance is None:
        device = get_device(config.DEVICE)
        logger.info("Loading XTTS v2 model (%s) …", config.XTTS_MODEL)
        _tts_instance = TTS(config.XTTS_MODEL).to(device)
        logger.info("XTTS v2 model loaded.")
    return _tts_instance


def generate_voice(state: dict) -> dict:
    """Clone voice from reference audio and synthesise speech."""

    text = state["text"]
    ref_audio = state["reference_voice"]

    if not os.path.isfile(ref_audio):
        raise FileNotFoundError(f"Reference voice file not found: {ref_audio}")

    output_audio = os.path.join(config.OUTPUT_DIR, "generated_voice.wav")
    logger.info("Generating speech (%d chars) with voice cloned from %s", len(text), ref_audio)

    tts = _get_tts()
    tts.tts_to_file(
        text=text,
        speaker_wav=ref_audio,
        language="en",
        file_path=output_audio,
    )

    if not os.path.isfile(output_audio):
        raise FileNotFoundError(f"TTS output not created: {output_audio}")

    logger.info("Speech audio saved to %s", output_audio)
    state["audio_path"] = output_audio
    return state
