import pygame
from Game.Shared.GameConstants import GameConstants
import random

class Cactus(object): 
    def __init__(self):
        """ The constructor of the class """
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.index = 0

    def handle_moves(self):
        """ Handles Keys """
        dist = 5 
        self.x += dist 
        if self.x >= GameConstants.Size[0]:
            self.x = 0
            self.index += random.randrange(0, 6)
        if  self.index >= len(GameConstants.Cactus_list)-1:
            self.index = 0

    def draw(self, surface, Sprite_path, index):
        """ Draw on surface """
        index = self.index
        if index == 1 or index == 4:
            self.y = GameConstants.Size[1]- 63
        else:
            self.y = GameConstants.Size[1]- 50
       
        if index < len(Sprite_path):
            sprite = pygame.image.load((Sprite_path[index]))
            surface.blit(sprite,(self.x, self.y)) 
            size_position = []   
            size_position.append(sprite.get_size())
            (self.width,self.height) = sprite.get_size()
            size_position.append((self.x, self.y))             
            return size_position

class Cactus1(Cactus): 
    def __init__(self):
        """ The constructor of the class """
        self.x = 0
        self.y = GameConstants.Size[1]- 50
        self.width = 0
        self.height = 0
        self.index = random.randrange(0, 6)

class Cactus2(Cactus): 
    def __init__(self):
        """ The constructor of the class """
        self.x = -300
        self.y = GameConstants.Size[1]- 50
        self.width = 0
        self.height = 0
        self.index = random.randrange(0, 6)