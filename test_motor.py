import pygame
from robot_hat import PWM
import time

pygame.init()
screen = pygame.display.set_mode((100, 100))

# Initialisation du moteur à charbon
motor_pwm = PWM("P3")  # Assurez-vous que le port "P3" est correct
motor_pwm.freq(1000)  # Définit une fréquence de base pour le PWM, à ajuster selon besoin

# Définition des largeurs d'impulsion pour avancer, arrêter et reculer
PWM_FORWARD = 2500  # À ajuster
PWM_STOP = 1500     # À ajuster
PWM_BACKWARD = 500 # À ajuster

def adjust_motor_speed(pwm_value):
    motor_pwm.pulse_width(pwm_value)
    print(f"Motor PWM: {pwm_value}")

running = True
print("Utiliser les flèches 'Haut' et 'Bas' pour contrôler le moteur à charbon")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        adjust_motor_speed(PWM_FORWARD)
    elif keys[pygame.K_DOWN]:
        adjust_motor_speed(PWM_BACKWARD)
    else:
        adjust_motor_speed(PWM_STOP)

    time.sleep(0.01)  # Ajustez ce délai selon les besoins de votre application

pygame.quit()
