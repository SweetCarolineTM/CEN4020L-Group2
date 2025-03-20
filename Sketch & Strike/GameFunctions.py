import sys
import socket 
import pygame
import requests
from Button import Button
from Player import Player
from PasswordBox import PasswordBox
from Text import Text
from Network import Network

import subprocess

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
    subprocess.Popen(["python", "Server.py", port]) #starter the server
    #then should go to this game screen, in public_ip:port
    #joinGame(window,clock,fps,public_ip,port)
    return 1

def joinGame(window, clock, fps, ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip, int(port)))
        print(f"Connected to {ip}:{port}")
        
        player1 = Player(100, 100, 100, 100, pygame.Color("green"))
        player2 = Player(0, 0, 100, 100, pygame.Color("red"))
        
        
        #we have another game loop in here, to go to the main game
        running = True
        while running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            
            player1.move()
            
            # Send player position to the server
            client.send(f"{player1.x},{player1.y}".encode())
            
            # Receive player2's position from the server
            try:
                data = client.recv(4096).decode()
                if data:
                    player2x, player2y = map(int, data.split(","))
                    player2.x, player2.y = player2x, player2y
                    player2.update()
            except:
                pass
            
            # Draw players on the window
            window.fill((255, 255, 255))  # Clear screen
            player1.draw(window)
            player2.draw(window)
            pygame.display.update()
        
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        client.close()
        print("Connection closed.")
    return 1