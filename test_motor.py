from robot_hat import PWM
import time

# Initialisation de l'objet PWM pour le moteur
motor_pwm = PWM("P3")  # Assurez-vous que "P3" est le port correct

# Réglage de la fréquence du signal PWM, qui est commune pour les contrôles de moteurs à courant continu
motor_pwm.freq(1000)  # Exemple: 1000 Hz

def set_motor_speed(pulse_width):
    # Réglage de la largeur d'impulsion pour contrôler la vitesse du moteur
    # La valeur doit être ajustée en fonction des spécifications de votre moteur et du contrôleur
    motor_pwm.pulse_width(pulse_width)

# Exemple d'utilisation pour faire tourner le moteur à une vitesse définie par la largeur d'impulsion
set_motor_speed(1500)  # Exemple de valeur, à ajuster
time.sleep(4)  # Faire tourner le moteur pendant 4 secondes
set_motor_speed(0)  # Arrêter le moteur
