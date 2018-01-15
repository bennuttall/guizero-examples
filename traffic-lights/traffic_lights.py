from guizero import App, Text, PushButton
from gpiozero import TrafficLights

lights = TrafficLights(22, 27, 17)

app = App("Traffic Lights controller", layout="grid")

Text(app, "Red", grid=[0, 0])
PushButton(app, command=lights.red.on, text="on", grid=[1, 0])
PushButton(app, command=lights.red.off, text="off", grid=[2, 0])
PushButton(app, command=lights.red.blink, text="blink", grid=[3, 0])

Text(app, "Amber", grid=[0, 1])
PushButton(app, command=lights.red.on, text="on", grid=[1, 1])
PushButton(app, command=lights.red.off, text="off", grid=[2, 1])
PushButton(app, command=lights.red.blink, text="blink", grid=[3, 1])

Text(app, "Green", grid=[0, 2])
PushButton(app, command=lights.red.on, text="on", grid=[1, 2])
PushButton(app, command=lights.red.off, text="off", grid=[2, 2])
PushButton(app, command=lights.red.blink, text="blink", grid=[3, 2])

Text(app, "All", grid=[0, 3])
PushButton(app, command=lights.red.on, text="on", grid=[1, 3])
PushButton(app, command=lights.red.off, text="off", grid=[2, 3])
PushButton(app, command=lights.red.blink, text="blink", grid=[3, 3])

app.display()
