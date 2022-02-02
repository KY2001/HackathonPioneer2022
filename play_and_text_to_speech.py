import pyttsx3
import time
from playsound import playsound
import concurrent.futures


# mp3ファイル再生関数。引数はファイルパス（なるべく絶対パス）。
def play():
    playsound("sample.mp3")


# テキスト読み上げ関数。引数はstr型文字列。
def auto_speech(text):
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty("voice", voices[2].id) # <- 雪吉の環境(windows)だと必要でした。
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)


# 並列再生の確認用
def main():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    executor.submit(playsound, 'sample.mp3')
    executor.submit(auto_speech, 'おはようございます。朝です。')
    executor.shutdown()


if __name__ == "__main__":
    main()
