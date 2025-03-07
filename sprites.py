import pygame
from config import *
import math
import random

#pygame.sprite.Sprite - a class that makes it easy to create sprites
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        
        self.game = game
        #differentiate layers
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        #call the init method in the inherited class - adding player to the group
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        #these are temp var of change in movement during a loop
        self.x_change = 0
        self.y_change = 0
        
        #default
        self.facing = 'down'
        
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        
        #the hit box
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'