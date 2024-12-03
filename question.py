from settings import *
from pygame import Rect
import random
import pygame.freetype

class Prompt:
    def __init__(self, game):
        self.game = game
        self.question = random.choice(QUESTIONS)
        self.font = pygame.font.Font(None, 50)
        self.extend_font = pygame.freetype.Font(FONT_PATH)
        self.menu_surface = pygame.Surface(FIELD_RES)
        self.menu_rect = self.menu_surface.get_rect(center=(FIELD_RES[0] // 2, FIELD_RES[1] // 2))

        # Define button dimensions and positions
        x_start = FIELD_RES[0] / 2.5
        button_width = TILE_SIZE*2
        spacing = TILE_SIZE
        offset = FIELD_RES[1] * 3 // 4
        button_height = TILE_SIZE
        self.highlight_button = 0

        self.buttons = [
            {"label": "A)", "rect": pygame.Rect(x_start - (button_width + spacing), offset, button_width, button_height)},
            {"label": "B)", "rect": pygame.Rect(x_start, offset, button_width, button_height)},
            {"label": "C)", "rect": pygame.Rect(x_start + (button_width + spacing), offset, button_width, button_height)},
        ]

        self.active = False

    # Wrap text inside a defined rectangle https://www.pygame.org/wiki/TextWrap
    def draw_question(self, surface, text, color, rect, font, aa=False, bkg=None):
        rect = Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Tg")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return

    def draw_extend_text(self):
        self.extend_font.render_to(self.game.screen, (WIN_W * 0.625, WIN_H * 0.02),
            text="CLIMATE", fgcolor='green',
            size=TILE_SIZE * 1.0, bgcolor='black')
        self.extend_font.render_to(self.game.screen, (WIN_W * 0.64, WIN_H * 0.049),
            text="BLOCKS", fgcolor='green',
            size=TILE_SIZE * 1.0, bgcolor='black')
        self.extend_font.render_to(self.game.screen, (WIN_W * 0.64, WIN_H * 0.20),
            text="level", fgcolor='orange',
            size=TILE_SIZE * 1.0, bgcolor='black')
        self.extend_font.render_to(self.game.screen, (WIN_W * 0.64, WIN_H * 0.30),
            text=str(self.game.tetris.level), fgcolor='white',
            size=TILE_SIZE * 1.8)
        self.extend_font.render_to(self.game.screen, (WIN_W * 0.64, WIN_H * 0.70),
            text="score", fgcolor='orange',
            size=TILE_SIZE * 1.0, bgcolor='black')
        self.extend_font.render_to(self.game.screen, (WIN_W * 0.64, WIN_H * 0.80),
            text=str(self.game.tetris.score), fgcolor='white',
            size=TILE_SIZE * 1.8)


    def draw(self):
        # Background of the menu
        self.menu_surface.fill("light gray")

        # draw the tetris blocks
        # self.game.tetris.sprites.draw(self.menu_surface)

        # Define the area for text
        rect = Rect(TILE_SIZE, TILE_SIZE, FIELD_RES[0]-TILE_SIZE, FIELD_RES[1] - TILE_SIZE*2)

        # Call the function to display the text
        self.draw_question(self.menu_surface, self.question[1], "black", rect, self.font)

        # Draw buttons
        for index, button in enumerate(self.buttons):
            color = "black"
            if index == self.highlight_button:
                color = "red"  # Highlight active button
            pygame.draw.rect(self.menu_surface, color, button["rect"])
            text = self.font.render(button["label"], True, "white")
            text_rect = text.get_rect(center=button["rect"].center)
            self.menu_surface.blit(text, text_rect)
        # Blit menu on the game screen
        self.game.screen.blit(self.menu_surface, self.menu_rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            # Navigate buttons with UP and DOWN arrows rotate with UP arrow
            if event.key == pygame.K_LEFT:
                self.highlight_button = (self.highlight_button - 1) % len(self.buttons)  # Wrap around
            elif event.key == pygame.K_RIGHT:
                self.highlight_button = (self.highlight_button + 1) % len(self.buttons)  # Wrap around
            elif event.key == pygame.K_UP:
                active_button = self.buttons[self.highlight_button]
                self.handle_button_click(active_button['label'])
                self.question = random.choice(QUESTIONS)
                self.active = False

    def handle_button_click(self, label):
        if label == self.question[0]:
            self.game.tetris.score += 100
        else:
            if not self.game.tetris.score - 50 < 0:
                self.game.tetris.score -= 50
