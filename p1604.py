import pygame
import sys
from pygame.locals import *

pygame.init()
size = width, height = 800, 600
bg = (255, 255, 255)
speed = [0, 0]

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

pygame.display.set_caption('First time')

turtle = pygame.image.load('20161024144619_FLXfK.gif')

position = turtle.get_rect()
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				speed = [-1, 0]
				turtle = l_head
			if event.key == K_RIGHT:
				speed = [1, 0]
				turtle = r_head
			if event.key == K_UP:
				speed = [0, -1]
			if event.key == K_DOWN:
				speed = [0, 1]
	
	position = position.move(speed)
	if position.left < 0 or position.right > width:
		turtle = pygame.transform.flip(turtle, True, False)
		speed[0] = -speed[0]
	if position.top < 0 or position.bottom > height:
		speed[1] = -speed[0]
	screen.fill(bg)
	screen.blit(turtle, position)
	pygame.display.flip()
	clock.tick(30)
		
			