import pygame
from robot_hat import Servo
import time

pygame.init()
screen = pygame.display.set_mode((100, 100))

motor3_pwm = Servo("P3")

angle_motor = 0
motor3_pwm.angle(angle_motor)

def adjust_motor_speed(new_angle_motor):
    motor3_pwm.angle(new_angle_motor)
    print(f"Motor Pulse Width: {new_angle_motor}")

running = True
print("Utiliser les flèches 'Haut' et 'Bas' pour contrôler le moteur")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    motor_changed = False
    
    while keys[pygame.K_UP]:
        angle_motor = min(90, angle_motor + 1) 
        motor_changed = True
        adjust_motor_speed(angle_motor)

    while keys[pygame.K_DOWN]:
        angle_motor = max(-90, angle_motor - 1)
        motor_changed = True
        adjust_motor_speed(angle_motor)
    else:
        angle_motor = 0
        adjust_motor_speed(angle_motor)
    
    time.sleep(0.0001)
        
pygame.quit()
