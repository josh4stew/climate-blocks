import sys

from settings import *
from tetris import Tetris

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode(FIELD_RES)
        self.clock = pygame.time.Clock()

        # Animation timer setup: will display movement after ANIM_TIME has passed
        self.user_event = pygame.USEREVENT + 0
        self.anim_flag = False
        pygame.time.set_timer(self.user_event, ANIM_TIME)

        self.tetris = Tetris(self)

    # To read player inputs
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
        self.screen.fill(color=BG_COLOR)
        self.tetris.draw()
        # corrects orientation
        pygame.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()