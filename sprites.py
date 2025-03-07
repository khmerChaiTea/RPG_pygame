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
        
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        
        #the hit box
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        pass