import pygame
import os
from Level1 import TutLevel
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
###### Key Names
pygame.init()
screen=pygame.display.set_mode((width,height)) #the dimensions of the game's screen set to widthxheight
background = pygame.image.load("img/background.png").convert_alpha()
current_lvl=TutLevel(width,height)
clock = pygame.time.Clock()
done=False #done means whether or not the window has been x-ed
while done==False:
    events=pygame.event.get()
    for event in events:                       ##### DON"T CARE ABOUT THIS KEEGAN
        if event.type==quitkey:                #######
            done=True                          #####
    screen.fill((225,225,225))
    screen.blit(background, [0,0])
    current_lvl.draw(screen)
    if clock.get_fps() != 0:
        current_lvl.sim(1/clock.get_fps())
    for event in events:
        if event.type==pygame.KEYDOWN:
            if event.key==pickupkey:
                current_lvl=TutLevel(width,height)
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
        
    clock.tick()
    

    pygame.display.flip()
    
pygame.quit()
