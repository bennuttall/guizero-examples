from guizero import *
from gpiozero import TrafficHat

th = TrafficHat(pwm=True)

app = App("Traffic HAT controller", layout="grid")

def scaled(v):
    return v / 100

def update_lights():
    while True:
        yield (scaled(red.get()), scaled(amber.get()), scaled(green.get()))

Text(app, "Red", grid=[0, 0])
red = Slider(app, start=100, end=0, grid=[1, 0], orient="vertical")
Text(app, "Amber", grid=[0, 1])
amber = Slider(app, start=100, end=0, grid=[1, 1], orient="vertical")
Text(app, "Green", grid=[0, 2])
green = Slider(app, start=100, end=0, grid=[1, 2], orient="vertical")
Text(app, "Buzzer", grid=[0, 3])
PushButton(app, command=th.buzzer.on, text="on", grid=[1, 3])
PushButton(app, command=th.buzzer.off, text="off", grid=[2, 3])
PushButton(app, command=th.buzzer.beep, text="beep", grid=[3, 3])

th.lights.source = update_lights()

app.display()
