import pygame
import random

# 게임 설정
pygame.init()
screen_width = 300
screen_height = 600
block_size = 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# 색상 정의
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (128, 0, 128)
]

# 블록 모양 정의
shapes = [
    [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']],

    [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']],

    [['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']],

    [['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....']],

    [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
]

class Block:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation % len(self.shape)]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in locked_positions:
                color = locked_positions[(x, y)]
                grid[y][x] = color
    return grid

def draw_grid(surface, grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[y][x], (x * block_size, y * block_size, block_size, block_size), 0)
    draw_grid_lines(surface)

def draw_grid_lines(surface):
    for y in range(20):
        pygame.draw.line(surface, (128, 128, 128), (0, y * block_size), (screen_width, y * block_size))
    for x in range(10):
        pygame.draw.line(surface, (128, 128, 128), (x * block_size, 0), (x * block_size, screen_height))

def draw_window(surface, grid):
    surface.fill((0, 0, 0))
    draw_grid(surface, grid)
    pygame.display.update()

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_block = False
    run = True
    current_block = Block(5, 0, random.choice(shapes))
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        grid = create_grid(locked_positions)
        fall_speed = 0.27
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_block.y += 1
            if not (valid_space(current_block, grid)) and current_block.y > 0:
                current_block.y -= 1
                change_block = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_block.x -= 1
                    if not valid_space(current_block, grid):
                        current_block.x += 1
                if event.key == pygame.K_RIGHT:
                    current_block.x += 1
                    if not valid_space(current_block, grid):
                        current_block.x -= 1
                if event.key == pygame.K_DOWN:
                    current_block.y += 1
                    if not valid_space(current_block, grid):
                        current_block.y -= 1
                if event.key == pygame.K_UP:
                    current_block.rotate()
                    if not valid_space(current_block, grid):
                        current_block.rotate()

        shape_pos = convert_shape_format(current_block)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = colors[current_block.color]

        if change_block:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = colors[current_block.color]
            current_block = Block(5, 0, random.choice(shapes))
            change_block = False

            if check_lost(locked_positions):
                run = False

        draw_window(screen, grid)

def valid_space(block, grid):
    accepted_positions = [[(x, y) for x in range(10) if grid[y][x] == (0, 0, 0)] for y in range(20)]
    accepted_positions = [x for item in accepted_positions for x in item]

    formatted = convert_shape_format(block)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def convert_shape_format(block):
    positions = []
    format = block.shape[block.rotation % len(block.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '.':
                continue
            if column == '0':
                positions.append((block.x + j, block.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

main()