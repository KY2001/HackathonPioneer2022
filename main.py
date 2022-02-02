# 本体
from record_and_to_text import *
from play_and_text_to_speech import *

text = record_and_to_text()
whday = 0
trivia = 0
theme = 0
maxtr = 2
maxwh = 2
maxth = 2

"""
if "音楽" in text and "流" in text:
  #音楽を流す
elif "話題" in text and "ない" in text:
  if
"""

if "今日" in text and "何" in text:
    if whday == 0:
        # 今日は大豆の日です
        auto_speech("今日は大豆の日です")
        whday += 1
    elif whday == 1:
        # 今日は乳酸菌の日です
        auto_speech("今日は乳酸菌の日です")
        whday += 1
    elif whday == 2:
        # 今日は英雄の日です
        print("今日は英雄の日です")
        whday = 0
    if trivia < maxwh:
        whday += 1

""""
  else : whday = 0
elif "何か" in text and "教えて" in text:
  if trivia == 0:
    #シロクマはだいたい左利き
  elif trivia == 1:
    #カタツムリには歯がしこたまある
  elif trivia ==2 :
    #カビバラはウサインボルトよりはやい
  if trivia < maxtr:
    trivia +=1
  else : trivia = 0
  """
