from elements import Element
from block import Block
from player import Player
from terrain import Terrain
from Level import Level

class TutLevel(Level):
    def __init__(self, width, height):
        super(TutLevel, self).__init__(width, height)
        ##initialize blocks##
        boxtop = Terrain(1, -5, 40, 1, 0, 0,100, self, 0.5)
        boxright= Terrain(20,4,1,13,0,0,100,self,0.5)
        boxbottom= Terrain(1,10,40,1,0,0,100,self,0.5)
        boxleft= Terrain(-18,4,1,13,0,0,100,self,0.5)
        b =   Block(10, 5,  2, 2, 0, 0,  1, self, 0.5)
        c =  Player(15, 5,  1, 2, 0, 0,  1, self, 0.5)
        d =   Block(7, 5, 2, 2, 0, 5,  2, self, 0.5)  
        self.add_elem(c)
        self.add_elem(b)
        self.add_elem(d)
        self.add_elem(boxtop)
        self.add_elem(boxright)
        self.add_elem(boxbottom)
        self.add_elem(boxleft)

