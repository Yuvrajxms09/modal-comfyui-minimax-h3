# modal-comfyui

Run ComfyUI on Modal.com with auto-scaling, GPU snapshots, and easy model management.

Good for testing Wan2.2/LTX-2.5/MiniMax-H3 or other image/video/audio generation models.

<i><b>Note:</b> If you want to work (creating/editing) on your workflows locally while seamlessly runs the workflow on Cloud GPU, you can install ComfyUI-Proxy custom node on your local ComfyUI https://github.com/anr2me/comfyui-proxy  
(ComfyGPU's URL for Remote GPU URL, and optionally ComfyCPU's URL for Remote CPU URL).</i>

## Prerequisites

- A [Modal](https://modal.com/) account
- Python installed
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) installed

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Yuvrajxms09/modal-comfyui-minimax-h3.git
   cd modal-comfyui-minimax-h3
   ```
2. Install the Modal client:
   ```bash
   uv sync
   ```
   2.1. Activate the virtual environment (if you're not already use a venv):
     ```
     source .venv/bin/activate
     ```
     Or on Windows (CMD):
     ```
     \.venv\Scripts\activate.bat 
     ```
     Or PowerShell:
     ```
     .\.venv\Scripts\Activate.ps1 
     ```
     _**Note:** If PowerShell shows a script execution error, you might need to run this first:_
     ```
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
     ```
4. Set up your modal account (if not done already):
   ```bash
   modal setup
   ```

## Configuration

### Model profiles

`COMFY_PROFILES` selects the models, custom nodes, and optional workflow assets for a deployment. ComfyUI defaults to the latest release (`COMFY_VER=latest`). The default profile remains `h3` for existing deployments.

```bash
# MiniMax H3
modal deploy comfyui.py

# LTX-2.5 only: no H3 weights, custom nodes, or private H3 workflow downloads
COMFY_PROFILES=ltx25 modal deploy comfyui.py

# LTX-2.5 with the optional Gemma prompt-enhancer encoder
COMFY_PROFILES=ltx25_prompt_enhancer modal deploy comfyui.py

# Combine profiles when one ComfyUI deployment needs both
COMFY_PROFILES=h3,ltx25 modal deploy comfyui.py
```

LTX-2.5 uses ComfyUI's built-in nodes and downloads the official ComfyUI INT8 ConvRot transformer and text encoder, BF16 video/audio VAEs, and BF16 2x latent upscaler. The prompt-enhancer encoder is optional. H3 weights and its workflow-specific LoRAs are defined separately in `MODEL_PROFILES` in `models.py`.

Each profile gets its own persistent Modal volume by default (`hf-hub-cache` for H3, and a profile-derived volume for other selections), avoiding reuse of another profile's model cache. Set `MODAL_VOLUME_NAME` to override this behavior. `HF_TOKEN` can be supplied through the Modal `huggingface-secret` for faster or gated Hugging Face downloads.

To add a model family, add a named entry to `MODEL_PROFILES` in `models.py` and its external downloads in `EXTERNAL_MODEL_PROFILES` if needed. Add required custom nodes to the matching profile in `PLUGIN_PROFILES` in `plugins.py`. Leave the profile's node list empty when the required nodes are built into ComfyUI. Multi-profile deployments merge model and node definitions.

The optional `private_assets.py` file supports local-only workflow and prompt-pack downloads. It is gitignored so private repository names and workflow configuration are not published. Without it, public H3 model downloads still work and personal workflows are skipped.

### Models and custom nodes

Hugging Face entries use `repo_id`, `filename`, and `model_dir`; direct downloads use `url`, `filename`, and `model_dir`. Relative model paths are resolved under `ComfyUI/models`; absolute paths can target node-specific folders. Profile-specific nodes support optional `branch`, `commit`, `folder`, `source_subdir`, `requirements`, and `ext_deps` fields. A root-level `workflow_api.json` can also install its required nodes during the image build.

## Usage

### Serve (Development)

Run the following command to start ComfyUI in development mode:
```bash
modal serve comfyui.py
```
This will provide a temporary URL where you can access the ComfyUI interface.

### Deploy (Production)

To deploy ComfyUI as a persistent app using the default L4 GPU:
```bash
modal deploy comfyui.py
```
Or rebuild the image and deploy (ie. after removing models at persistent volume to redownload them):
```bash
MODAL_FORCE_BUILD=1 modal deploy comfyui.py
```
Or deploy with cleared `shared_dict` (ie. when the App forcefully stopped):
```bash
python comfyui.py
```
Or change the GPU with:
```bash
MODAL_GPU=RTX-PRO-6000 modal deploy comfyui.py
```
You can find the GPU types available on modal.com at https://modal.com/docs/guide/gpu

Other Environment Variables you can use are:
```bash
COMFY_PROFILES="h3" # comma-separated: h3, ltx25, ltx25_prompt_enhancer
COMFY_VER="latest" # or "nightly --commit <hash>" or "nightly --pr kijai:minimax_fun"
MODAL_VOLUME_NAME="" # optional override for the profile-specific cache volume
COMFYGPU_ARGS="--use-flash-attention --preview-method auto --front-end-version Comfy-Org/ComfyUI_frontend@1.45.21"
COMFYMIX_ARGS="--preview-method auto --front-end-version Comfy-Org/ComfyUI_frontend@1.45.21 --enable-manager-legacy-ui"
JOBS_CUTOFFTIME=172800
MODAL_MAXTIME=3600
MODAL_IDLETIME=38
MODAL_WAITTIME=20
MODAL_MAXSTARTTIME=300
MODAL_USE_AUTH=True
```
You can access ComfyUI from the provided persistent URL when successfully deployed.  
Authentication is enabled by default. Create a Modal Proxy Token in Settings and provide it when accessing the app. Set `MODAL_USE_AUTH=False` only if you intentionally want a public endpoint.

## Features

- **Auto-scaling**: Scales down to zero when not in use to save costs (modal's serverless can also auto-scales vertically, where CPU cores and RAM size can grow automatically as needed, so you don't need to overprovision them).
- **GPU Snapshots**: Fast startup times using Modal's GPU snapshots (cold-start can be under 3 seconds).
- **Model Caching**: Uses Modal Volumes to cache models across runs (modal's persistent volume is free for the first 1 TiB).
- **Custom Node Management**: Integrated with `comfy-cli` for easy plugin installation.
- **Mixed CPU and GPU instance**: Create/Edit your workflows using CPU-only instance for cheaper rates, but runs workflows on GPU instance seamlessly. Also have persistent completed jobs across sessions with their output assets accessible from Media Assets panel.
- **Pre-installed Wheels**:
  - PyTorch+CUDA 13.0
  - FlashAttention 2.8.3, 3, and 4
  - SageAttention 2.2 and 3
  - SpargeAttention 0.1
  - nunchaku 1.2.1
  - llama-cpp-python

## Contributing

Please feel free to contribute to make this project better.
Performance improvements/optimizations are very welcome.
