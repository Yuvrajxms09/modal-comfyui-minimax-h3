"""MiniMax H3 text-to-video and image-to-video model files."""

models = [
    {
        "repo_id": "Comfy-Org/MiniMax-H3",
        "filename": "diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors",
        "model_dir": "diffusion_models",
    },
    {
        "repo_id": "Comfy-Org/MiniMax-H3",
        "filename": "text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors",
        "model_dir": "text_encoders",
    },
    {
        "repo_id": "Comfy-Org/MiniMax-H3",
        "filename": "vae/minimax_h3_video_vae_int8_convrot.safetensors",
        "model_dir": "vae",
    },
    {
        "repo_id": "Comfy-Org/MiniMax-H3",
        "filename": "vae/minimax_h3_audio_vae_fp32.safetensors",
        "model_dir": "vae",
    },
    {
        "repo_id": "Comfy-Org/MiniMax-H3",
        "filename": "loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors",
        "model_dir": "loras",
    },
]

models_ext = []
