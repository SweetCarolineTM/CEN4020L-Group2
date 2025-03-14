# Other game file imports
from Button import Button
from PasswordBox import PasswordBox
from Player import Player
from Network import Network # type: ignore
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
    while True:
        ip, port, status = mainMenu(window, clock, fps)

        if status == "hostGame":
            result = hostGame(window, clock, fps, public_ip, port)

            #use this to display the result of the game or just go back to main menu if the connection failed
            """
            if result == -1:
                pass
                #connection failed
            elif result == 0:
                pass
                #it was a tie
            elif result == 1:
                pass
                #player 1 won
            elif result == 2:
                pass
                #player 2 won
            """
        elif status == "joinGame":
            result = joinGame(window, clock, fps, ip, port)

            #use this to display the result of the game or just go back to main menu if the connection failed
            """
            if result == -1:
                pass
                #connection failed
            elif result == 0:
                pass
                #it was a tie
            elif result == 1:
                pass
                #player 1 won
            elif result == 2:
                pass
                #player 2 won
            """

main()

pygame.quit()
sys.exit()