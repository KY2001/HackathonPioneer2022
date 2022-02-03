import PySimpleGUI as sg
import concurrent.futures
import record_and_to_text as r2t
from text_compere import *

sg.theme('DarkAmber')  # デザインテーマの設定
# ウィンドウに配置するコンポーネント
layout = [[sg.Button('実行'), sg.Button('キャンセル')],
          [sg.MLine(key='-ML1-' + sg.WRITE_ONLY_KEY, size=(40, 10))],
          [sg.MLine(key='-ML2-' + sg.WRITE_ONLY_KEY, size=(40, 10))]
          ]
# ウィンドウの生成
window = sg.Window('お話スムーサー', layout)
# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    if event == '実行':
        text = r2t.record_and_to_text()
        text2 = judge_text(text)
        window['-ML1-' + sg.WRITE_ONLY_KEY].print(text)
        window['-ML2-' + sg.WRITE_ONLY_KEY].print(text2)

window.close()