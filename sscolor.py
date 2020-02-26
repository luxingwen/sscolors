from tkinter import *
import random
import time
import threading

colors = [
    [
      "#ffffff",
      "#84dcc6",
      "#a5ffd6",
      "#ffa69e",
      "#ff686b"
    ],
    [
      "#ef476f",
      "#ffd166",
      "#06d6a0",
      "#118ab2",
      "#073b4c"
    ],
    [
      "#f2d7ee",
      "#d3bcc0",
      "#a5668b",
      "#69306d",
      "#0e103d"
    ],
    [
      "#ffbe0b",
      "#fb5607",
      "#ff006e",
      "#8338ec",
      "#3a86ff"
    ],
    [
      "#ffac81",
      "#ff928b",
      "#fec3a6",
      "#efe9ae",
      "#cdeac0"
    ],
    [
      "#011627",
      "#fdfffc",
      "#2ec4b6",
      "#e71d36",
      "#ff9f1c"
    ],
    [
      "#03256c",
      "#2541b2",
      "#1768ac",
      "#06bee1",
      "#ffffff"
    ],
    [
      "#f7b267",
      "#f79d65",
      "#f4845f",
      "#f27059",
      "#f25c54"
    ],
    [
      "#4b6e70",
      "#97b5ac",
      "#718f86",
      "#d4ded4",
      "#a9b0cb"
    ],
    [
      "#a7c6da",
      "#c3957d",
      "#bd5f70",
      "#dcd9f8",
      "#cbb38c"
    ],
    [
      "#ffbe0b",
      "#fb5607",
      "#ff006e",
      "#8338ec",
      "#3a86ff"
    ],
    [
      "#283d3b",
      "#197278",
      "#edddd4",
      "#c44536",
      "#772e25"
    ],
    [
      "#ffe74c",
      "#ff5964",
      "#ffffff",
      "#6bf178",
      "#35a7ff"
    ]
]

def getRandomColor():
    index = random.randint(0, len(colors)) - 1
    length = len(colors[index])
    return colors[index][random.randint(0, length - 1)]

def drawSquares(cv, x, y, size):
  cv.create_rectangle(x, y, x + size, y + size, fill =  getRandomColor());
  cv.create_rectangle(x + 10, y + 10, x + size - 10, y + size - 10, fill = getRandomColor());
  cv.create_rectangle(x + 20, y + 20, x + size - 20, y + size - 20, fill = getRandomColor());
  cv.create_rectangle(x + 30, y + 20, x + size - 30, y + size - 30, fill = getRandomColor());
  cv.pack()

def draw(cv, w, h):
    size = 40
    x = 0
    while x < w + size:
        y = 0
        while y < h + size:
            drawSquares(cv, x, y, size)
            y += size
        x += size

def reset(cv):
    cv.delete()

def loop():
    while True:
        draw(cv, width, height)
        reset(cv)

root = Tk()
root.attributes("-fullscreen", True)
width = 1920
height = 1080
cv = Canvas(root, bg = 'white', width = width, height = height)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
root.mainloop()