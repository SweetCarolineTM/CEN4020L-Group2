
import pygame
import pymunk
import sys

#pygame and window initialization
pygame.init()
window_width = 800
window_height = 600
size_of_square = 50
fps = 120
display = pygame.display.set_mode((window_width, window_height))
# space = pymunk.space()
pygame.display.set_caption("Sketch & Strike")
clock = pygame.time.Clock()



# Main game loop
running = True

x, y = 100, 100
speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y <= window_height - size_of_square:
        y += speed
    if keys[pygame.K_LEFT] and x >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x <= window_width - size_of_square:
        x += speed

    display.fill((255, 255, 255))

    pygame.draw.rect(display, (0, 128, 255), pygame.Rect(x, y, size_of_square, size_of_square))

    # Update the display/space and maintain fps
    pygame.display.flip()
    clock.tick(fps)
    # space.step(1/fps)

pygame.quit()
sys.exit()


