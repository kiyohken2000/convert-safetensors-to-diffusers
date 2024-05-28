# Convert safetensors to diffusers

civitaiでダウンロードした`.safetensors`ファイルをdiffusersで使えるように変換するスクリプト

## 動作した環境

- macOS 14.5(Apple Silicon)
  - Python 3.9.6
  - pip 24.0

- Windows10
  - Python 3.12.3
  - pip 24.0

## ファイル説明

- convert.py => 変換用スクリプト
- test.py => 変換後のモデルの動作確認用スクリプト
- config.py => モデル名定義用
- commands.txt => 使いそうなコマンドをまとめた

## 使い方

### パッケージのインストール

```
pip install -r requirements.txt
```

### 変換

1. civitaiから`.safetensors`ファイルをダウンロードしてこのディレクトリにコピー

2. `config.py`の`MODEL_NAME`をダウンロードしたファイル名に変更する(例: "waiREALMIX_v70.safetensors"なら"waiREALMIX_v70")

3. スクリプトの実行`python convert.py`

4. 成功した場合は2で指定したフォルダと中身が作成される

### ローカルで動作確認

1. Geforceを使用する場合は`test.py`の10行目の`cpu`を`cuda`に変更

2. スクリプトの実行`python test.py`

3. 成功した場合は`output_20230526_123456.png`のようにタイムスタンプがついたファイル名で保存される

### Huggingface

HuggingfaceのInference APIで使いたい場合はアップロード後にモデルカード(README.md)の作成が必要