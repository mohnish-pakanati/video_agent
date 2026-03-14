import torchaudio
from TTS.api import TTS

# Prefer a non-torchcodec backend so we don't need torchcodec/FFmpeg at runtime.
# 'sox_io' is commonly available in torchaudio wheels; fall back to 'soundfile' if needed.
try:
    torchaudio.set_audio_backend("sox_io")
except Exception:
    try:
        torchaudio.set_audio_backend("soundfile")
    except Exception:
        pass

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

tts.tts_to_file(
    text="Hello. This is a test of the voice cloning system.",
    # use a local WAV speaker file (we'll create outputs/speaker.wav from the original OPUS)
    speaker_wav="outputs/speaker.wav",
    file_path="outputs/test_audio.wav",
    language="en",
)