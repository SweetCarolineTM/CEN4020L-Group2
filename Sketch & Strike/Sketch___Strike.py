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
#import pymunk

def main():
    # Variable Initialization 
    pygame.init()
    window_width = 800
    window_height = 600
    fps = 120
    # This is necessary for when we implement physics but it was being buggy so I commented it out
    #space = pymunk.space()
    pygame.display.set_caption("Sketch & Strike")
    window = pygame.display.set_mode((window_width , window_height))
    clock = pygame.time.Clock()
    public_ip = requests.get("https://api64.ipify.org?format=text").text

    #this will display the main menu, then try to host or join a game
    #when the game is over or if it fails to connect, it will restart the loop and return to the main menu
    
    # result = -1(conn failed), 0 (tie), 1(1 won), 2(2 won)
    while True:
        ip, port, status = mainMenu(window, clock, fps)

        if status == "hostGame":
            result = hostGame(window, clock, fps, public_ip, port)
            #joinGame(window,clock,fps,ip,port) #beucase this is getting the ip and address from mainMenu, so we need to get this info from server class

        elif status == "joinGame":
            result = joinGame(window, clock, fps, ip, port)

        if result == -1:
            continue  # If connection failed, return to menu
main()

pygame.quit()
sys.exit()