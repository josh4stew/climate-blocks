from settings import *
from tetro import Tetro
from question import Prompt

class Tetris:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.sprites = pygame.sprite.Group()
        # Field keeps track of blocks placed in the field
        self.field = [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]
        self.tetro = Tetro(self)
        self.ask_question = False
        self.prompt = Prompt(self.game)

    def drop_in_field(self):
        for block in self.tetro.shape:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field[y][x] = block

    # If the row is filled then destroy it and move the blocks down
    def check_rows(self):
        # Start from the bottom-most row and move upward
        for y in range(FIELD_H - 1, -1, -1):
            # Check if the row is completely filled
            if all(self.field[y][x] for x in range(FIELD_W)):
                # Mark blocks in this row as dead and clear the row
                for x in range(FIELD_W):
                    self.field[y][x].alive = False  # Assuming blocks have an `alive` attribute
                    self.field[y][x] = 0

                # Shift rows down
                for move_y in range(y, 0, -1):
                    for x in range(FIELD_W):
                        self.field[move_y][x] = self.field[move_y - 1][x]
                        if self.field[move_y][x]:
                            self.field[move_y][x].pos = vec(x, move_y)

                # Clear the top row
                for x in range(FIELD_W):
                    self.field[0][x] = 0

                self.prompt.active = True

                break  # Only handle one row per frame


    def check_grounded(self):
        if self.tetro.grounded:
            self.drop_in_field()
            self.tetro = Tetro(self)

    # Create the background grid
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE) # the size of each rectangle
                pygame.draw.rect(self.game.screen, "white", rect, 1)

    # shift the block left or right
    def shift(self, key):
        if key == pygame.K_LEFT or key == pygame.K_a:
            self.tetro.move('L')
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.tetro.move('R')
        elif key == pygame.K_UP or key == pygame.K_s:
            self.tetro.rotate()

    def update(self):
        if self.game.anim_flag and not self.prompt.active:
            self.check_rows()
            self.tetro.update()
            self.check_grounded()
            self.sprites.update()

    def draw(self):
        if self.prompt.active:
            self.prompt.draw()
        else:
            self.draw_grid()
            self.sprites.draw(self.game.screen)