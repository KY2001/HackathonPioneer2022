import speech_recognition as sr


def record_and_to_text():  # 音声を録音し、文字を返す
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("=== 何か、話しかけてください ===")
        audio = r.listen(source)
        print("=== ここまでの音声を録音しました ===")
        text = r.recognize_google(audio, language="ja-JP", show_all=True)
        if len(text) == 0:
            print("良く聞き取れませんでした")
            return ""
        print(text["alternative"][0]["transcript"])
        return text["alternative"][0]["transcript"]


if __name__ == "__main__":
    record_and_to_text()
