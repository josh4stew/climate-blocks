from settings import *
import math
from tetro import Tetro

class Tetris:
    def __init__(self, app):
        self.app = app
        self.tetro = Tetro(self)
        self.sprites = pygame.sprite.Group()

    def create_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE) # the size of each rectangle
                pygame.draw.rect(self.app.screen, "white", rect, 1)


    def update(self):
        self.tetro.update()
        self.sprites.update()

    def draw(self):
        self.create_grid()
        self.sprites.draw(self.app.screen)