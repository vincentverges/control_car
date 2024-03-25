import pygame
from robot_hat import Servo, PWM, TTS
import time

motor = PWM('P1')
motor.pulse_width(2500)
time.sleep(4)
motor.pulse_width(1500)



