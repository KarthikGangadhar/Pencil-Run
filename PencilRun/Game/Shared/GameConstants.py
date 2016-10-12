import os
import pygame
class GameConstants(object):
    """description of class"""
    Size = (640,400)
    scorePosition = (10, 30)
    LivesPosition = (10, 10)
    intersectPosition =(500, 10)
    GameOverPosition =(215, 183)
    playbuttonPosition = (505,20)
    optionbuttonPosition = (505,115)
    exitbuttonPosition = (505,295)
    creditsbuttonPosition = (505,205)
    selectbuttonPosition = (265,300)
    BackbuttonPosition = (80,300)
    nextbuttonPosition = (425,300)
    CreditBackPosition =(10,148)
    Compression_ratio = (105,75)
    front_image_cprn_ratio = (380,280)
    front_image_position = (20,90)

    front_image = []
    image = pygame.image.load(os.path.join("Game", "Assets","Sprite" ,"menu", "frontimage", "11.png"))
    image = pygame.transform.scale(image, front_image_cprn_ratio)
    front_image.append(image)
    image = pygame.image.load(os.path.join("Game", "Assets","Sprite" ,"menu", "frontimage", "12.png"))
    image = pygame.transform.scale(image,front_image_cprn_ratio)
    front_image.append(image)
    image = pygame.image.load(os.path.join("Game", "Assets","Sprite" ,"menu", "frontimage", "13.png"))
    image = pygame.transform.scale(image, front_image_cprn_ratio)
    front_image.append(image)
    image = pygame.image.load(os.path.join("Game", "Assets","Sprite" ,"menu", "frontimage", "14.png"))
    image = pygame.transform.scale(image, front_image_cprn_ratio)
    front_image.append(image)
    image = pygame.image.load(os.path.join("Game", "Assets","Sprite" ,"menu", "frontimage", "15.png"))
    image = pygame.transform.scale(image, front_image_cprn_ratio)
    front_image.append(image)
    image = pygame.image.load(os.path.join("Game", "Assets","Sprite" ,"menu", "frontimage", "16.png"))
    image = pygame.transform.scale(image, front_image_cprn_ratio)
    front_image.append(image)
    image = pygame.image.load(os.path.join("Game", "Assets","Sprite" ,"menu", "frontimage", "17.png"))
    image = pygame.transform.scale(image, front_image_cprn_ratio)
    front_image.append(image)
    

    TallPencil = []
    TallPencil.append(os.path.join("Game", "Assets","Sprite" ,"pencil","pencil1.png"))
    TallPencil.append(os.path.join("Game", "Assets","Sprite","pencil", "pencil2.png"))
    TallPencil.append(os.path.join("Game", "Assets","Sprite","pencil","pencil3.png"))
    TallPencil.append(os.path.join("Game", "Assets","Sprite" ,"pencil","pencil4.png"))
    TallPencil.append(os.path.join("Game", "Assets","Sprite","pencil", "pencil5.png"))
    TallPencil.append(os.path.join("Game", "Assets","Sprite","pencil", "pencil6.png"))
    LittlePencil = []
    LittlePencil.append(os.path.join("Game", "Assets","Sprite" ,"Littlepencil","littlepencil11.png"))
    LittlePencil.append(os.path.join("Game", "Assets","Sprite" ,"Littlepencil","littlepencil12.png"))
    LittlePencil.append(os.path.join("Game", "Assets","Sprite" ,"Littlepencil","littlepencil13.png"))
    LittlePencil.append(os.path.join("Game", "Assets","Sprite" ,"Littlepencil","littlepencil14.png"))
    LittlePencil.append(os.path.join("Game", "Assets","Sprite" ,"Littlepencil","littlepencil15.png"))
    LittlePencil.append(os.path.join("Game", "Assets","Sprite" ,"Littlepencil","littlepencil16.png"))
    Specks_path = []
    Specks_path.append(os.path.join("Game", "Assets","Sprite" ,"Specks","specks1.png"))
    Specks_path.append(os.path.join("Game", "Assets","Sprite" ,"Specks","specks2.png"))
    Specks_path.append(os.path.join("Game", "Assets","Sprite" ,"Specks","specks3.png"))
    Specks_path.append(os.path.join("Game", "Assets","Sprite" ,"Specks","specks4.png"))
    Specks_path.append(os.path.join("Game", "Assets","Sprite" ,"Specks","specks5.png"))
    Specks_path.append(os.path.join("Game", "Assets","Sprite" ,"Specks","specks6.png"))
    Girlpencil_path = []
    Girlpencil_path.append(os.path.join("Game", "Assets","Sprite" ,"GirlPencil","girlpencil11.png"))
    Girlpencil_path.append(os.path.join("Game", "Assets","Sprite" ,"GirlPencil","girlpencil12.png"))
    Girlpencil_path.append(os.path.join("Game", "Assets","Sprite" ,"GirlPencil","girlpencil13.png"))
    Girlpencil_path.append(os.path.join("Game", "Assets","Sprite" ,"GirlPencil","girlpencil14.png"))
    Girlpencil_path.append(os.path.join("Game", "Assets","Sprite" ,"GirlPencil","girlpencil15.png"))
    Girlpencil_path.append(os.path.join("Game", "Assets","Sprite" ,"GirlPencil","girlpencil16.png"))


    Moon_path = []
    Moon_path.append(os.path.join("Game", "Assets","Sprite" ,"moon","moon11.png"))
    Moon_path.append(os.path.join("Game", "Assets","Sprite" ,"moon","moon12.png"))
    Moon_path.append(os.path.join("Game", "Assets","Sprite" ,"moon","moon13.png"))
    Moon_path.append(os.path.join("Game", "Assets","Sprite" ,"moon","moon14.png"))
    Cactus_list = []
    Cactus_list.append(os.path.join("Game", "Assets","Sprite" ,"cactus","cactus1.png"))
    Cactus_list.append(os.path.join("Game", "Assets","Sprite" ,"cactus","cactus11.png"))
    Cactus_list.append(os.path.join("Game", "Assets","Sprite" ,"cactus","cactus2.png"))
    Cactus_list.append(os.path.join("Game", "Assets","Sprite" ,"cactus","cactus3.png"))
    Cactus_list.append(os.path.join("Game", "Assets","Sprite" ,"cactus","cactus4.png"))
    Cactus_list.append(os.path.join("Game", "Assets","Sprite" ,"cactus","cactus22.png"))
    Root_Path = []
    Root_Path.append(os.path.join("Game", "Assets","Sprite" ,"path","path3.png"))
    Root_Path.append(os.path.join("Game", "Assets","Sprite" ,"path","path4.png"))
    Coin_path = []
    Coin_path.append(os.path.join("Game", "Assets","Sprite" ,"coin","coin1.png"))
    Coin_path.append(os.path.join("Game", "Assets","Sprite" ,"coin","coin2.png"))
    Coin_path.append(os.path.join("Game", "Assets","Sprite" ,"coin","coin3.png"))
    Bird_path = []
    Bird_path.append(os.path.join("Game", "Assets","Sprite" ,"bird","bird_1.png"))
    Bird_path.append(os.path.join("Game", "Assets","Sprite" ,"bird","bird_2.png"))
    GameOverText =os.path.join("Game", "Assets","Sprite" ,"GameOver.png")  
    highscore =os.path.join("Game", "Assets","Sprite" ,"highscore.png")  
    menu =os.path.join("Game", "Assets","Sprite" ,"menu.png")  
    soundGameOver = os.path.join("Game", "Assets","sound" ,"gameover.wav")
    soundJump = os.path.join("Game", "Assets","sound" ,"jump.wav")

    #Menu image Paths
    Creditst_buttons =os.path.join("Game", "Assets","Sprite","menu" ,"Creditst_buttons_crop.png")  
    Creditst_buttons_pressed =os.path.join("Game", "Assets","Sprite","menu" ,"Creditst_buttons_pressed_cropped.png")  
    exit_buttons =os.path.join("Game", "Assets","Sprite","menu" ,"exit_buttons_cropped.png")  
    exit_buttons_pressed =os.path.join("Game", "Assets","Sprite","menu" ,"exit_buttons_pressed_cropped.png")  
    optionst_buttons =os.path.join("Game", "Assets","Sprite","menu" ,"optionst_buttons_cropped.png")  
    optionst_buttons_pressed =os.path.join("Game", "Assets","Sprite","menu" ,"optionst_buttons_pressed_cropped.png")  
    play_buttons =os.path.join("Game", "Assets","Sprite","menu" ,"play_buttons_cropped.png")  
    play_buttons_pressed =os.path.join("Game", "Assets","Sprite","menu" ,"play_buttons_pressed_cropped.png")  
    play_buttons_pressed_2 =os.path.join("Game", "Assets","Sprite","menu" ,"play_buttons_pressed_2_cropped.png")  
    play_buttons_pressed_blue =os.path.join("Game", "Assets","Sprite","menu" ,"play_buttons_pressed_blue_cropped.png")
    GameBackGround =os.path.join("Game", "Assets","Sprite","menu" ,"bg.png")   
    mouse =os.path.join("Game", "Assets","Sprite","menu" ,"mouse.png")   
    text321impactPath = os.path.join("Game", "Assets","Sprite","text" ,"321impact.ttf") 
    textRobotoMediumItalicPath = os.path.join("Game", "Assets","Sprite","text" ,"Roboto-MediumItalic.ttf") 
    select_red = os.path.join("Game", "Assets","Sprite","menu" ,"select_red.png")
    select_blue = os.path.join("Game", "Assets","Sprite","menu" ,"select.png")
    back_red = os.path.join("Game", "Assets","Sprite","menu" ,"back_red.png")
    back_blue = os.path.join("Game", "Assets","Sprite","menu" ,"back_blue.png")
    next_red = os.path.join("Game", "Assets","Sprite","menu" ,"next_red.png")
    next_blue = os.path.join("Game", "Assets","Sprite","menu" ,"next_blue.png")
    #Roboto-MediumItalic.ttf
    #top_banner =os.path.join("Game", "Assets","Sprite","menu" ,"top_banner.jpg")  


    #MENU and OPTION Screen Buttons

    select = pygame.image.load(select_red)
    select = pygame.transform.scale(select, Compression_ratio)
    select_rect = select.get_rect()
    select_rect[0],select_rect[1] = selectbuttonPosition

    select_pressed = pygame.image.load(select_blue)
    select_pressed = pygame.transform.scale(select_pressed, Compression_ratio)
    select_pressed_rect = select_pressed.get_rect()
    select_pressed_rect[0],select_pressed_rect[1] = selectbuttonPosition

    back = pygame.image.load(back_red)
    back = pygame.transform.scale(back, Compression_ratio)
    back_rect = back.get_rect()
    back_rect[0],back_rect[1]=BackbuttonPosition

    back_pressed = pygame.image.load(back_blue)
    back_pressed = pygame.transform.scale(back_pressed, Compression_ratio)
    back_pressed_rect = back_pressed.get_rect()
    back_pressed_rect[0],back_pressed_rect[1]=BackbuttonPosition

    next_pressed = pygame.image.load(next_blue)
    next_pressed = pygame.transform.scale(next_pressed, Compression_ratio)
    next_pressed_rect = next_pressed.get_rect()
    next_pressed_rect[0],next_pressed_rect[1]=nextbuttonPosition
    
    next = pygame.image.load(next_red)
    next = pygame.transform.scale(next, Compression_ratio)
    next_rect = next.get_rect()
    next_rect[0],next_rect[1]=nextbuttonPosition

    option = pygame.image.load(optionst_buttons)
    option = pygame.transform.scale(option, Compression_ratio)
    option_rect = option.get_rect()
    option_rect[0],option_rect[1]=optionbuttonPosition

    option_blue = pygame.image.load(optionst_buttons_pressed)
    option_blue = pygame.transform.scale(option_blue, Compression_ratio)
    option_blue_rect = option_blue.get_rect()
    option_blue_rect[0],option_blue_rect[1]=optionbuttonPosition

    play_blue = pygame.image.load(play_buttons_pressed_blue)
    play_blue = pygame.transform.scale(play_blue, Compression_ratio)
    play_blue_rect = play_blue.get_rect()
    play_blue_rect[0],play_blue_rect[1]=playbuttonPosition

    play = pygame.image.load(play_buttons)
    play = pygame.transform.scale(play, Compression_ratio)
    play_rect = play.get_rect()
    play_rect[0],play_rect[1]=playbuttonPosition


    exit_blue = pygame.image.load(exit_buttons_pressed)
    exit_blue = pygame.transform.scale(exit_blue, Compression_ratio)
    exit_blue_rect = exit_blue.get_rect()
    exit_blue_rect[0],exit_blue_rect[1]=exitbuttonPosition

    exit = pygame.image.load(exit_buttons)
    exit = pygame.transform.scale(exit, Compression_ratio)
    exit_rect = exit.get_rect()
    exit_rect[0],exit_rect[1]=exitbuttonPosition

    Creditst = pygame.image.load(Creditst_buttons)
    Creditst = pygame.transform.scale(Creditst, Compression_ratio)
    Creditst_rect = Creditst.get_rect()
    Creditst_rect[0],Creditst_rect[1]=creditsbuttonPosition

    Creditst_blue = pygame.image.load(Creditst_buttons_pressed)
    Creditst_blue = pygame.transform.scale(Creditst_blue, Compression_ratio)
    Creditst_blue_rect = Creditst_blue.get_rect()
    Creditst_blue_rect[0],Creditst_blue_rect[1]=creditsbuttonPosition

    CreditBack_red = pygame.image.load(back_blue)
    CreditBack_red = pygame.transform.scale(CreditBack_red, Compression_ratio)
    CreditBack_red_rect = CreditBack_red.get_rect()
    CreditBack_red_rect[0],CreditBack_red_rect[1]=CreditBackPosition

    CreditBack_blue = pygame.image.load(back_red)
    CreditBack_blue = pygame.transform.scale(CreditBack_blue, Compression_ratio)
    CreditBack_blue_rect = CreditBack_blue.get_rect()
    CreditBack_blue_rect[0],CreditBack_blue_rect[1]=CreditBackPosition
