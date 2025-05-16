import pygame
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board_size = 8
        self.square_size = 60
        self.colors = [(255, 255, 255), (0, 0, 0)]  # White and Black
        self.pieces = []
        self.selected_piece = None  # Track selected piece
        self.setup_pieces()

    def setup_pieces(self):
        self.pieces = []
        # Pawns
        for col in range(8):
            self.pieces.append(Pawn('white', (6, col)))
            self.pieces.append(Pawn('black', (1, col)))
        # Rooks
        self.pieces.append(Rook('white', (7, 0)))
        self.pieces.append(Rook('white', (7, 7)))
        self.pieces.append(Rook('black', (0, 0)))
        self.pieces.append(Rook('black', (0, 7)))
        # Knights
        self.pieces.append(Knight('white', (7, 1)))
        self.pieces.append(Knight('white', (7, 6)))
        self.pieces.append(Knight('black', (0, 1)))
        self.pieces.append(Knight('black', (0, 6)))
        # Bishops
        self.pieces.append(Bishop('white', (7, 2)))
        self.pieces.append(Bishop('white', (7, 5)))
        self.pieces.append(Bishop('black', (0, 2)))
        self.pieces.append(Bishop('black', (0, 5)))
        # Queens
        self.pieces.append(Queen('white', (7, 3)))
        self.pieces.append(Queen('black', (0, 3)))
        # Kings
        self.pieces.append(King('white', (7, 4)))
        self.pieces.append(King('black', (0, 4)))

    def draw(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = self.colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color, 
                                 (col * self.square_size, row * self.square_size, 
                                  self.square_size, self.square_size))
        # Highlight selected piece
        if self.selected_piece:
            row, col = self.selected_piece.position
            highlight_color = (0, 255, 0)
            pygame.draw.rect(self.screen, highlight_color,
                             (col * self.square_size, row * self.square_size,
                              self.square_size, self.square_size), 4)
        for piece in self.pieces:
            piece.draw(self.screen, self.square_size)

    def get_piece_at(self, pos):
        for piece in self.pieces:
            if piece.position == pos:
                return piece
        return None

    def handle_click(self, mouse_pos):
        col = mouse_pos[0] // self.square_size
        row = mouse_pos[1] // self.square_size
        clicked_pos = (row, col)
        piece = self.get_piece_at(clicked_pos)
        if self.selected_piece:
            # If clicked on another of your own pieces, select it
            if piece and piece != self.selected_piece:
                self.selected_piece = piece
            else:
                # Move selected piece to empty square or capture
                self.move_piece(self.selected_piece, clicked_pos)
                self.selected_piece = None
        else:
            if piece:
                self.selected_piece = piece

    def move_piece(self, piece, new_pos):
        # Remove any captured piece
        target = self.get_piece_at(new_pos)
        if target and target != piece:
            self.pieces.remove(target)
        piece.move(new_pos)

    def reset(self):
        self.setup_pieces()
        self.selected_piece = None