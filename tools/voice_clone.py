from TTS.api import TTS

def generate_voice(state):

    text = state["text"]
    ref_audio = state["reference_voice"]

    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

    output_audio = "outputs/generated_voice.wav"

    tts.tts_to_file(
        text=text,
        speaker_wav=ref_audio,
        file_path=output_audio
    )

    state["audio_path"] = output_audio

    return state