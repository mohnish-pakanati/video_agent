# AI Video Generation Pipeline

Generate talking videos from a text prompt using voice cloning, talking-face animation, and lip synchronisation — orchestrated with LangGraph.

## Architecture

```
START → voice_clone (XTTS v2) → video_generate (SadTalker) → lip_sync (Wav2Lip) → render (FFmpeg) → END
```

## Prerequisites

- **Python 3.10+**
- **FFmpeg** installed and on PATH
- **CUDA GPU** recommended (CPU works but is slow)

### External model repos

Clone these into the project root (or set env vars to point elsewhere):

```bash
git clone https://github.com/OpenTalker/SadTalker.git
git clone https://github.com/Rudrabha/Wav2Lip.git
```

Download the required model checkpoints per each repo's README.

## Installation

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

## Usage

### CLI

```bash
python run_pipeline.py \
    --text "Hello world" \
    --voice inputs/sample.wav \
    --image inputs/face.jpg \
    --prompt "confident cinematic delivery"
```

Output: `outputs/final_video.mp4`

### Streamlit UI

```bash
streamlit run ui.py
```

### Python

```python
from pipeline.runner import run_pipeline

video = run_pipeline(
    text="Hello world",
    voice_ref="inputs/sample.wav",
    face_image="inputs/face.jpg",
    acting_prompt="confident cinematic delivery",
)
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `SADTALKER_ROOT` | `./SadTalker` | Path to SadTalker repo |
| `WAV2LIP_ROOT` | `./Wav2Lip` | Path to Wav2Lip repo |
| `WAV2LIP_CHECKPOINT` | `./Wav2Lip/checkpoints/wav2lip_gan.pth` | Wav2Lip model weights |
| `WAV2LIP_ENABLED` | `true` | Set `false` to skip lip-sync step |
| `OUTPUT_DIR` | `./outputs` | Output directory |
| `INPUT_DIR` | `./inputs` | Input directory |
| `XTTS_MODEL` | `tts_models/multilingual/multi-dataset/xtts_v2` | TTS model ID |
| `FFMPEG_BIN` | `ffmpeg` | FFmpeg binary path |
| `DEVICE` | `auto` | `auto`, `cpu`, or `cuda` |
| `LOG_LEVEL` | `INFO` | Python logging level |

## GCP Deployment

The code avoids hardcoded paths — configure everything via environment variables. To run on a GCP GPU VM:

1. Provision a VM with NVIDIA GPU and CUDA drivers
2. Clone this repo and the model repos
3. Set env vars (`DEVICE=cuda`, paths to model dirs)
4. Run `python run_pipeline.py …` or `streamlit run ui.py`

## Project Structure

```
agent/          LangGraph state and graph definition
tools/          Individual pipeline step implementations
pipeline/       Pipeline orchestration / runner
utils/          Shared utilities (device, logging)
ui.py           Streamlit web interface
run_pipeline.py CLI entry point
config.py       Central configuration
```
