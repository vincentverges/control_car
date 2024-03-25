import pygame
from robot_hat import Servo
import time

pygame.init()
screen = pygame.display.set_mode((100, 100))

motor3_pwm = Servo("P3")
angle_motor = 0  # Angle initial du moteur

def adjust_motor_speed(new_angle_motor):
    motor3_pwm.angle(new_angle_motor)
    print(f"Motor Pulse Width: {new_angle_motor}")

running = True
print("Maintenir la flèche 'Haut' pour accélérer le moteur")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    key_pressed = False  # Flag pour indiquer si une touche est pressée

    if keys[pygame.K_UP]:
        key_pressed = True
        if angle_motor < 80:  # Augmenter l'angle seulement s'il est inférieur à 90
            angle_motor += 1
        adjust_motor_speed(angle_motor)  # Maintenir la vitesse maximale si angle_motor est à 90
    elif keys[pygame.K_DOWN]:
        key_pressed = True
        if angle_motor > -80:  # Diminuer l'angle seulement s'il est supérieur à -90
            angle_motor -= 1
        adjust_motor_speed(angle_motor)

    if not key_pressed:
        # Arrêter progressivement le moteur si aucune touche n'est pressée
        if angle_motor > 0:
            angle_motor -= 1
        elif angle_motor < 0:
            angle_motor += 1
        adjust_motor_speed(angle_motor)

    time.sleep(0.01)  # Un petit délai pour contrôler la vitesse de changement d'angle et la réactivité

pygame.quit()
