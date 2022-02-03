import PySimpleGUI as sg
import record_and_to_text as r2t

sg.theme('DarkAmber')  # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [[sg.Button('実行'), sg.Button('キャンセル')],
          [sg.MLine(key='-ML1-' + sg.WRITE_ONLY_KEY, size=(20, 10))]
          ]

# ウィンドウの生成
window = sg.Window('サンプルプログラム', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == '実行':
        text = r2t.record_and_to_text()
        window['-ML1-' + sg.WRITE_ONLY_KEY].print(text)

window.close()