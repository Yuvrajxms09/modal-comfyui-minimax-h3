"""Custom-node definitions grouped by selectable deployment profile."""

H3_PLUGINS = [
    {"url": "https://github.com/kijai/ComfyUI-KJNodes.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/T8mars/comfyui-minimax-h3-blockcache-T8.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/badgids/ComfyUI-H3-ExactAudioLock.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/T8mars/comfyui-minimax-h3-audio-T8.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/Adudeguyman/ComfyUI-Fantastic-MiniMaxH3-PromptBuilder.git", "requirements": ["requirements.txt"], "ext_deps": ["google-genai"]},
    {"url": "https://github.com/Jalen-Brunson/ComfyUI-HybridWindows.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/LBH-123-AI/Comfyui_Minimax_h3_latent_Upscaler.git", "commit": "40316cf008b2fd8663263270669eb4da23f89d2c", "requirements": ["requirements.txt"], "ext_deps": ["einops", "safetensors"]},
    {"url": "https://github.com/drozbay/MaskVidExperiments.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/rockerBOO/h3-latent-upscaler.git", "folder": "h3-latent-upscaler", "commit": "a5ed6e9586f0b14250a0018f78568e0076e4bd9d", "requirements": ["requirements.txt"], "ext_deps": ["einops", "safetensors"]},
    {"url": "https://github.com/seitanism/ComfyUI-H3-Motion-Context-MultiRef.git", "commit": "361624fb406b63eb6694442eac6c895fc1533a70", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/larryvrh/ComfyUI-MiniMax-H3-Turbo.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/kijai/ComfyUI-MelBandRoFormer.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/Shrek3OnVH5/MiniMax-H3-NativeAudio-MusicVideo-Workflow.git", "folder": "ComfyUI-H3-NativeAudioLock", "source_subdir": "custom_nodes/ComfyUI-H3-NativeAudioLock"},
    {"url": "https://github.com/chanon/comfyui-obvpm.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/chanon/comfyui-obvpm-timeline.git", "requirements": ["requirements.txt"]},
    {"url": "https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3.git", "requirements": ["requirements.txt"]},
]

PLUGIN_PROFILES = {"h3": H3_PLUGINS, "ltx25": [], "ltx25_prompt_enhancer": []}
REGISTRY_PLUGIN_PROFILES = {"h3": [], "ltx25": [], "ltx25_prompt_enhancer": []}


def get_plugins(selection):
    from models import resolve_profiles

    profiles = resolve_profiles(selection)
    external, registry = [], []
    for profile in profiles:
        external.extend(PLUGIN_PROFILES.get(profile, []))
        registry.extend(REGISTRY_PLUGIN_PROFILES.get(profile, []))
    return registry, external
