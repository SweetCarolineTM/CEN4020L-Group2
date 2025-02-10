#other files
from Button import Button
from PasswordBox import PasswordBox
from GameFunctions import AskPassword, MainMenu, PlayerMovement
import Server
import Client

#libraries
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

passwordBox = PasswordBox(250, 250, 300, 50, pygame.Color("gray"), pygame.font)
hostButton = Button(300, 200, 200, 60, "Host Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: AskPassword(display, passwordBox))
joinButton = Button(300, 300, 200, 60, "Join Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: AskPassword(display, passwordBox))
buttons = [hostButton, joinButton]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for button in buttons:
            button.handle_event(event)

    

    display.fill((255, 255, 255))


    #change button events so that when clicked it just changes a variable
    #then if that variable is true, display the password box instead of the main menu
    MainMenu(display, buttons)

    PlayerMovement(display, x, y, speed, window_height, window_width, size_of_square)

    # Update the display/space and maintain fps
    pygame.display.flip()
    clock.tick(fps)
    # space.step(1/fps)

pygame.quit()
sys.exit()


