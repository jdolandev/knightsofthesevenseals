import random
import os, sys
import pygame

def main():
	#initialize screen
	pygame.init()
	screen = pygame.display.set_mode((150,50))
	pygame.display.set_caption("Knights of the Seven Seals")

	#Background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0,0,0))

	#Display Text
	font = pygame.font.Font(None,36)
	text = font.render("Hello World!", 1,(10,10,10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text,textpos)

	#Blit everything to screen
	screen.blit(background,(0,0))
	pygame.disply.flip()

	#Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
		screen.blit(background,(0,0))
		pygame.display.flip

if __name__=='__main__': main()
