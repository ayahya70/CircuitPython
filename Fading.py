# A Yahya
# Fading LED
# This code makes an led wired to a pwm pin fade in and out, rythmicly


import time
import board
import pulseio
led = pulseio.PWMOut(board.D9, frequency=5000, duty_cycle=0)

while True:
    for i in range(100): #what this do?
        led.duty_cycle = int(i / 100 * 65535)
        time.sleep(0.01)
    for i in range(100, -1, -1):
        led.duty_cycle = int(i / 100 * 65535)
        time.sleep(0.01).
