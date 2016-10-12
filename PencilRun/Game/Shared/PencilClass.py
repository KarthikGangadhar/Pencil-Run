import pygame,time
from Game.Shared.GameConstants import GameConstants

class PencilClass(object): 
    
    def __init__(self):
        """ The constructor of the class """
        self.Ylocation = 0
        self.x = 550
        self.y = self.Ylocation
        self.width = 0
        self.height = 0
        self.y_velocity =0
    
    def handle_keys(self,sound):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 5 
        if key[pygame.K_UP]: 
            sound.stop()
            sound.play()
            self.y -= 4*dist 

    def update(self):
        dist = 5
        if self.y < self.Ylocation:
            self.y += dist
        if self.y > self.Ylocation:
            self.y = self.Ylocation

    def draw(self, surface, Sprite_path, index):
        """ Draw on surface """
        self.x = self.x - 1
        if self.x < -30:
            self.x = 550
        if index < len(Sprite_path):
            sprite = pygame.image.load((Sprite_path[index]))
            surface.blit(sprite,(self.x, self.y)) 
            size_position = []   
            size_position.append(sprite.get_size())
            (self.width,self.height) = sprite.get_size()
            size_position.append((self.x, self.y))             
            return size_position

    def __intersectsY(self, other):
        size = other[0]
        position = other[1]
        if self.y >= position[1] and self.y <= (position[1] + size[1]):
            return 1
        if (self.y + self.height) >= position[1] and self.y + self.height <= (position[1] + size[1]):
            return 1
        return 0

    def __intersectsX(self, other):
        size = other[0]
        position = other[1]
        if self.x >= position[0] and self.x <= position[0] + size[0]:
            return 1
        if (self.x + self.width) > position[0] and (self.x + self.width) <= (position[0] + size[0]):
            return 1
        return 0

    def intersects(self, other):
        if self.__intersectsX(other) and self.__intersectsY(other):
            return 1
        return 0
 
    def walk(self,x,y, surface, Sprite_path, index):
        """ Draw on surface """ 
        self.x = x
        self.y = y      
        if index < len(Sprite_path):
            sprite = pygame.image.load((Sprite_path[index]))
            #if Sprite_path[0] != 'Game\\Assets\\Sprite\\pencil\\pencil1.png':
            #    sprite = pygame.transform.scale(sprite,(50,110))
            surface.blit(sprite,(self.x, self.y)) 
           