import pygame

class PasswordBox:
    def __init__(self, x, y, width, height, color, font, mask_char="*"):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.font = font
        self.text = ""
        self.mask_char = mask_char
        self.active = False

    def draw(self, screen):
        """Draw the input box and the text inside it."""
        # Draw the input box
        pygame.draw.rect(screen, self.color, self.rect, 2)
        
        # Mask password and render text
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.mask_char * len(self.text), True, pygame.Color("black"))
        
        # Draw the text
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True  # Activate input mode
            else:
                self.active = False  # Deactivate input mode

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return self.text  # Return entered password
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode  # Add typed character
