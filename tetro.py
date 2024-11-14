from settings import *

class Block(pygame.sprite.Sprite): # for the sprite of the object
    def __init__(self, tetro, pos):
        self.tetro = tetro
        super().__init__()
        self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self. image.fill("orange")

        self.rect = self.image.get_rect()
        self.rect.topleft = pos[0] * TILE_SIZE, pos[1] * TILE_SIZE





class Tetro:
    def __init__(self, tetris):
        self.tetris = tetris
        Block(self, (4, 7))

    def update(self):
        pass