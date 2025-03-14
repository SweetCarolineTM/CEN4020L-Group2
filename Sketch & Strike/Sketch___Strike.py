# Other game file imports
import sys
from Button import Button
from PasswordBox import PasswordBox
from GameFunctions import *
from Network import Network # type: ignore

# Library imports
import pygame
#import pymunk

pygame.init()
window_width = 800
window_height = 600
size_of_square = 50
fps = 120
display = pygame.display.set_mode((window_width, window_height))
# This is necessary for when we implement physics but it was being buggy so I commented it out
# space = pymunk.space()
pygame.display.set_caption("Sketch & Strike")

win = pygame.display.set_mode((window_width , window_height))


def main():
    
    # Variable Initialization
    running = True
    n = Network()
    
    hostGamePressed, joinGamePressed, settingsPressed = False, False, False
    #x, y = 100, 100
    
    pygame.init()
    window_width = 800
    window_height = 600
    size_of_square = 50
    fps = 120
    display = pygame.display.set_mode((window_width, window_height))
    # This is necessary for when we implement physics but it was being buggy so I commented it out
    # space = pymunk.space()
    pygame.display.set_caption("Sketch & Strike")

    window = pygame.display.set_mode((window_width , window_height))
    
    # Object Initialization
    """passwordBox = PasswordBox(250, 250, 300, 50, pygame.Color("gray"), pygame.font)
    hostButton = Button(300, 200, 200, 60, "Host Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('hostGamePressed', True))
    joinButton = Button(300, 300, 200, 60, "Join Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('joinGamePressed', True))
    settingsButton = Button(300, 400, 200, 60, "Settings", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('settingsPressed', True))
    buttons = [hostButton, joinButton, settingsButton]"""


    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))
    clock = pygame.time.Clock()

    while running:

        #for button in buttons:
        #   button.handle_event(event)

        """password = passwordBox.handle_event(event)  
        if password is not None:  # Return on Enter press
            if (hostGamePressed == True):
                hostGamePressed = False
                hostGame(password)
            elif (joinGamePressed == True):
                joinGamePressed = False
                joinGame(password)"""
        
        clock.tick(fps)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()


        # Checks variables for current "screen" and displays accordingly
        """if (hostGamePressed == True or joinGamePressed == True):
            passwordBox.draw(display)  
        elif (settingsPressed == True):
            # Create a function in GameFunctions.py to handle settings
            pass
        else:
            for button in buttons:
                button.draw(display)"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        p.move()
        redrawWindow(window, p, p2)

    pygame.quit()
    sys.exit()

main()