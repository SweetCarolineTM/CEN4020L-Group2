# Other game file imports
from Button import Button
from PasswordBox import PasswordBox
from Player import Player
from GameFunctions import *
from Text import Text

# Library imports
import sys
import pygame
import requests
import pymunk
import pymunk.pygame_util

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
    pygame.init()
    window_width = 800
    window_height = 600
    fps = 120
    pygame.display.set_caption("Sketch & Strike")
    window = pygame.display.set_mode((window_width , window_height))
    clock = pygame.time.Clock()
    public_ip = requests.get("https://api64.ipify.org?format=text").text

    # Pymunk setup for physics?
    space = pymunk.Space()
    space.gravity = (0, 980)    # Add gravity if we want
    draw_options = pymunk.pygame_util.DrawOptions(display)

    #this will display the main menu, then try to host or join a game
    #when the game is over or if it fails to connect, it will restart the loop and return to the main menu
    
    # result = -1(conn failed), 0 (tie), 1(1 won), 2(2 won)
    # running = True
    while True:
        ip, port, status = mainMenu(window, clock, fps)

        if status == "hostGame":
            result = hostGame(window, clock, fps, public_ip, port)
            #joinGame(window,clock,fps,ip,port) #beucase this is getting the ip and address from mainMenu, so we need to get this info from server class

        elif status == "joinGame":
            result = joinGame(window, clock, fps, ip, port)

        if result == -1:
            continue  # If connection failed, return to menu

        # Game logic after successful connection
        # Create initial terrain
        create_terrain(space)

        p = Player(100, 100, 100, 100, (0, 255, 0))
        p2 = Player(200, 100, 100, 100, (255, 0, 0))
        space.add(p.body, p.shape)
        space.add(p2.body, p2.shape)

        in_game = True
        while in_game:
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
                    # running = False
                    pygame.quit()
                    sys.exit()

                # Handle terrain drawing or weapon actions
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if event.button == 1:    # Left-click to add shapes
                        draw_shape(x, y, "circle")
                    elif event.button == 3:    # Right-click to destroy terrain
                        destroy_terrain(x, y, 30)

            p.move()
            p2.update()

            redrawWindow(window, p, p2)
            # update physics
            space.step(1 / 120.0)    # pymunk physics step
            space.debug_draw(draw_options)

main()

pygame.quit()
sys.exit()
