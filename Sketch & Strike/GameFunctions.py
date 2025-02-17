import Button
import pygame 

def PlayerMovement(display, x, y, speed, window_height, window_width, size_of_square):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y <= window_height - size_of_square:
        y += speed
    if keys[pygame.K_LEFT] and x >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x <= window_width - size_of_square:
        x += speed

    pygame.draw.rect(display, (0, 128, 255), pygame.Rect(x, y, size_of_square, size_of_square))

    return [x, y, speed]


# need an update method, to update the movements of each player?

"""
def update(self):
    self.rect(self.x,y,width,height) #translate this into window_h width etc
"""