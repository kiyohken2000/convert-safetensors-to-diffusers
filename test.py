from diffusers import StableDiffusionXLPipeline
import torch
from datetime import datetime
import time

from config import MODEL_NAME

# 開始時間を記録
start_time = time.time()

model_path = MODEL_NAME
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

# 終了時間を記録し、実行時間を計算
end_time = time.time()
execution_time = end_time - start_time

# 実行時間を分と秒に変換
minutes, seconds = divmod(execution_time, 60)

# 実行時間をコンソールに出力
print(f"実行時間: {int(minutes)}分{int(seconds)}秒")