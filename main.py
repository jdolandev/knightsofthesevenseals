import random
import os, sys
import pygame

inventory=[]
dead= False
location = "town"

#Equipment
iHead = None
iArmR = None
iArmL = None
iChest = None
iLegs = None
iShoes = None

screen = pygame.display.set_mode((640,480),32,0)

pygame.init()
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	pygame.display.update()