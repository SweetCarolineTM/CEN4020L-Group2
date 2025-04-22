import pygame
import pymunk

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

        # Pymunk body for physics?
        mass = 1
        moment = pymunk.moment_for_box(mass, (width, height))
        self.body = pymunk.Body(mass, moment) 
        self.body.position = (x, y)

        self.shape = pymunk.Poly.create_box(self.body, (width, height))
        self.shape.elasticity = 0.4
        self.shape.friction = 0.8
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.body.position = (self.x, self.y)

        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.body.position = (self.x, self.y)

        if keys[pygame.K_UP]:
            self.y -= self.vel
            self.body.position = (self.x, self.y)

        if keys[pygame.K_DOWN]:
            self.y += self.vel
            self.body.position = (self.x, self.y)

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
