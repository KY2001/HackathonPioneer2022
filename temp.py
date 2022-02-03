# 本体
from record_and_to_text import *
from play_and_text_to_speech import *

executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

while True:
    text = executor.submit(record_and_to_text)
    text = text.result()
    if "音楽" in text or "流" in text:
        executor.submit(auto_speech, "音楽を再生します。")
        time.sleep(2.2)
        executor.submit(play, os.path.dirname(__file__) + "/music_35.mp3")
        time.sleep(2.2)
        executor.submit(auto_speech, "お母様はこのアーティスト、お好きでしたよね")

    if "バンド" in text or "名前" in text:
        executor.submit(auto_speech, "このアーティストはスピッツです。")

    if "昨日" in text or "ゴルフ" in text:
        executor.submit(auto_speech, "お父様の昨日の目的地は銀座です。")

    if "やましい" in text:
        executor.submit(auto_speech, "そういえば、明日は特別な日だったような気がします。お母様、グローブボックスを開けてください。")
