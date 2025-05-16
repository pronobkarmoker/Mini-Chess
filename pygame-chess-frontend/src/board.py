import pygame

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board_size = 8
        self.square_size = 60
        self.colors = [(255, 255, 255), (0, 0, 0)]  # White and Black

    def draw(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = self.colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color, 
                                 (col * self.square_size, row * self.square_size, 
                                  self.square_size, self.square_size))

    def reset(self):
        # Logic to reset the board to its initial state can be added here
        pass