import pygame
import os
import math

height=900 #height of the game window's screen
width=1800 #width
####### Key Names
quitkey=pygame.QUIT
leftkey=pygame.K_LEFT
rightkey=pygame.K_RIGHT
upkey=pygame.K_UP
downkey=pygame.K_DOWN
pickupkey=pygame.K_SPACE
###### Key Names
current_lvl=testlvl(width,height,player)
pygame.init()
p1=elems[0]
screen=pygame.display.set_mode((width,height)) #the dimensions of the game's screen set to widthxheight
clock = pygame.time.Clock()
done=False #done means whether or not the window has been x-ed
while done==False:
    events=pygame.event.get()
    for event in events:                       ##### DON"T CARE ABOUT THIS KEEGAN
		if event.type==quitkey:                #######
			done=True                          #####
	current_lvl.sim(1/Clock.get_fps())
	current_lvl.draw(screen)
	for event in events:
		if event.type==pygame.KEYDOWN
			if event.key == leftkey:
				current_lvl.player.moveleft=True
			if event.key == rightkey:
				current_lvl.player.moveright=True
			if event.key == upkey:
				current_lvl.player.moveup=True
			if event.key == downkey:
				current_lvl.player.movedown=True
		if event.type==pygame.KEYDOWN
			if event.key == leftkey:
				current_lvl.player.moveleft=True
			if event.key == rightkey:
				current_lvl.player.moveright=True
			if event.key == upkey:
				current_lvl.player.moveup=True
			if event.key == downkey:
				current_lvl.player.movedown=True
		
    clock.tick()










	