# Convert safetensors to diffusers

civitaiでダウンロードした`.safetensors`ファイルをdiffusersで使えるように変換するスクリプト

## 動作した環境

- macOS 14.5
- Python 3.9.6
- pip 24.0

## ファイル説明

- convert.py => 変換用スクリプト
- test.py => 変換後のモデルの動作確認用スクリプト
- command.txt => 使いそうなコマンドをまとめた

## 使い方

### パッケージのインストール

```
pip install -r requirements.txt
```

### 変換

1. civitaiから`.safetensors`ファイルをダウンロードしてこのディレクトリにコピー

2. `convert.py`の5行目をダウンロードしたファイル名に変更する(例: "waiREALMIX_v70.safetensors")

3. `convert.py`の8行目を変換後のフォルダ名にする(例: "waiREALMIX_v70")

4. スクリプトの実行`python convert.py`

5. 成功した場合は3で指定したフォルダと中身が作成される

### ローカルで動作確認

1. `test.py`の5行目を変換後のフォルダ名に変更(例: "waiREALMIX_v70")

2. Geforceを使用する場合は`test.py`の9行目の`cpu`を`cuda`に変更

3. スクリプトの実行`python test.py`

4. 成功した場合は`output_20230526_123456.png`のようにタイムスタンプがついたファイル名で保存される