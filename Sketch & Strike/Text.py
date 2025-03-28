import pygame

class Text:
    def __init__(self, text, x, y, font_size=36, color=(0, 0, 0)):
        pygame.font.init()
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.render()

    def render(self):
        """Renders the text surface."""
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        """Draws the text on the screen."""
        screen.blit(self.text_surface, self.text_rect)

    def set_text(self, new_text):
        """Updates the text and re-renders it."""
        self.text = new_text
        self.render()