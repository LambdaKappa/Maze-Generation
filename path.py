import pygame as pg
import numpy as np

from settings import *
from maps import *
from cell import generate_maze

pg.init()

new_map = create_map(generate_maze(MAP_SIZE_Y // 3,  MAP_SIZE_X // 3), data)
path = get_path(new_map, data.path_start, data.path_end)

class Application:
	def __init__(self):
		self.screen = pg.display.set_mode(RES)
		self.map = new_map
		self.is_running = False
		self.time = 0
		self.elements_per_frame = 90
		self.elements_drawn = 0

		pg.display.set_caption("Maze Generator")

	def start(self):
		self.is_running = True
		while self.is_running:
			self.event_check()
			self.update()
			self.draw()
		self.on_exit()

	def event_check(self):
		for event in pg.event.get():
			if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
				self.is_running = False

	def update(self):
		pass

	def draw(self):
		if self.time < 16:
			self.screen.fill(BACKGROUND)
		self.draw_map()
		pg.display.flip()

		dt = pg.time.Clock().tick(FPS)
		self.time += dt

	def draw_map(self):
		(size_x, size_y) = (WIDTH // MAP_SIZE_X, HEIGHT // MAP_SIZE_Y)
		dx = (WIDTH - ((WIDTH // MAP_SIZE_X) * MAP_SIZE_X)) / 2
		dy = (HEIGHT - ((HEIGHT // MAP_SIZE_Y) * MAP_SIZE_Y)) / 2
		if self.time < 16:
			shape_y, shape_x = self.map.shape
			for y in range(shape_y):
				for x in range(shape_x):
					color = WHITE if self.map[y, x].traversable else BLACK
					pg.draw.rect(self.screen, color, (dx + x * size_x, dy + y * size_y, size_x, size_y))

		elements_max = min(len(path), self.elements_drawn + self.elements_per_frame)
		if self.elements_drawn < len(path):
			for y, x in path[self.elements_drawn:elements_max]:
				pg.draw.rect(self.screen, (255, 0, 0), (dx + x * size_x, dy + y * size_y, size_x, size_y))
			self.elements_drawn += self.elements_per_frame

		pg.draw.rect(self.screen, (0, 255, 0), (dx + data.path_start[1] * size_x, dy + data.path_start[0] * size_y, size_x, size_y))
		pg.draw.rect(self.screen, (0, 0, 255), (dx + data.path_end[1] * size_x, dy + data.path_end[0] * size_y, size_x, size_y))

	def on_exit(self):
		pg.quit()

if __name__ == "__main__":
	application = Application()
	application.start()
	exit()
