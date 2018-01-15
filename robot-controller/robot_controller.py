from guizero import *
from gpiozero import Robot

robot = Robot((2, 3), (4, 5))

app = App("Robot controller", layout="grid")

Text(app, "Left", grid=[0, 0])
left = Slider(app, start=100, end=-100, grid=[1, 0], horizontal=False)
right = Slider(app, start=100, end=-100, grid=[2, 0], horizontal=False)
Text(app, "Right", grid=[3, 0])

def scaled(slider):
    while True:
        yield slider.value / 100

robot.source = zip(scaled(left), scaled(right))

app.display()
