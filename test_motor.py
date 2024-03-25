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
    
    if keys[pygame.K_UP]:
        angle_motor = min(90, angle_motor + 1) 
        motor_changed = True
    elif keys[pygame.K_DOWN]:
        angle_motor = max(-90, angle_motor - 1)
        motor_changed = True
    
    if not motor_changed and angle_motor != 0:
        angle_motor -=5 if angle_motor>0 else -5
        angle_motor = max(min(angle_motor, 90), -90)
    
    adjust_motor_speed(angle_motor) 
    
    time.sleep(0.001)
        
pygame.quit()
