import random
import tkinter as tk
from PIL import Image,ImageTk

# 表示文字配列
kondate = ['うどん','カレー','とんかつ','そば','親子丼','パスタ','お好み焼き','オムライス','チャーハン','ラーメン']
# 画像配列
file = ['udon.jpg','kare-.jpeg','tonnkatu.jpeg','soba.jpg','oyakodon.jpg','pasuta.jpg','okonomiyaki.jpg','omuraisu.jpg','tya-han.jpg','ra-men.jpg']

# ボタンの処理
def startButton():
    randomResult = random.choice(kondate)
    # ラベルの変更
    label.configure(text=randomResult,font=('',50))
    # ボタン変更
    button.configure(text='最初へ戻る',font=('',50),command=title)
    # 画像変更
    canvas.itemconfig(canvasImage,image=fileList[kondate.index(randomResult)])

# 「最初へ戻る」のボタン処理 
def title():
    label.configure(text='本日の献立',font=('',50))
    button.configure(text='start',font=('',50),command=startButton)
    canvas.itemconfig(canvasImage,image=cooking)
# ウィンドウの作成
display = tk.Tk()
# ウィンドウのタイトル
display.title('献立アプリ')
# 画面サイズ
display.geometry('800x700')
# 画面表示領域
canvas = tk.Canvas(bg='white',width=780,height=520)
canvas.place(x=0,y=200)
# ラベル
label = tk.Label(text='本日の献立',font=('',50))
# ボタン
button = tk.Button(text='start',font=('',50),command=startButton)
# ラベル配置
label.pack()
# ボタン配置
button.pack()
# 画面取得・リサイズ
def openAndResize(item):
    images = Image.open(item)
    image_risize = ImageTk.PhotoImage(images.resize(size=(750,500)))
    return image_risize
# 初期画像
cooking = openAndResize('osara.jpg')
canvasImage = canvas.create_image(10,0,image=cooking,anchor=tk.NW)
# 画像のオブジェクト格納配列
fileList = []
# 画像ファイルを格納
for name in file:
    obj = openAndResize(name)
    fileList.append(obj)

display.mainloop()