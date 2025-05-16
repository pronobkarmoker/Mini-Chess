import pygame

PIECE_COLORS = {
    'white': (220, 220, 220),
    'black': (50, 50, 50)
}

PIECE_LABELS = {
    'Pawn': 'P',
    'Rook': 'R',
    'Knight': 'N',
    'Bishop': 'B',
    'Queen': 'Q',
    'King': 'K'
}

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self, screen, square_size):
        row, col = self.position
        center = (col * square_size + square_size // 2, row * square_size + square_size // 2)
        pygame.draw.circle(screen, PIECE_COLORS[self.color], center, square_size // 2 - 8)
        font = pygame.font.SysFont(None, square_size // 2)
        label = PIECE_LABELS[self.__class__.__name__]
        text = font.render(label, True, (0, 0, 0) if self.color == 'white' else (255, 255, 255))
        text_rect = text.get_rect(center=center)
        screen.blit(text, text_rect)

    def move(self, new_position):
        self.position = new_position

class Pawn(Piece): pass
class Rook(Piece): pass
class Knight(Piece): pass
class Bishop(Piece): pass
class Queen(Piece): pass
class King(Piece): pass