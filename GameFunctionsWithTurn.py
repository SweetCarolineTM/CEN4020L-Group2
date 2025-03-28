#This file is the GameFunctions.py with the updated turn implementation, replace the GameFuncitons.py with
#this file when this file is complete (rename back to GameFunctions.py in main)
# game functions
import socket 
import pygame
import Button
#import pymunk


#player and game functionalities

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def turn (self):
        chooseWeapon(self)
        move(self)
        drawTerrain(self)
        #useItem(self)
        attack(self)

        #update the terrain based on the players attack (if the attack removed some terrain for ex.)
        updateTerrain(self)
        #calculate if a player got hit by an attack
        playerDamageCalc(self)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def joinGame():
    foo = False #workon later
