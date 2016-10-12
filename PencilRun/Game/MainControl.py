import pygame,time,os,sys
from Game.GameObjects import Path,Coin,Moon
from Game.GameObjects.Cactus import Cactus1, Cactus2
from Game.GameObjects.PencilObjects import TallPencil, Girlpencil1, LittlePencil1, SpecksPencil1 
from Game.Shared.GameConstants import GameConstants as C
from Game.Scenes.MenuScene import MenuScene

class MainControl(object):
    """description of class"""

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.keepGameLoop = True
        self.screen = pygame.display.set_mode(C.Size)
        self.Lives = 5
        self.Score = 0
        self.moon = Moon.Moon()
        
        self.cactus = Cactus1()
        self.cactus1 = Cactus2()
        self.path = Path.Path()
        self.clock = pygame.time.Clock()
        self.pencil_index = 0
        self.myriadProFont = pygame.font.SysFont("Myriad Pro", 24)
        self.intersectText = self.myriadProFont.render("Intersecting!", 1, (0, 0, 0), (0, 255, 0))
        self.GameOversound = pygame.mixer.Sound(C.soundGameOver)
        self.jumpsound = pygame.mixer.Sound(C.soundJump)
        self.menu = MenuScene()
        self.character = TallPencil() 
        self.select_character_count = 0

    def selectPencil(self):
        if self.select_character_count == 0:
            self.character = TallPencil()
        elif self.select_character_count == 1:
            self.character = SpecksPencil1()
        elif self.select_character_count == 2:
            self.character = Girlpencil1()
        elif self.select_character_count == 3:
            self.character = LittlePencil1()

    def control(self):
        running = True
        self.select_character_count = self.menu.start()
        self.selectPencil()
        while self.keepGameLoop:
            while running:
                scoreText = self.myriadProFont.render("SCORE: {0}".format(self.Score), 1, (0, 0, 0), (0, 255, 0))
                LivesText = self.myriadProFont.render("LIVES: {0}".format(self.Lives), 1, (0, 0, 0), (0, 255, 0))

                self.Score += 5 

                if self.pencil_index <0 or self.pencil_index > 5:
                    self.pencil_index = 0
                self.pencil_index += 1
                self.character.handle_keys(self.jumpsound) 
                self.character.update()
                self.cactus.handle_moves()
                self.moon.handle_moves()
                self.cactus1.handle_moves()
                self.path.handle_moves()
                self.screen.fill((0,255,0)) 
                self.moon.draw(self.screen,C.Moon_path,0)
                if self.select_character_count == 0:
                    pencilSize = self.character.draw(self.screen,C.TallPencil,self.pencil_index)
                elif self.select_character_count == 1:
                    pencilSize = self.character.draw(self.screen,C.Specks_path,self.pencil_index)
                elif self.select_character_count == 2:
                    pencilSize = self.character.draw(self.screen,C.Girlpencil_path,self.pencil_index)
                else:
                    pencilSize = self.character.draw(self.screen,C.LittlePencil,self.pencil_index)
                cactus_sizePosition = self.cactus.draw(self.screen,C.Cactus_list,0)
                cactus_sizePosition2 = self.cactus1.draw(self.screen,C.Cactus_list,0)
                self.screen.blit(scoreText, C.scorePosition)
                self.screen.blit(LivesText, C.LivesPosition)
                intersects = self.character.intersects(cactus_sizePosition)
                intersects2 = self.character.intersects(cactus_sizePosition2)
                if self.Lives <= 0:
                    self.screen.blit(pygame.image.load(C.GameOverText), C.GameOverPosition)
                    self.GameOversound.play()
                    time.sleep(8)
                    self.menu.HighestScoreScene(self.Score)
                    running = False
                if intersects or intersects2:
                    self.cactus = Cactus1()
                    self.cactus1 = Cactus2()
                    self.Lives =self.Lives - 1
                    self.screen.blit(self.intersectText, C.intersectPosition)
                    self.screen.blit(LivesText, C.LivesPosition)
                self.path.draw(self.screen,C.Root_Path,0)
                pygame.display.update() 
                time.sleep(.03)
                self.clock.tick(40)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
            MainControl().control()


        


