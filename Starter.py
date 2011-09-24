import pygame
import os
import TutLevel
import Level1
import LevelReal
os.environ['SDL_VIDEO_CENTERED'] = '1'
height=600 #height of the game window's screen
width=800 #width
####### Key Names
quitkey=pygame.QUIT
leftkey=pygame.K_LEFT
rightkey=pygame.K_RIGHT
upkey=pygame.K_UP
downkey=pygame.K_DOWN
pickupkey=pygame.K_SPACE
levelselected=False
###### Key Names
pygame.init()
screen=pygame.display.set_mode((width,height)) #the dimensions of the game's screen set to widthxheight
background = pygame.image.load("img/background.png").convert_alpha()
current_lvl=TutLevel.TutLevel(width,height)
clock = pygame.time.Clock()
option=1
done=False #done means whether or not the window has been x-ed
while done==False:
    events=pygame.event.get()
    for event in events:                       ##### DON"T CARE ABOUT THIS KEEGAN
        if event.type==quitkey:                #######
            done=True                          #####
    screen.fill((225,225,225))
    if levelselected:
        if current_lvl.game_over:
            screen.blit(background, [0,0])
            if current_lvl.game_won:
                font=pygame.font.Font(None, 50)
                text = font.render("EFF YEZ",True,(0,0,0))
                screen.blit(text,[width*2/5,height/2])
                for event in events:
                    if event.type==pygame.KEYDOWN:
                        levelselected=False
            else:
                font=pygame.font.Font(None, 40)
                text = font.render("YOU GOT OWNED DESOOO",True,(0,0,0))
                screen.blit(text,[width/4,height/2])
                for event in events:
                    if event.type==pygame.KEYDOWN:
                        levelselected=False
        else:
            screen.blit(background, [0,0])
            current_lvl.draw(screen)
            if clock.get_fps() != 0:
                current_lvl.sim(1/clock.get_fps())
            for event in events:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        levelselected=False
                    if event.key==pickupkey:
                        if option==1:
                            current_lvl=TutLevel.TutLevel(width,height)
                        if option==2:
                            current_lvl=Level1.TutLevel(width,height)
                        if option==3:
                            current_lvl=LevelReal.TutLevel(width,height)
                    if event.key == leftkey:
                        current_lvl.get_player().moveleft=True
                    if event.key == rightkey:
                        current_lvl.get_player().moveright=True
                    if event.key == upkey:
                        current_lvl.get_player().moveup=True
                    if event.key == downkey:
                        current_lvl.get_player().movedown=True
                if event.type==pygame.KEYUP:
                    if event.key == leftkey:
                        current_lvl.get_player().moveleft=False
                    if event.key == rightkey:
                        current_lvl.get_player().moveright=False
                    if event.key == upkey:
                        current_lvl.get_player().moveup=False
                    if event.key == downkey:
                        current_lvl.get_player().movedown=False
    else:
        for event in events:
            if event.type==pygame.KEYDOWN:
                if event.key == upkey:
                    option-=1
                if event.key == downkey:
                    option+=1
                if option>3:
                    option=3
                if option<1:
                    option=1
                if event.key == rightkey:
                    if option==1:
                        current_lvl=TutLevel.TutLevel(width,height)
                    if option==2:
                        current_lvl=Level1.TutLevel(width,height)
                    if option==3:
                        current_lvl=LevelReal.TutLevel(width,height)
                    levelselected=True
        font = pygame.font.Font(None, 25)
        text1 = font.render("TutLvl",True,(0,0,0))
        text2 = font.render("Level1",True,(0,0,0))
        text3 = font.render("RealLevel",True,(0,0,0))
        screen.blit(text1,[width/2,height/4])
        screen.blit(text2,[width/2,height*2/4])
        screen.blit(text3,[width/2,height*3/4])
        if option==1:
            pygame.draw.line(screen,(0,0,0),[0,height/4],[width/2,height/4])
        if option==2:
            pygame.draw.line(screen,(0,0,0),[0,height*2/4],[width/2,height*2/4])
        if option==3:
            pygame.draw.line(screen,(0,0,0),[0,height*3/4],[width/2,height*3/4])
    clock.tick()
    

    pygame.display.flip()
    
pygame.quit()
