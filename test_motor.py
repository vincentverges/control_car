import pygame
from robot_hat import Servo, PWM, TTS
import time

pygame.init()
screen = pygame.display.set_mode((100,100))

# Initialize TTS class
tts = TTS(lang='en-US')
# Speak text
tts.say("What the fuck")
# show all supported languages
print(tts.supported_lang())

