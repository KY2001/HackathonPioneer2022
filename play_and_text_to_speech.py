import os
import time
from gtts import gTTS
from playsound import playsound
import concurrent.futures


# mp3ファイル再生関数。引数はファイルパス（なるべく絶対パス）。
def play(path="sample.mp3"):
    playsound(path)


# テキスト読み上げ関数。引数はstr型文字列。
def auto_speech(text, file_name="0.mp3"):
    tts = gTTS(text=text, lang="ja")
    tts.save(os.path.dirname(__file__) + "/" + file_name)
    play(os.path.dirname(__file__) + "/" + file_name)


# 並列再生の確認用
def main():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    executor.submit(playsound, 'sample.mp3')
    executor.submit(auto_speech, 'おはようございます。朝です。')
    executor.shutdown()


if __name__ == "__main__":
    main()
