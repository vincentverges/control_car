from robot_hat import PWM
import time

# Initialiser l'objet PWM sur le canal connecté à l'ESC
# Remplacez "P0" par le bon canal en fonction de votre configuration
esc_pwm = PWM("P3")

# Définir la fréquence du signal PWM
# La fréquence typique pour les ESC est de 50 Hz, mais cela peut varier
# Vérifiez la documentation de votre ESC spécifique
esc_pwm.freq(50)

def set_esc_speed(pulse_width):
    # Configurer la largeur d'impulsion pour l'ESC
    # La valeur typique pour l'arrêt est de 1500 (neutre pour beaucoup d'ESC)
    # Les valeurs doivent être ajustées au-dessus ou en dessous pour accélérer ou inverser
    esc_pwm.pulse_width(pulse_width)

try:
    # Démarrage de l'ESC (peut nécessiter une procédure de démarrage spécifique, vérifiez la documentation de votre ESC)
    set_esc_speed(1500)  # Valeur neutre pour initialiser
    time.sleep(1)

    # Exemple : accélérer
    set_esc_speed(2500)  # Valeur d'exemple pour accélérer, à ajuster
    time.sleep(4)

    # Retour à la vitesse neutre
    set_esc_speed(1500)
    time.sleep(1)

    # Exemple : inverser
    set_esc_speed(500)  # Valeur d'exemple pour inverser, à ajuster
    time.sleep(4)

    # Arrêt du moteur
    set_esc_speed(1500)

except KeyboardInterrupt:
    # Assurez-vous d'arrêter le moteur en cas d'interruption
    set_esc_speed(1500)
    print("Arrêt du programme.")

