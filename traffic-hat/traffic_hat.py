from guizero import *
from gpiozero import TrafficHat
from threading import Thread

th = TrafficHat(pwm=True)

app = App("Traffic HAT controller", layout="grid")

def scaled(v):
    return v / 100

def update_lights():
    while True:
        yield (scaled(red.value), scaled(amber.value), scaled(green.value))

def update_button():
    while True:
        button_pressed.value = th.button.value
        button_held.value = th.button.is_held

Text(app, "Lights", grid=[0, 1])
Text(app, "Red", grid=[1, 0])
red = Slider(app, start=100, end=0, grid=[1, 1], horizontal=False)
Text(app, "Amber", grid=[2, 0])
amber = Slider(app, start=100, end=0, grid=[2, 1], horizontal=False)
Text(app, "Green", grid=[3, 0])
green = Slider(app, start=100, end=0, grid=[3, 1], horizontal=False)

Text(app, "Buzzer", grid=[0, 2])
PushButton(app, command=th.buzzer.on, text="on", grid=[1, 2])
PushButton(app, command=th.buzzer.off, text="off", grid=[2, 2])
PushButton(app, command=th.buzzer.beep, text="beep", grid=[3, 2])

Text(app, "Button", grid=[0, 3])
button_pressed = CheckBox(app, "Pushed", grid=[1, 3])
button_held = CheckBox(app, "Held", grid=[2, 3])

th.lights.source = update_lights()

thread = Thread(target=update_button)
thread.start()

app.display()
