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

    if keys[pygame.K_UP]:
        angle_motor += 1  # Augmenter l'angle pour accélérer
        angle_motor = min(angle_motor, 90)  # Limiter l'angle maximal à 90
        adjust_motor_speed(angle_motor)
    elif keys[pygame.K_DOWN]:
        angle_motor -= 1  # Diminuer l'angle pour ralentir
        angle_motor = max(angle_motor, -180)  # Limiter l'angle minimal à -180
        adjust_motor_speed(angle_motor)
    else:
        # Optionnel : arrêter progressivement le moteur si aucune touche n'est pressée
        if angle_motor > 0:
            angle_motor -= 1
        elif angle_motor < 0:
            angle_motor += 1
        adjust_motor_speed(angle_motor)

    time.sleep(0.01)  # Un petit délai pour contrôler la vitesse de changement d'angle et la réactivité

pygame.quit()
