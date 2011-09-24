from elements import Element
from block import Block
from player import Player
from terrain import Terrain
from Level import Level
from monster import Monster
from Goal import Goal
from GoalBlock import GoalBlock
from Spike import Spike
from Trampoline import Trampoline

class TutLevel(Level):
    def __init__(self, width, height):
        super(TutLevel, self).__init__(width, height)
        ##initialize blocks##
        boxtop = Terrain(20, -19, 40, 2, 0, 0,100, self, 0.5)
        boxleft= Terrain(-1,-5,2,30,0,0,100,self,0.5)
        boxbottom= Terrain(23,9,46,2,0,0,100,self,0.5)
        boxright= Terrain(47,-5,2,30,0,0,100,self,0.5)

        goal= Goal(44,5,1,5,0,0,100,self,0.5)
        
        
        b =   Block(2, 2,  2, 2, 0, 0,  1, self, 0.5)
        c =  Player(7, 5,  1, 2, 0, 0,  1, self, 0.5)
        d =   Block(4, 2, 2, 2, 0, 5,  2, self, 0.5)  
        a =   GoalBlock(4, 5, 2, 2, 0, 5,  2, self, 0.5) 
        m = Trampoline(30, -4, 2, 1, 0, 0, 1, self, 0.5)
        e = Spike(23, 8, 29, 1, 0, 0, 100, self, 0.1)
        f = Spike(23, 6, 1, 1, 0, 0, 100, self, 0.1)
        self.add_elem(c)
        self.add_elem(m)
        self.add_elem(b)
        self.add_elem(a)
        self.add_elem(d)
        self.add_elem(e)
        self.add_elem(f)
        self.add_elem(boxtop)
        self.add_elem(boxright)
        self.add_elem(boxbottom)
        self.add_elem(boxleft)
        self.add_elem(goal)
