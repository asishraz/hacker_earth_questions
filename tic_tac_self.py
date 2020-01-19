import pygame
from grid import Grid


surface = pygame.display.set_mode((600,600))

grid = Grid()
running = 1

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False







	surface.fill((0,0,0))
	grid.draw(surface)
	pygame.display.flip()
