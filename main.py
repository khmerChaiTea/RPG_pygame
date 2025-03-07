import pygame
from sprites import *
from config import *
import sys

#game class / main class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        #framerate -  usually 60
        self.clock =  pygame.time.Clock()
        # self.font = pygame.font.Font('Arial, 32')
        self.running = True
    
    def new(self):
        #a new game starts
        self.playing = True
        
        #a group of sprites
        self.all_sprites = pygame.sprite.LayeredUpdates()
        #walls
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        
        #looking at Player() in sprite.py, self is omitted and game is replaced by 'self' followed by (x, y)
        self.player = Player(self, 1, 2)
        
    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
        
    def update(self):
        #game loop update
        self.all_sprites.update()
        
    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
        
    def main(self):
        #game loop; while True call...
        while self.playing:
            #key press event
            self.events()
            self.update()
            #display sprites
            self.draw()
        self.running = False
        
    def game_over(self):
        pass
        
    def intro_screen(self):
        pass
    
#convert class into an object
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
    
pygame.quit()
sys.exit()