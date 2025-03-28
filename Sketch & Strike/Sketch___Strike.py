# Other game file imports
import sys
from Button import Button
from PasswordBox import PasswordBox
from GameFunctions import *
from Network import Network # type: ignore

# Library imports
import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
window_width = 800
window_height = 600
size_of_square = 50
fps = 120
display = pygame.display.set_mode((window_width, window_height))

# This is necessary for when we implement physics but it was being buggy so I commented it out
# space = pymunk.space()

# Pymunk setup for physics?
space = pymunk.Space()
space.gravity = (0, 980)    # Add gravity if we want
draw_options = pymunk.pygame_util.DrawOptions(display)


pygame.display.set_caption("Sketch & Strike")

win = pygame.display.set_mode((window_width , window_height))

# Basic Terrain Creation function
def create_terrain(space):
    """Create initial terrain boundaries and obstacles."""
    static_lines = [
        pymunk.Segment(space.static_body, (50, 500), (750, 500), 5),    # Ground
        pymunk.Segment(space.static_body, (50, 50), (50, 500), 5),    # Left Wall
        pymunk.Segment(space.static_body, (750, 50), (750, 500), 5),    # Right Wall
    ]
    for line in static_lines:
        line.elasticity = 0.5
        line.friction = 0.8
        space.add(line)

# Destroy Terrain function
def destroy_terrain(x, y, radius):
    """Destroy terrain by drawing over it and removing collision."""
    pygame.draw.circle(win, (255, 255, 255), (x, y), radius)    # Erase with white
    # Optional: Remove Pymunk objects if needed

# Draw function
def draw_shape(x, y, shape_type="circle"):
    """Draw shapes to modify terrain."""
    if shape_type == "circle":
        pygame.draw.circle(win, (0, 0, 255), (x, y), 20)    # Blue circle
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Circle(body, 20, (0, 0))
        shape.elasticity = 0.4
        shape.friction = 0.9
        body.position = (x, y)
        space.add(body, shape)

# Weapon function
def weapon_impact(weapon_pos):
    """Handle weapon impact and modify terrain."""
    x, y = weapon_pos
    destroy_terrain(x, y, 30)    # Destroy terrain on weapon hit

def main():
    
    # Variable Initialization
    running = True
    n = Network()
    
    hostGamePressed, joinGamePressed, settingsPressed = False, False, False
    #x, y = 100, 100
    
    # pygame.init()
    # window_width = 800
    # window_height = 600
    # size_of_square = 50
    # fps = 120
    # display = pygame.display.set_mode((window_width, window_height))
    # This is necessary for when we implement physics but it was being buggy so I commented it out
    # space = pymunk.space()
    # pygame.display.set_caption("Sketch & Strike")

    window = pygame.display.set_mode((window_width , window_height))
    
    # Create initial terrain
    create_terrain(space)
    
    # Object Initialization
    """passwordBox = PasswordBox(250, 250, 300, 50, pygame.Color("gray"), pygame.font)
    hostButton = Button(300, 200, 200, 60, "Host Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('hostGamePressed', True))
    joinButton = Button(300, 300, 200, 60, "Join Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('joinGamePressed', True))
    settingsButton = Button(300, 400, 200, 60, "Settings", pygame.Color("gray"), pygame.Color("darkgray"), lambda: globals().__setitem__('settingsPressed', True))
    buttons = [hostButton, joinButton, settingsButton]"""


    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))
    # add lines
    space.add(p.body, p.shape)
    space.add(p2.body, p2.shape)
    
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

            # Handle terrain drawing or weapon actions
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if event.button == 1:    # Left-click to add shapes
                    draw_shape(x, y, "circle")
                elif event.button == 3:    # Right-click to destroy terrain
                    destroy_terrain(x, y, 30)

        p.move()
        # update movement
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        # p2.x, p2.y = p2Pos     # Check this line and 2 above
        p2.update()
        
        redrawWindow(window, p, p2)
        # update physics
        space.step(1 / 120.0)    # pymunk physics step
        space.debug_draw(draw_options)
        

    pygame.quit()
    sys.exit()

main()
