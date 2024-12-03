from settings import *
import random

class Block(pygame.sprite.Sprite): # For the sprite of the object
    def __init__(self, tetro, pos):
        self.tetro = tetro
        self.pos = vec(pos) + INIT_OFFSET
        self.alive = True


        # Set the sprite
        super().__init__(tetro.tetris.sprites)
        self.image = tetro.image
        # self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        # pygame.draw.rect(self.image, tetro.color, (1, 1, TILE_SIZE - 2, TILE_SIZE - 2), border_radius=8)
        self.rect = self.image.get_rect()

    # Remove dead bocks
    def is_alive(self):
        if not self.alive:
            self.kill()

    # Rotate the object 90 degrees
    def rotate(self, pivot_pos):
        return (self.pos - pivot_pos).rotate(90) + pivot_pos

    # Return a bool of if the block is in a valid position
    def is_collide(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and (y < 0 or (y < FIELD_H and not self.tetro.tetris.field[y][x])):
            return False
        return True

    def set_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_pos()

class Tetro:
    def __init__(self, tetris):
        self.tetris = tetris
        self.type = random.choice(list(SHAPES.keys()))
        self.image = random.choice(tetris.game.image)
        self.grounded = False
        self.shape = [Block(self, pos) for pos in SHAPES[self.type]]


    def rotate(self):
        pivot_pos = self.shape[0].pos
        new_pos = [block.rotate(pivot_pos) for block in self.shape]

        if not self.is_collide(new_pos):
            for i, block in enumerate(self.shape):
                block.pos = new_pos[i]

    def is_collide(self, block_pos):
        # Use a map to determine if there are any blocks in the shape colliding
        for block, pos in zip(self.shape, block_pos):
            if block.is_collide(pos):
                return True
        return False

    # move the shape
    def move(self, direction):
        move_direction = DIRECTION_KEYS[direction]
        new_pos = [block.pos + move_direction for block in self.shape]


        # Check if the new pos are valid
        if not self.is_collide(new_pos):
            for block in self.shape:
                block.pos += move_direction
        elif direction == 'D':
            self.tetris.speed_up = False
            self.grounded = True

    def update(self):
        self.move('D')