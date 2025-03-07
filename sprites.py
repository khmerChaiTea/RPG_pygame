import pygame
from config import *
import math
import random

#create a class sprite sheet for efficiency, w/o inheritance
class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()
        
    def get_sprite(self, x, y, width, height):
        #width and height specified (32 x 32)
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

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
        
        #image_to_load = pygame.image.load("img/single.png")
        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        #self.image = pygame.Surface([self.width, self.height])
        #make the specified color transparent
        #self.image.set_colorkey(BLACK)
        #instead of fill image as RED, we use blit function to display image
        #self.image.blit(image_to_load, (0, 0))
        
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
            
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x ,y):
        
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.fill(BLUE)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y