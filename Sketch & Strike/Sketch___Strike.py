# Other game file imports
from Button import Button
from PasswordBox import PasswordBox
from GameFunctions import *
from Server import hostGame
from Client import joinGame

# Library imports
import pygame
#import pymunk
import sys
from Client import Network

# Pygame and window initialization
pygame.init()
window_width = 800
window_height = 600
size_of_square = 50
fps = 120
display = pygame.display.set_mode((window_width, window_height))
# This is necessary for when we implement physics but it was being buggy so I commented it out
# space = pymunk.space()
pygame.display.set_caption("Sketch & Strike")
clock = pygame.time.Clock()

# Variable Initialization
running = True
hostGamePressed, joinGamePressed, settingsPressed = False, False, False
#x, y = 100, 100
#speed = 5

n = Network()

startPos = read_pos(n.getPos())
p1 = Player(startPos[0],startPos[1],100,100,(0,255,0))
p2 = Player(0,0,100,100,(255,0,0))
#p1 = Player(display,startPos[0],startPos[1],speed, window_height, window_width, size_of_square)
#p2 = Player(display,0,0,speed, window_height, window_width, size_of_square)



# Object Initialization
passwordBox = PasswordBox(250, 250, 300, 50, pygame.Color("gray"), pygame.font)
hostButton = Button(300, 200, 200, 60, "Host Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('hostGamePressed', True))
joinButton = Button(300, 300, 200, 60, "Join Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('joinGamePressed', True))
settingsButton = Button(300, 400, 200, 60, "Settings", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('settingsPressed', True))
buttons = [hostButton, joinButton, settingsButton]


# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for button in buttons:
            button.handle_event(event)

        password = passwordBox.handle_event(event)  
        if password is not None:  # Return on Enter press
            if (hostGamePressed == True):
                hostGamePressed = False
                hostGame(password)
            elif (joinGamePressed == True):
                joinGamePressed = False
                joinGame(password)

    display.fill((255, 255, 255))

    clock.tick(60)
    p2Pos = read_pos(n.send(make_pos((p1.x, p1.y))))
    p2.x = p2Pos[0]
    p2.y = p2Pos[1]
    p2.update()
    # Checks variables for current "screen" and displays accordingly
    if (hostGamePressed == True or joinGamePressed == True):
        passwordBox.draw(display)  
    elif (settingsPressed == True):
        # Create a function in GameFunctions.py to handle settings
        pass
    else:
        for button in buttons:
            button.draw(display)


    p1.move()
    redrawWindow( p1, p2)

    # Update the display/space and maintain fps
    #pygame.display.flip()
    clock.tick(fps)
    # space.step(1/fps)

pygame.quit()
sys.exit()


