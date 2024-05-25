from diffusers import StableDiffusionXLPipeline
import torch

pipe = StableDiffusionXLPipeline.from_single_file(
  "ponyDiffusionV5_v55.safetensors",
)
pipe.save_pretrained(
  "ponyDiffusionV5_v55",
)