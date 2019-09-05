import board
import time
import pulseio
import touchio
from adafruit_motor import servo

# create pwmout object on D9
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
# create a servo object My_servo
touch_A5 = touchio.TouchIn(board.A5)
touch_A4 = touchio.TouchIn(board.A4)
my_servo = servo.Servo(pwm)
angle = 5

while True:
    if touch_A5.value:

        if angle < 180:
            angle = angle + 5
        my_servo.angle = angle
        time.sleep(0.05)
        print(angle)

    if touch_A4.value:
        if angle > 0:
            angle = angle - 5
        my_servo.angle = angle
        time.sleep(0.05)
        print(angle)