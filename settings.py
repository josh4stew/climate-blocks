import pygame

FPS = 60
# background color
BG_COLOR = "black"
# Block colors
COLOR = "orange", "cyan", "purple", "red", "blue", "green", "yellow"

# A 2D vector to manage the position of the blocks on the screen
vec = pygame.math.Vector2

TILE_SIZE = 50
FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

# The inital offset is set for the top middle of the screen
INIT_OFFSET = vec(FIELD_W // 2, 0)

# Value for the time interval in milliseconds
ANIM_TIME = 150

# The key is the direction the value is how much it is moved
DIRECTION_KEYS = {'L' : vec(-1, 0), 'R': vec(1, 0), 'D': vec(0, 1)}

# Shape layouts, the first block is always the pivot point for rotations
SHAPES = {
    'O': [(0, 0), (0, -1), (1,-1), (1, 0)],
    'I': [(0, 0), (0, -1), (0, 1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (0, -1), (-1, -1), (1, 0)],
    'L': [(0, 0), (0, -1), (0, -2), (1, 0)],
    'J': [(0, 0), (0, -1), (0, -2), (-1, 0)],
    'T': [(0, 0), (0, -1), (1, -1), (-1, -1)]
}

QUESTIONS = [
    ('A)', "This is my question about climate change A) Right answer, B) Wrong answer, C) Wrong answer"),
    ('B)', "This is my question about climate change A) Wrong answer, B) Right answer, C) Wrong answer"),
    ('C)', "This is my question about climate change A) Wrong answer, B) Wrong answer, C) Right answer")
]