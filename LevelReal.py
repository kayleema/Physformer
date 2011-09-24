from elements import Element
from block import Block
from player import Player  
from Level import Level
from terrain import Terrain

class TutLevel(Level):
    def __init__(self, width, height):
        super(TutLevel, self).__init__(width, height)
        ##initialize blocks##
        p1 =     Terrain(70, 9, 40, 2, 0, 0,100, self, 0.5)
        p2=     Terrain(20,1,40,2,0,0,100,self,0.5)
        p3=     Terrain(70,1,40,2,0,0,100,self,.5)
        p4=     Terrain(-10,-20,2,41,0,0,100,self,.5)
        p5=     Terrain(20,-40,40,2,0,0,100,self,0.5)
        p6=     Terrain(70,-40,40,2,0,0,100,self,.5)
        p7=     Terrain(45,20,10,2,0,0,100,self,.5)
        b =   Block(70, -45,  2, 2, 0, 0,  1, self, 0.5)
        c =  Player(70, 5,  1, 2, 0, 0,  1, self, 0.5)
        d =   Block(7, -45, 2, 2, 0, 5,  2, self, 0.5)  
        self.add_elem(c)
        self.add_elem(b)
        self.add_elem(d)
        self.add_elem(p1)
        self.add_elem(p2)
        self.add_elem(p3)
        self.add_elem(p4)
        self.add_elem(p5)
        self.add_elem(p6)
        self.add_elem(p7)