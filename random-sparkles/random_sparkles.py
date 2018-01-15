from guizero import App, Text, Slider
from sense_emu import SenseHat  # or use sense_emu
from random import randint
from threading import Thread

sense = SenseHat()
app = App("Random Sparkles", width=170, height=150, layout="grid")

def values():
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, rs.value)
    g = randint(0, gs.value)
    b = randint(0, bs.value)
    return x, y, r, g, b

def update_display():
    while True:
        sense.set_pixel(*values())

low = 1
high = 255

Text(app, "R", grid=[0, 0])
rs = Slider(app, start=low, end=high, grid=[0, 1], horizontal=False)
rs.value = high
Text(app, "G", grid=[1, 0])
gs = Slider(app, start=low, end=high, grid=[1, 1], horizontal=False)
gs.value = high
Text(app, "B", grid=[2, 0])
bs = Slider(app, start=low, end=high, grid=[2, 1], horizontal=False)
bs.value = high

t = Thread(target=update_display)
t.start()

app.display()
