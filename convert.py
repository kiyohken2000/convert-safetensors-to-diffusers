from diffusers import StableDiffusionXLPipeline, AutoencoderKL
import torch

pipe = StableDiffusionXLPipeline.from_single_file(
  "AnythingXL_xl.safetensors",
)

folder = "AnythingXL_xl"
pipe.save_pretrained(folder, safe_serialization=True)
pipe = pipe.to(torch_dtype=torch.float16)
pipe.save_pretrained(folder, safe_serialization=True, variant="fp16")