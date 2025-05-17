def load_image(file_path):
    """Load an image from the specified file path."""
    import pygame
    try:
        image = pygame.image.load(file_path)
        return image.convert_alpha()  # Convert for faster blitting
    except pygame.error as e:
        print(f"Unable to load image at {file_path}: {e}")
        return None

def check_valid_move(piece, new_pos, pieces, board=None):
    row, col = piece.position
    new_row, new_col = new_pos
    dr, dc = new_row - row, new_col - col

    # Prevent moving to the same square
    if (row, col) == (new_row, new_col):
        return False

    # Prevent capturing own piece
    for p in pieces:
        if p.position == (new_row, new_col) and p.color == piece.color:
            return False

    name = piece.__class__.__name__

    if name == "Pawn":
        direction = -1 if piece.color == "white" else 1
        start_row = 6 if piece.color == "white" else 1
        # Move forward
        if dc == 0:
            if dr == direction and not any(p.position == (new_row, new_col) for p in pieces):
                return True
            # Double move from start
            if row == start_row and dr == 2 * direction and not any(
                p.position == (row + direction, col) or p.position == (new_row, new_col) for p in pieces
            ):
                return True
        # Capture
        if abs(dc) == 1 and dr == direction:
            if any(p.position == (new_row, new_col) and p.color != piece.color for p in pieces):
                return True
            # En passant
            if board and board.en_passant_target == (new_row, new_col):
                return True
        return False

    if name == "Rook":
        if dr == 0 or dc == 0:
            step_r = (dr > 0) - (dr < 0)
            step_c = (dc > 0) - (dc < 0)
            r, c = row + step_r, col + step_c
            while (r, c) != (new_row, new_col):
                if any(p.position == (r, c) for p in pieces):
                    return False
                r += step_r
                c += step_c
            return True
        return False

    if name == "Knight":
        return (abs(dr), abs(dc)) in [(2, 1), (1, 2)]

    if name == "Bishop":
        if abs(dr) == abs(dc):
            step_r = (dr > 0) - (dr < 0)
            step_c = (dc > 0) - (dc < 0)
            r, c = row + step_r, col + step_c
            while (r, c) != (new_row, new_col):
                if any(p.position == (r, c) for p in pieces):
                    return False
                r += step_r
                c += step_c
            return True
        return False

    if name == "Queen":
        if dr == 0 or dc == 0 or abs(dr) == abs(dc):
            step_r = (dr > 0) - (dr < 0) if dr != 0 else 0
            step_c = (dc > 0) - (dc < 0) if dc != 0 else 0
            r, c = row + step_r, col + step_c
            while (r, c) != (new_row, new_col):
                if any(p.position == (r, c) for p in pieces):
                    return False
                r += step_r
                c += step_c
            return True
        return False

    if name == "King":
        # Normal king move
        if max(abs(dr), abs(dc)) == 1:
            return True
        # Castling
        if not hasattr(piece, 'has_moved') or piece.has_moved:
            return False
        if dr == 0 and abs(dc) == 2 and board:
            rook_col = 0 if dc == -2 else 7
            rook = board.get_piece_at((row, rook_col))
            if not rook or rook.color != piece.color or not hasattr(rook, 'has_moved') or rook.has_moved:
                return False
            # Check squares between king and rook are empty
            step = -1 if dc < 0 else 1
            for c in range(col + step, rook_col, step):
                if board.get_piece_at((row, c)):
                    return False
            # (You can add check detection here for full rules)
            return True

    return False

def handle_user_input():
    """Handle user input for moving pieces."""
    import pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        # Additional input handling logic can be added here
    return True