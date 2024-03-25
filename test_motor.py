from robot_hat import PWM
import time

# Initialisation de l'objet PWM pour le moteur
motor_pwm = PWM("P1")  # Remplacez "P3" par le bon port pour votre moteur

# Réglage de la fréquence du PWM (ajustez cette valeur en fonction de votre matériel)
motor_pwm.freq(1000)

def run_motor(direction, duration):
    if direction == "forward":
        pulse_width = 2500  # Marche avant
    elif direction == "backward":
        pulse_width = 500   # Marche arrière
    else:
        pulse_width = 1500  # Arrêt

    # Calcul du pourcentage de la largeur d'impulsion par rapport à la valeur maximale que nous utilisons (2500 dans cet exemple)
    pulse_width_percent = (pulse_width / 2500) * 100
    motor_pwm.pulse_width_percent(pulse_width_percent)

    print(f"Direction: {direction}, Pulse Width: {pulse_width}, Pulse Width Percent: {pulse_width_percent}%")
    time.sleep(duration)  # Laisse le moteur tourner pendant la durée spécifiée

def stop_motor():
    motor_pwm.pulse_width_percent(0)  # Arrêt du moteur
    print("Motor stopped.")

# Test: Fait tourner le moteur en marche avant pendant 2 secondes, puis en marche arrière pendant 2 secondes, et enfin l'arrête.
run_motor("forward", 2)
run_motor("backward", 2)
stop_motor()

print("Test du moteur terminé.")
