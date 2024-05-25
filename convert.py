from diffusers import StableDiffusionXLPipeline
import torch

pipe = StableDiffusionXLPipeline.from_single_file(
  "waiREALMIX_v70.safetensors",
)
pipe.save_pretrained(
  "waiREALMIX_v70",
)