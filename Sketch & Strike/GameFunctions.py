import sys
import socket 
import pygame
import requests
from Button import Button
from Player import Player
from PasswordBox import PasswordBox
from Text import Text
from Network import Network

# game functionalities and player movement/info sending

def mainMenu(window, clock, fps):
    # Page Switching Function that buttons can call
    pageStatus = "mainMenu"
    def setPage(pageName):
        nonlocal pageStatus
        if pageStatus == "hostGame" or pageStatus == "joinGame":
            ipBox.text = ""
            portBox.text = ""
        pageStatus = pageName
    
    # Object Initialization
    hostButton = Button(300, 200, 200, 60, "Host Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: setPage("hostGame"))
    joinButton = Button(300, 300, 200, 60, "Join Game", pygame.Color("gray"), pygame.Color("darkgray"), lambda: setPage("joinGame"))
    settingsButton = Button(300, 400, 200, 60, "Settings", pygame.Color("gray"), pygame.Color("darkgray"), lambda: setPage("settings"))
    ipBox = PasswordBox(300, 200, 200, 60, pygame.Color("gray"), pygame.font, "IP: ")
    portBox = PasswordBox(300, 300, 200, 60, pygame.Color("gray"), pygame.font, "Port: ")
    backButton = Button(300, 400, 200, 60, "Back", pygame.Color("gray"), pygame.Color("darkgray"), lambda: setPage("mainMenu"))
    mainMenuButtons = [hostButton, joinButton, settingsButton]

    #main menu loop
    while True:
        # Event Handling to check for button presses and if an ip and/or port have been entered and submitted
        # The host only enters the port and then their ip is grabbed, while the client enters the host's ip and the port the host selected
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (pageStatus == "joinGame"):
                ip = ipBox.handle_event(event)
                port = portBox.handle_event(event)
                if ip is not None or port is not None:  # Return on Enter press
                    return [ipBox.text, portBox.text, pageStatus]
                backButton.handle_event(event)
            elif (pageStatus == "hostGame"):
                port = portBox.handle_event(event)
                if port is not None:
                    return [ipBox.text, portBox.text, pageStatus]
                backButton.handle_event(event)
            elif (pageStatus == "settings"):
                backButton.handle_event(event)
            else:
                for button in mainMenuButtons:
                    button.handle_event(event)

        # Checks variable for current "screen" and displays accordingly
        window.fill((255,255,255))
        if (pageStatus == "joinGame"):
            ipBox.draw(window)
            portBox.draw(window)
            backButton.draw(window)
        elif (pageStatus == "hostGame"):
            portBox.draw(window)
            backButton.draw(window)
        elif (pageStatus == "settings"):
            # Create a function to handle settings
            backButton.draw(window)
        else:
            for button in mainMenuButtons:
                button.draw(window)

        pygame.display.update()
        #leave this down here so it runs at the end of each frame
        #its meant to limit the fps and make the loop wait for the time lenght of a single frame if it went too fast
        clock.tick(fps)

    pygame.quit()
    sys.exit()

def hostGame(window, clock, fps, public_ip, port):
    
    #copied and pasted your player movement code here so its available for you
    
    #n = Network()   
    """startPos = read_pos(n.getPos())
    p1 = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))"""
    """p2Pos = read_pos(n.send(make_pos((p1.x, p1.y))))
    p2.x = p2Pos[0]
    p2.y = p2Pos[1]
    p2.update()
    p1.move()
    """

    #needed to display the host's ip and port so they can tell the client
    #have it display within the loop until the connection is made, then make it invisible and set a flag so that the game itself starts running
    """
    ipText = Text("Your IP: " + public_ip, 300, 100, font_size=40, color=(255, 0, 0))
    ipText.text_rect.centerx = window.get_width() // 2
    ipText.x, ipText.y = ipText.text_rect.topleft
            
    portText = Text("Your port: " + port, 300, 200, font_size=40, color=(255, 0, 0))
    portText.text_rect.centerx = window.get_width() // 2
    portText.x, portText.y = portText.text_rect.topleft
    """

    return -1

def joinGame(window, clock, fps, ip, port):
    #attempt to connect to the ip and port and then start the game loop
    

    return -1















# i left your network functions down here to separate them from the game functions

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(window, player1, player2):
    window.fill((255,255,255))
    player1.draw(window)
    player2.draw(window)
    pygame.display.update()