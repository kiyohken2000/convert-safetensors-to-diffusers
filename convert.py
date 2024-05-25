from diffusers import StableDiffusionXLPipeline
import torch

pipe = StableDiffusionXLPipeline.from_single_file(
  "waiANIMIXPONYXL_v10.safetensors",
)
pipe.save_pretrained(
  "waiANIMIXPONYXL_v10",
)