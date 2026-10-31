"""Model files grouped by selectable deployment profile."""

MODEL_PROFILES = {
    'h3': [
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors',
        'model_dir': 'diffusion_models',
    },
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors',
        'model_dir': 'diffusion_models',
    },
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors',
        'model_dir': 'text_encoders',
    },
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'vae/minimax_h3_video_vae_int8_convrot.safetensors',
        'model_dir': 'vae',
    },
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'vae/minimax_h3_video_vae_fp16.safetensors',
        'model_dir': 'vae',
    },
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'vae/minimax_h3_audio_vae_fp32.safetensors',
        'model_dir': 'vae',
    },
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors',
        'model_dir': 'loras',
    },
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'loras/minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors',
        'model_dir': 'loras',
    },
    {
        'repo_id': 'Kijai/MiniMax-H3_comfy',
        'filename': 'loras/minimax_h3_fl2v_lightx2v_turbo_4step_v0.1_comfy.safetensors',
        'model_dir': 'loras/minimax',
    },
    {
        'repo_id': 'Kijai/MiniMax-H3-experimental',
        'filename': 'loras/MiniMax-H3-Ref2VA-Acc-8Step_comfy.safetensors',
        'model_dir': 'loras/minimax',
    },
    {
        'repo_id': 'drbaph/MiniMax-H3-Turbo-Lora-ComfyUI',
        'filename': 'experimental/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors',
        'model_dir': 'loras/minimax',
    },
    {
        'repo_id': 'lightx2v/Minimax-h3-Turbo',
        'filename': 'minimax_h3_ref2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors',
        'model_dir': 'loras/minimax',
    },
    {
        'repo_id': 'Kijai/MiniMax-H3_comfy',
        'filename': 'loras/minimax_h3_ref2v_lightx2v_turbo_4step_v0.1_resized_avg_rank_20_bf16.safetensors',
        'model_dir': 'loras/minimax',
    },
    {
        'repo_id': 'LBH-123-AI/Minimax_h3_latent_Upscaler',
        'filename': 'minimax_h3_latent_upscaler_3d_conv_v1/minimax_h3_latent_upscaler_3d_conv_v1_fp32.pth',
        'model_dir': 'latent_upscale_models/minimax_h3_latent_upscaler_3d_conv_v1',
    },
    {
        'repo_id': 'Comfy-Org/sam3.1',
        'filename': 'checkpoints/sam3.1_multiplex_fp16.safetensors',
        'model_dir': 'checkpoints',
    },
    {
        'repo_id': 'Kijai/MiniMax-H3-TAE',
        'filename': 'vae_approx/taeh3.safetensors',
        'model_dir': 'vae_approx',
    },
    {
        'repo_id': 'Kijai/MelBandRoFormer_comfy',
        'filename': 'MelBandRoformer_fp16.safetensors',
        'model_dir': 'diffusion_models',
    },
    {
        'repo_id': 'Kijai/MiniMax-H3_comfy',
        'filename': 'loras/minimax_h3_ref2v_lightx2v_turbo_4step_v0.1_resized_avg_rank_20_bf16.safetensors',
        'model_dir': 'loras/h3',
    },
    {
        'repo_id': 'Comfy-Org/MiniMax-H3',
        'filename': 'loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors',
        'model_dir': 'loras/h3',
    },
    {
        'repo_id': 'Kijai/MiniMax-H3_comfy',
        'filename': 'loras/minimax_h3_fl2v_lightx2v_turbo_4step_v0.1_comfy.safetensors',
        'model_dir': 'loras/h3',
    },
    ],
    'ltx25': [
    {
        'repo_id': 'Lightricks/LTX-2.5',
        'filename': 'diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors',
        'model_dir': 'diffusion_models',
    },
    {
        'repo_id': 'Lightricks/LTX-2.5',
        'filename': 'text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors',
        'model_dir': 'text_encoders',
    },
    {
        'repo_id': 'Lightricks/LTX-2.5',
        'filename': 'vae/ltx-2.5-video-vae-bf16.safetensors',
        'model_dir': 'vae',
    },
    {
        'repo_id': 'Lightricks/LTX-2.5',
        'filename': 'vae/ltx-2.5-audio-vae-bf16.safetensors',
        'model_dir': 'vae',
    },
    {
        'repo_id': 'Lightricks/LTX-2.5',
        'filename': 'latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors',
        'model_dir': 'latent_upscale_models',
    },
    ],
    'ltx25_prompt_enhancer': [
    {
        'repo_id': 'Comfy-Org/gemma-4',
        'filename': 'text_encoders/gemma4_e2b_it_int8_convrot.safetensors',
        'model_dir': 'text_encoders',
    },
    ],
}

EXTERNAL_MODEL_PROFILES = {"h3": [], "ltx25": [], "ltx25_prompt_enhancer": []}
KNOWN_PROFILES = tuple(MODEL_PROFILES)


def resolve_profiles(selection):
    """Parse/validate comma-separated profile names and deduplicate them."""
    if isinstance(selection, str):
        selected = [part.strip() for part in selection.split(",") if part.strip()]
    else:
        selected = [str(part).strip() for part in selection if str(part).strip()]
    if not selected:
        raise ValueError("Select at least one model profile.")
    if "ltx25_prompt_enhancer" in selected and "ltx25" not in selected:
        selected.insert(selected.index("ltx25_prompt_enhancer"), "ltx25")
    unknown = sorted(set(selected) - set(KNOWN_PROFILES))
    if unknown:
        raise ValueError(f"Unknown profile(s): {', '.join(unknown)}. Available: {', '.join(KNOWN_PROFILES)}")
    return tuple(dict.fromkeys(selected))


def get_model_config(selection):
    """Return de-duplicated Hugging Face and direct-download model definitions."""
    hf_models, external_models, seen = [], [], set()
    for profile in resolve_profiles(selection):
        for model in MODEL_PROFILES[profile]:
            key = (model["repo_id"], model["filename"], model["model_dir"])
            if key not in seen:
                hf_models.append(model)
                seen.add(key)
        external_models.extend(EXTERNAL_MODEL_PROFILES.get(profile, []))
    return hf_models, external_models
