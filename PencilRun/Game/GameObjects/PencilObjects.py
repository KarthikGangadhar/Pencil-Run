from Game.Shared.GameConstants import GameConstants
from Game.Shared.PencilClass import PencilClass

class TallPencil(PencilClass):
    def __init__(self):
        PencilClass.__init__(self)
        self.Ylocation = GameConstants.Size[1]- 200
        self.x = 550
        self.y = self.Ylocation
        self.width = 0
        self.height = 0
        self.y_velocity =0

class SpecksPencil1(PencilClass):     
    def __init__(self):
        self.Ylocation = GameConstants.Size[1]- 105
        self.x = 550
        self.y = self.Ylocation
        self.width = 0
        self.height = 0

class Girlpencil1(PencilClass):   
    def __init__(self):
        self.Ylocation = GameConstants.Size[1]- 113
        self.x = 550
        self.y = self.Ylocation
        self.width = 0
        self.height = 0
        self.y_velocity =0

class LittlePencil1(PencilClass): 
    def __init__(self):
        self.Ylocation = GameConstants.Size[1]- 70
        self.x = 550
        self.y = self.Ylocation
        self.width = 0
        self.height = 0
        self.y_velocity =0




