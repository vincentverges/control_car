import pygame
from robot_hat import Servo, PWM
import time

pygame.init()
screen = pygame.display.set_mode((100,100))

# servo0 = Servo("P0")
motor3_pwm = Servo("P3")

angle_motor = 0
motor3_pwm.angle(angle_motor)
motor_state = 'stop'

# angle = 0
# servo0.angle(angle)

def adjust_servo_angle(new_angle):
	servo0.angle(new_angle)
	print(f"Angle: {new_angle}°")	
	return new_angle
	
def adjust_motor_speed(new_angle_motor, new_state):
	global angle_motor, motor_state
	if motor_state != new_state:
		angle_motor = new_angle_motor
		motor3_pwm.angle(new_angle_motor)
		motor_state = new_state
		print(f"Motor State: {new_state}, Motor Pulse Width: {new_angle_motor}")	


running = True
print("Utiliser les fleches du clavier pour controler le Servo et le Moteur")
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	keys = pygame.key.get_pressed()

#	if keys[pygame.K_RIGHT]:
#		angle = adjust_servo_angle(min(90, angle + 1))
#	elif keys[pygame.K_LEFT]:
#		angle = adjust_servo_angle(max(-90, angle - 1))
#	else:
#		if angle != 0:
#			angle = adjust_servo_angle(0)
	
	if keys[pygame.K_UP]:
		adjust_motor_speed(90, 'forward')
	elif keys[pygame.K_DOWN]:
		if motor_state == 'forward' or motor_state == "stop":
			adjust_motor_speed(-90, 'backward')
		else:
			adjust_motor_speed(0, 'stop')
	else:
		if motor_state != 'stop':
			adjust_motor_speed(0, 'stop')
		
	time.sleep(0.001)
		
pygame.quit()

