import pygame
from Game.Shared.GameConstants import GameConstants

class Moon(object):  # represents the pencil, not the game
    def __init__(self):
        """ The constructor of the class """
        self.change_img = 0
        self.x = 50
        self.y = GameConstants.Size[1]- 360
        self.index = 0

    def handle_moves(self):       
        """ Handles Keys """
        self.change_img += 5
        self.index = int(self.change_img / 80)
        if self.change_img >= 640:
            self.change_img = 0
            self.index = (self.change_img % 80)
            
        if  self.index >= len(GameConstants.Moon_path)-1:
            self.index = 0

    def draw(self, surface, Sprite_path, index):
        """ Draw on surface """
        index = self.index
        # blit yourself at your current position
        if index < len(Sprite_path):
            surface.blit(pygame.image.load(Sprite_path[index]),(self.x, self.y))
