from robot_hat import PWM
import time

# Initialisation de l'objet PWM pour le moteur
motor_pwm = PWM("P3")  # Remplacez "P3" par le bon port pour votre moteur
motor_pwm.freq(1000)  # Réglage de la fréquence du PWM, peut nécessiter des ajustements

# Définition des largeurs d'impulsion pour faire tourner le moteur et pour l'arrêter
PWM_RUN = 2000  # Largeur d'impulsion pour faire tourner le moteur, à ajuster selon les besoins
PWM_STOP = 1500  # Largeur d'impulsion pour arrêter le moteur, souvent autour de 1500 pour un arrêt neutre

# Fonction pour faire tourner le moteur
def run_motor(duration, pwm_value):
    motor_pwm.pulse_width_time(pwm_value)  # Définit la largeur d'impulsion pour faire tourner le moteur
    time.sleep(duration)  # Laisse le moteur tourner pendant la durée spécifiée

# Fonction pour arrêter le moteur
def stop_motor():
    motor_pwm.pulse_width_time(PWM_STOP)  # Réinitialise la largeur d'impulsion pour arrêter le moteur

# Test: Fait tourner le moteur pendant 5 secondes puis l'arrête
run_motor(5, PWM_RUN)
stop_motor()

print("Test terminé.")
