from phue import Bridge
from guizero import *
from time import sleep

b = None
while not b:
    try:
        b = Bridge('192.168.86.37')
    except:
        print("Press the bridge button")
        sleep(1)
lights = list(b.lights)

def light_switches(light_number, on=True):
    light = lights[int(light_number)]
    def light_switch():
        light.on = on
    return light_switch

def dimmer_switches(light_number):
    light = lights[int(light_number)]
    def dimmer_switch(value):
        light.brightness = int(value)
    return dimmer_switch

app = App(title="hueizero", layout="grid")

for x, light in enumerate(lights):
    Text(app, light.name, grid=[x, 0]),
    PushButton(app, command=light_switches(x, on=True), text="on", grid=[x, 1]),
    PushButton(app, command=light_switches(x, on=False), text="off", grid=[x, 2]),
    Slider(app, start=0, end=255, command=dimmer_switches(x),
        grid=[x, 3], horizontal=False
    )

app.display()
