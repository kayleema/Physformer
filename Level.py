import pygame
from copy import copy
from elements import Element
class Level(object):
    def add_elem(self,elem):
        self.elem_list+=[elem]
    
    def get_player(self):
        return self.elem_list[0]
    
    def __init__(self,width,height):
        self.w=width
        self.h=height
        self.elem_list=[]
        self.frame=[0,0,width,height]
        self.g=14
        self.meter=40
        self.game_over = False
    
    def sim(self,time):
        i=0                                                         ### Checking touching loop (with collide)
        while i<len(self.elem_list):
            j=i+1
            while j<len(self.elem_list):
                if self.elem_list[i].touch(self.elem_list[j]):
                    e1=copy(self.elem_list[i])
                    e2=copy(self.elem_list[j])
                    e1.collide(self.elem_list[j])
                    e2.collide(self.elem_list[i])
                    e2.move(self.elem_list[i])
                    e1.move(self.elem_list[j])
                j+=1
            i+=1                                                    ### Checking touching loop end (with collide)

        for elem in self.elem_list:
            if elem.exist:
                elem.sim(time)
    
    def draw(self,screen):
        x=self.get_player().x*self.meter
        y=self.get_player().y*self.meter
        self.frame=[x-self.w/2,y-self.h/2,self.w/2+x,self.h/2+y]
        for elem in self.elem_list:
            #print(elem.exist)
            if elem.within_screen(self.frame[0],self.frame[2],self.frame[1],self.frame[3]) and elem.exist:
                elem.draw(screen,elem.left*self.meter-self.frame[0],elem.top*self.meter-self.frame[1],(elem.w)*self.meter,(elem.h)*self.meter)
        
        screen.fill((128,128,128), [10,10,200,20])
        screen.fill((200, 0, 0), [15, 15, 190*self.get_player().health/100, 10])
