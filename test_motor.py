import pygame
from robot_hat import Servo, PWM, TTS
import time

pygame.init()
screen = pygame.display.set_mode((100,100))

motor = PWM('P1')
motor.freq(1000)

motor.pulse_width_percent(100)



