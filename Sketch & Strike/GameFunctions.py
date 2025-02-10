import Button

import pygame

def AskPassword(display, passwordBox):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Exit on close
            password = passwordBox.handle_event(event)  
            if password is not None:  # Return on Enter press
                return password  

        display.fill((255, 255, 255))  
        passwordBox.draw(display)  
        pygame.display.flip()  

def MainMenu(display, buttons):
    for button in buttons:
        button.draw(display)

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
