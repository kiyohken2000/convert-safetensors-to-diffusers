from diffusers import StableDiffusionXLPipeline, AutoencoderKL
import torch
from config import MODEL_NAME

pipe = StableDiffusionXLPipeline.from_single_file(
  f"{MODEL_NAME}.safetensors",
)

folder = MODEL_NAME
pipe.save_pretrained(folder, safe_serialization=True)
pipe = pipe.to(torch_dtype=torch.float16)
pipe.save_pretrained(folder, safe_serialization=True, variant="fp16")