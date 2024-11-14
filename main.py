import sys

from settings import *
from tetris import Tetris

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode(FIELD_RES)
        self.clock = pygame.time.Clock()
        self.tetris = Tetris(self)

    # To read player inputs
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    # The update the status of objects
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    # draw objects
    def draw(self): # visual representation of objects
        self.screen.fill(color=COLOR)
        self.tetris.draw()
        pygame.display.flip() # corrects orientation

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()