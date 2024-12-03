import sys

from settings import *
from tetris import Tetris
import pathlib

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode(WIN_RES)
        self.clock = pygame.time.Clock()

        # Animation timer setup: will display movement after ANIM_TIME has passed
        self.user_event = pygame.USEREVENT + 0
        self.anim_flag = False
        pygame.time.set_timer(self.user_event, ANIM_TIME)

        self.image = self.load_image()

        self.tetris = Tetris(self)

    # load sprites for falling tetris blocks
    def load_image(self):
        files = [item for item in pathlib.Path(SPRITE_PATH).rglob('*.png') if item.is_file()]
        images = [pygame.image.load(file).convert_alpha() for file in files]
        images = [pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images

    # Read player inputs
    def check_events(self):
        self.anim_flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif self.tetris.prompt.active:
                self.tetris.prompt.handle_event(event)
            elif event.type == pygame.KEYDOWN:
                self.tetris.shift(event.key)
            elif event.type == self.user_event:
                self.anim_flag = True

    # The update the status of objects (location and collision)
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    # draw grid and sprites
    def draw(self):
        self.screen.fill(color=EXTEND_BG_COLOR)
        self.screen.fill(color=BG_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        pygame.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()