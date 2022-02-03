# 本体
from record_and_to_text import *
from play_and_text_to_speech import *

text = record_and_to_text()

if "音楽" in text or "流" in text:
    auto_speech("音楽を再生します。")
    play("music.mp3")

if "バンド" in text or "名前" in text:
    auto_speech("このアーティストはスピッツです。")

if "昨日" in text or "ゴルフ" in text:
    auto_speech("お父様の昨日の目的地は銀座です。")

if "やましい" in text:
    auto_speech("お母様、グローブボックスを開けてください。")
