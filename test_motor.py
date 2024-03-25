import robot_hat
from robot_hat import PWM
import time

# Initialisation
pwm_motor = PWM("P1")  # Assumer que "P0" est le canal pour le moteur

# Configurer la fréquence PWM pour le servo et le moteur
pwm_motor.freq(60)  # La fréquence peut devoir être ajustée selon vos composants

# Valeurs initiales
motor_speed = 400  # Valeur neutre pour l'ESC

def update_motor(speed):
    pwm_motor.pulse_width(speed)
    print(f"Vitesse du moteur: {speed}")

try:
    while True:
        # Ici, vous pouvez lire les entrées de l'utilisateur, par exemple, en utilisant `input()`
        # ou une autre méthode pour obtenir des commandes en temps réel
        
        # Exemple pour augmenter la vitesse du moteur
        motor_speed += 10  # Augmenter la valeur pour accélérer
        update_motor(motor_speed)
        
        time.sleep(1)  # Attente d'une seconde entre les mises à jour
        
except KeyboardInterrupt:
    # Arrêt propre du programme
    pwm_motor.pulse_width(400)  # Envoyer un signal neutre à l'ESC pour arrêter le moteur
    print("Arrêt du programme.")
