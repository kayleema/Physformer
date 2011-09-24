import pygame
from copy import copy
from elements import Element
class Level:
    def add_elem(self,elem):
        self.elem_list+=[elem]
    
    def get_player(self):
        return self.elem_list[0]
    
    def __init__(self,width,height):
        self.w=width
        self.h=height
        self.elem_list=[]
        self.frame=[0,0,width,height]
        self.g=9.8
        self.meter=20
    
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
        self.frame[0]=self.get_player().x-self.w/2
        self.frame[1]=self.get_player().y-self.h/2
        self.frame[2]=self.get_player().x+self.w/2
        self.frame[3]=self.get_player().y+self.h/2                                    
        for elem in self.elem_list:
            elem.sim(time)
    
    def draw(self,screen):
        for elem in self.elem_list if elem.within_screen(self.frame[0],self.frame[2],self.frame[1],self.frame[3]):
            elem.draw(screen,(elem.left-self.frame[0])*self.meter,(elem.top-self.frame[1])*self.meter,(self.frame[2]-elem.right)*self.meter,(self.frame[3]-elem.bottom)*self.meter)