from diffusers import StableDiffusionXLPipeline
import torch
from datetime import datetime

model_path = "waiREALMIX_v70"  # コンバートしたモデルのパス
pipe = StableDiffusionXLPipeline.from_pretrained(
  model_path,
  torch_dtype=torch.float32,
).to("cpu")

prompt = "topless girl"
image = pipe(prompt).images[0]

# 現在の日時からタイムスタンプを生成
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# 画像を表示
image.show()

# 画像をファイルに保存
image.save(f"output_{timestamp}.png")