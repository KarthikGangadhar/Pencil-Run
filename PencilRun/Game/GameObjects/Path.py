import pygame
from Game.Shared.GameConstants import GameConstants

class Path(object):  # represents the pencil, not the game
    def __init__(self):
        """ The constructor of the class """
        self.x = -640
        self.path =self.x + 640
        self.y = GameConstants.Size[1]- 50
    def handle_moves(self):
        """ Handles Keys """
        dist = 5 
        self.x += dist 
        if self.x >= GameConstants.Size[0]:
            self.x = -640
        if self.path >= GameConstants.Size[0]:
            self.path  = 0
    def draw(self, surface, Sprite_path, index):
        """ Draw on surface """
        surface.blit(pygame.image.load(Sprite_path[index]),(self.x, self.y))
        surface.blit(pygame.image.load(Sprite_path[1]),(self.path, self.y))
