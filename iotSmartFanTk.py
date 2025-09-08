# -*- coding: utf-8 -*-
# iotSmartFanTk.py (Tkinter simulation for Smart Fan)

import Tkinter as tk     # Python2 Tkinter
from temperatureSensor import TemperatureSensor

# Fan simulation logic
TEMP_MIN = 20
TEMP_MAX = 45
DUTY_MIN = 20
DUTY_MAX = 100

def calcFanDuty(temp):
    if temp < TEMP_MIN:
        return 0
    if temp > TEMP_MAX:
        temp = TEMP_MAX
    duty_step = (DUTY_MAX - DUTY_MIN) / float(TEMP_MAX - TEMP_MIN)
    return DUTY_MIN + duty_step * (temp - TEMP_MIN)

# Create a fake temperature sensor
sensor = TemperatureSensor("sim", {"gpio": 3})

# GUI update loop
def update_values():
    temp = sensor.readValue()  # use your fake sensor
    duty = round(calcFanDuty(temp), 2)

    lbl_temp.config(text="Temperature: {} C".format(temp))
    lbl_duty.config(text="Fan Duty: {} %".format(duty))

    root.after(2000, update_values)  # update every 2 seconds

# GUI setup
root = tk.Tk()
root.title("IoT Smart Fan Simulation")

lbl_title = tk.Label(root, text="Smart Fan Controller", font=("Arial", 16, "bold"))
lbl_title.pack(pady=10)

lbl_temp = tk.Label(root, text="Temperature: -- C", font=("Arial", 14))
lbl_temp.pack(pady=5)

lbl_duty = tk.Label(root, text="Fan Duty: -- %", font=("Arial", 14))
lbl_duty.pack(pady=5)

# Start updates
update_values()

root.mainloop()

