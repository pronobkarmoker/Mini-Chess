def load_image(file_path):
    """Load an image from the specified file path."""
    import pygame
    try:
        image = pygame.image.load(file_path)
        return image.convert_alpha()  # Convert for faster blitting
    except pygame.error as e:
        print(f"Unable to load image at {file_path}: {e}")
        return None

def check_valid_move(piece, start_pos, end_pos, board):
    """Check if the move is valid for the given piece."""
    # Placeholder for actual move validation logic
    return True  # This should be replaced with actual logic

def handle_user_input():
    """Handle user input for moving pieces."""
    import pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        # Additional input handling logic can be added here
    return True