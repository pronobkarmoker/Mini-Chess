class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self, surface):
        pass  # Implement drawing logic for the piece

    def move(self, new_position):
        self.position = new_position


class Pawn(Piece):
    def draw(self, surface):
        pass  # Implement drawing logic for the Pawn


class Rook(Piece):
    def draw(self, surface):
        pass  # Implement drawing logic for the Rook


class Knight(Piece):
    def draw(self, surface):
        pass  # Implement drawing logic for the Knight


class Bishop(Piece):
    def draw(self, surface):
        pass  # Implement drawing logic for the Bishop


class Queen(Piece):
    def draw(self, surface):
        pass  # Implement drawing logic for the Queen


class King(Piece):
    def draw(self, surface):
        pass  # Implement drawing logic for the King