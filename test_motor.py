import pygame
from robot_hat import Servo, PWM, TTS
import time

motor = Servo('P1')
#motor.pulse_width(2500)
#time.sleep(4)
#motor.pulse_width(1500)
motor.angle(0)
time.sleep(1)
motor.angle(90)
time.sleep(3)
motor.angle(0)
time.sleep(1)
motor.angle(0)
time.sleep(1)
motor.angle(-90)
time.sleep(3)
motor.angle(0)

print("Test fini")