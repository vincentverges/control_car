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

def get_key_state():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        return "UP"
    elif keys[pygame.K_DOWN]:
        return "DOWN"
    else:
        return "NONE"

running = True
print("Maintenir la flèche 'Haut' pour accélérer le moteur")

last_key_state = "NONE"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_state = get_key_state()

    if key_state == "UP":
        if angle_motor < 90:
            angle_motor += 1  # Augmente progressivement jusqu'à 90
    elif key_state == "DOWN":
        if angle_motor > -90:
            angle_motor -= 1  # Diminue progressivement jusqu'à -90
    else:
        # Si aucune touche n'est pressée, réduire progressivement l'angle à 0
        if angle_motor > 0:
            angle_motor -= 1
        elif angle_motor < 0:
            angle_motor += 1

    if key_state != last_key_state or key_state == "NONE":
        adjust_motor_speed(angle_motor)  # Ajuste la vitesse du moteur

    last_key_state = key_state  # Mémorise l'état de la touche pour la prochaine itération

    time.sleep(0.01)  # Délai pour une mise à jour fluide

pygame.quit()
