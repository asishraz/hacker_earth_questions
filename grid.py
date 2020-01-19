import pygame 

class Grid:
	def __init__(self):
		self.grid_lines = [((0,200),(600,200)),
		((0,400),(600,400)),
		((200,0),(200,600)),
		((400,0),(400,600))]


	def draw(self, surface):
		for event in self.grid_lines:
			pygame.draw.line(surface,(200,200,200),event[0],event[1])