import pygame
import sys

# Constants
WIDTH, HEIGHT = 480, 480  # 8x8 board, 60px per square
SQUARE_SIZE = WIDTH // 8

# Colors
WHITE = (245, 245, 220)
BLACK = (139, 69, 19)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Chess Board")

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_board()
    pygame.display.flip()