import pygame
from robot_hat import Servo, PWM
import time

pygame.init()
screen = pygame.display.set_mode((100,100))

servo0 = Servo("P0")

angle = 0
servo0.angle(angle)

def adjust_servo_angle(new_angle):
	servo0.angle(new_angle)
	print(f"Angle: {new_angle}°")	
	return new_angle



running = True
print("Utiliser les fleches du clavier pour controler le Servo et le Moteur")
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		angle = adjust_servo_angle(min(90, angle + 1))
	elif keys[pygame.K_RIGHT]:
		angle = adjust_servo_angle(max(-90, angle - 1))
	else:
		if angle != 0:
			angle = adjust_servo_angle(0)
		
	time.sleep(0.001)
		
pygame.quit()

