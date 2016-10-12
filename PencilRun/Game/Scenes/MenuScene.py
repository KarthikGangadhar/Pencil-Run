import pygame,random,time
from Game.Shared.GameConstants import GameConstants as C
from Game.GameObjects.PencilObjects import TallPencil as TP, LittlePencil1 as LP, SpecksPencil1 as SP, Girlpencil1 as GP
from Game.Shared.HighScore import  Highscore
class MenuScene(object):

     def __init__(self): 
         self.Screen = pygame.display.set_mode(C.Size)
         self.pencil1 = GP() 
         self.pencil2 = LP() 
         self.pencil3 = SP() 
         self.pencil4 = GP() 
         self.pencilIndex = 0
         self.playerName = ""
         self.select_character_count = 0
         pygame.display.set_caption('Help these Geeks to reach their School!! ')
         self.character = -1
     
     def addText(self, string, x=0, y=0, color = [255,80,40], background = [0, 0, 0], size = 17, type = False):
        
         if(type):
             MousePos = pygame.mouse.get_pos()
             pygame.font.init()
             font = pygame.font.Font("freesansbold.ttf", size)
             font = pygame.font.Font(C.text321impactPath, size)
             textsurface = font.render(string, True, color)
             textrect = textsurface.get_rect()
             fontrect = textsurface.get_rect()
             textrect = (x,y,textrect[2],textrect[3])
             self.Screen.blit(textsurface, textrect)
         else:
            tooltipfont = pygame.font.Font(C.textRobotoMediumItalicPath, size)
            tooltipsurface = tooltipfont.render(string,1,color)       
            tooltip_rect = tooltipsurface.get_rect()
            textrect = (x,y,tooltip_rect[2],tooltip_rect[3])
            tooltiprect = (x,y,tooltip_rect[2],tooltip_rect[3])
            self.Screen.blit(tooltipsurface, textrect)
         #pygame.display.update()
         return textrect

     def setyLimit(self,credit_y, y_change):
         if credit_y > 0:
             credit_y -= y_change
             return credit_y
         else:
             credit_y = C.Size[1]
             return credit_y

     def onButton(self,Mouse_pos,button):
         isOnButton = False
         if(((Mouse_pos[0] >button[0] ) and (Mouse_pos[0] < button[0]+button[2]))):
             if(((Mouse_pos[1]>button[1]) and (Mouse_pos[1]< button[1] + button[3]))):
                 isOnButton = True
                 return isOnButton
             else: return isOnButton
         return isOnButton

     def displayMouse(self):
         Mouse_pos = pygame.mouse.get_pos()
         mousePoint = pygame.image.load(C.mouse)
         mouse_rect = mousePoint.get_rect()
         mouse_rect.center = Mouse_pos
         self.Screen.blit(mousePoint,mouse_rect)

     def textScreen(self):
         self.Screen.fill((0,0,0))
         pygame.mouse.set_visible(0)
         textPos = [0,0,0,0]
         while True:
             Mouse_pos = pygame.mouse.get_pos()
             mousePoint = pygame.image.load(C.mouse)
             mouse_rect = mousePoint.get_rect()
             self.Screen.fill((0,0,0))
             mouse_rect.center = Mouse_pos
             self.Screen.blit(mousePoint,mouse_rect)

             if(self.onButton(Mouse_pos,textPos)):
                 self.Screen.fill((0,0,0))  
                 textPos = self.addText("This is Pygame",300,200,[255,80,40],[0, 0, 0], 45, True)
                 self.Screen.blit(mousePoint,mouse_rect)

             else:
                 self.Screen.fill((0,0,0))
                 textPos = self.addText("This is Pygame",300,200,[255,80,40],[0, 0, 0], 45, False)
                 self.Screen.blit(mousePoint,mouse_rect)
             pygame.display.update()


             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
      
     def optionScreen(self):
         option_screen = True
         self.Screen.fill((0,255,0))
         pygame.mouse.set_visible(0)
         
         while option_screen:
             click = pygame.mouse.get_pressed()
             Mouse_pos = pygame.mouse.get_pos()
             if (self.onButton(Mouse_pos,C.select_rect)):
                 self.Screen.blit(C.select_pressed,C.selectbuttonPosition)
                 if click[0]:
                     self.character = self.select_character_count
             else:
                 self.Screen.blit(C.select,C.selectbuttonPosition)

             if (self.onButton(Mouse_pos,C.back_rect)):
                 self.Screen.blit(C.back_pressed,C.BackbuttonPosition)
                 if click[0]:
                     option_screen = False
                     self.select_character_count = 0
                     return self.select_character_count
             else:
                 self.Screen.blit(C.back,C.BackbuttonPosition)

             if (self.onButton(Mouse_pos,C.next_rect)):
                 self.Screen.blit(C.next_pressed,C.nextbuttonPosition)
                 if click[0]:
                     self.select_character_count +=1
                     if self.select_character_count > 3:
                         self.select_character_count = 0
             else:
                 self.Screen.blit(C.next,C.nextbuttonPosition)


             self.pencilIndex += 1 
             if self.pencilIndex > 5:
                 self.pencilIndex = 0

             textPos = self.addText("Select the Pencil to Run!! ",175,20,[255,80,40],[0, 0, 0], 25, False)
             if self.select_character_count == 0:
                 self.pencil1.walk(250,90, self.Screen,C.TallPencil, self.pencilIndex)
             elif self.select_character_count == 1:
                 self.pencil2.walk(250,90, self.Screen,C.Specks_path, self.pencilIndex)
             elif self.select_character_count == 2:
                 self.pencil3.walk(250,90, self.Screen,C.Girlpencil_path, self.pencilIndex)
             elif self.select_character_count == 3:
                 self.pencil4.walk(250,90, self.Screen,C.LittlePencil, self.pencilIndex)



             if self.character != -1 or (not(option_screen)) :
                 return self.character

             self.displayMouse()
             pygame.display.update()
             self.Screen.fill((0,255,0))


             time.sleep(.09)
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     exit()
         
     def start(self):
         Action = ''
         menu_control = True
         self.Screen.fill((0,255,0))
         pygame.mouse.set_visible(0)

         front_image_count = 0
         while menu_control:
             textPos = self.addText("Help these Geeks to reach their School!! ",30,20,[255,80,40],[0, 0, 0], 25, False)
             click = pygame.mouse.get_pressed()
             Mouse_pos = pygame.mouse.get_pos()
             front_image_count += 1
             if front_image_count > 6:
                 front_image_count = 0
                  

             self.Screen.blit(C.front_image[front_image_count],C.front_image_position)
             self.Screen.blit(C.option,C.optionbuttonPosition)
             self.Screen.blit(C.play,C.playbuttonPosition)
             self.Screen.blit(C.exit,C.exitbuttonPosition)
             self.Screen.blit(C.Creditst,C.creditsbuttonPosition)

             if (self.onButton(Mouse_pos,C.option_rect)):
                 self.Screen.blit(C.option_blue,C.optionbuttonPosition)
                 pygame.display.update()
                 if click[0]:
                     self.character = -1
                     self.character = self.optionScreen()

             if (self.onButton(Mouse_pos,C.play_rect)):
                 self.Screen.blit(C.play_blue,C.playbuttonPosition)
                 pygame.display.update()
                 if click[0]:
                     if self.character == -1:
                         self.character = 0
                     return self.character

             if (self.onButton(Mouse_pos,C.exit_rect)):
                 self.Screen.blit(C.exit_blue,C.exitbuttonPosition)
                 pygame.display.update()
                 if click[0]:
                     Action = 'quit' 
             
             if (self.onButton(Mouse_pos,C.Creditst_rect)):
                 self.Screen.blit(C.Creditst_blue,C.creditsbuttonPosition)
                 pygame.display.update()        
                 if click[0]:
                     self.creditScreen()
              
             self.displayMouse()
             pygame.display.update()
             self.Screen.fill((0,255,0))
             time.sleep(.05)

             for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (Action == 'quit') :
                    exit()

     def creditScreen(self):
         credit_screen = True
         self.Screen.fill((0,255,0))
         pygame.mouse.set_visible(0)
         credit_y1 = 400
         credit_y2 = 400
         credit_y3 = 400
         y_change = 10
         while credit_screen:
             click = pygame.mouse.get_pressed()
             Mouse_pos = pygame.mouse.get_pos()
             credit_y1 = self.setyLimit(credit_y1, (4*y_change))
             credit_y2 = self.setyLimit(credit_y1, (8*y_change))
             credit_y3 = self.setyLimit(credit_y1, (12*y_change))
    
             self.displayMouse()
             pygame.display.update()
             self.Screen.fill((0,255,0))
             time.sleep(.15)
             textPos = self.addText("This Game is developed by one person!! ",150,credit_y3,[255,80,40],[0, 0, 0], 25, False)
             textPos = self.addText("for more info  ",250,credit_y2,[255,80,40],[0, 0, 0], 25, False)
             textPos = self.addText("Contact: karthikg1643@gmail.com ",150,credit_y1-(3*y_change),[255,80,40],[0, 0, 0], 25, False)
             
             if (self.onButton(Mouse_pos,C.CreditBack_red_rect)):
                 self.Screen.blit(C.CreditBack_red,C.CreditBackPosition)
                 if click[0]:
                     return 0
             else:
                 self.Screen.blit(C.CreditBack_blue,C.CreditBackPosition)

             for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    exit()

     def HighestScoreScene(self,score):
         HighestScoreController = True
         waitTillNameEntered = False
         highscore  = Highscore()
         while HighestScoreController == True:
             self.Screen.fill((0,255,0))
             pygame.mouse.set_visible(0)
             if (waitTillNameEntered):
                 self.Screen.fill((0,255,0))
                 x = 100
                 y = 60
                 for score in highscore.getScores():
                     self.addText(score[0], x, y,(255,80,40), size = 30,type= False)
                     self.addText(str(score[1]), x + 200, y, (255,80,40),size = 30,type= False)
                 
                     y += 30
                 
                 self.addText("Press F1 to start a new game,F2 to quit", 20, 20, (255,80,40), size = 30,type = False)
             else:
                 self.addText("Your Name: ", 100, 150, size=30)
                 self.addText(self.playerName, 100, 200, size=30)
             time.sleep(.25)
             pygame.display.update()
             for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    exit()
                if (event.type == pygame.KEYDOWN):
                    if event.key >= 65 and event.key <= 122:
                        self.playerName += chr(event.key)
                    elif event.key == pygame.K_SPACE:
                        highscore.add(self.playerName, score)
                        waitTillNameEntered = True
                    elif event.key == pygame.K_F1:
                        self.start()
                    elif event.key == pygame.K_F2:
                        exit()
                        