import pygame
import sys
from board import Board

# Constants
WIDTH, HEIGHT = 480, 480  # 8x8 board, 60px per square

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Chess Board")

board = Board(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            board.handle_click(event.pos)

    board.draw()
    pygame.display.flip()