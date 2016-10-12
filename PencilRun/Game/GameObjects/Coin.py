import pygame
from Game.Shared.GameConstants import GameConstants

class Coin(object):  # represents the pencil, not the game
    def __init__(self):
        """ The constructor of the class """
        self.x = 0
        self.y = GameConstants.Size[1]- 50
        self.index = 0

    def handle_moves(self):
        """ Handles Keys """
        dist = 5 
        self.x += dist 
        if self.x >= GameConstants.Size[0]:
            self.x = 0
            self.index += 1
        if  self.index >= len(GameConstants.Coin_path)-1:
            self.index = 0

    def draw(self, surface, Sprite_path, index):
        """ Draw on surface """
        index = self.index
        # blit yourself at your current position
        if index < len(Sprite_path):
            surface.blit(pygame.image.load(Sprite_path[index]),(self.x, self.y))
