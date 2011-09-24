from elements import Element
from block import Block
from elements import Element
from block import Block
from player import Player
from terrain import Terrain
from Level import Level
from Goal import Goal
from GoalBlock import GoalBlock
from Trampoline import Trampoline

class TutLevel(Level):
    def __init__(self, width, height):
        super(TutLevel, self).__init__(width, height)
        ##initialize blocks##
        boxtop = Terrain(20, -19, 40, 2, 0, 0,100, self, 0.5)
        boxleft= Terrain(-1,-5,2,30,0,0,100,self,0.5)
        boxbottom= Terrain(20,9,40,2,0,0,100,self,0.5)
        boxright= Terrain(41,-5,2,30,0,0,100,self,0.5)
        barrbottom = Terrain(15,-6,6,1,0,0,100,self,.5)
        barrright = Terrain(18.5,-11,1,10,0,0,100,self,.5)
        
        goal= Goal(38,-15.5,1,5,0,0,100,self,0.5)
        
        tramp1= Trampoline(7,7,6,1,0,0,100,self,.5)
        tramp2= Trampoline(36,7,6,1,0,0,100,self,.5)
        tramp3= Trampoline(32,-8,6,1,0,0,100,self,.5)
        tramp4= Trampoline(36,-23,6,1,0,0,100,self,.5)
        p =  Player(2, 5,  1, 2, 0, 0,  1, self, 0.5) 
        g =   GoalBlock(16.5, -7, 2, 2, 0, 0,  2, self, 0.5)
        self.add_elem(p)
        self.add_elem(barrbottom)
        self.add_elem(barrright)
        self.add_elem(tramp1)
        self.add_elem(tramp2)
        self.add_elem(tramp3)
        self.add_elem(tramp4)
        self.add_elem(g)
        self.add_elem(boxtop)
        self.add_elem(boxright)
        self.add_elem(boxbottom)
        self.add_elem(boxleft)
        self.add_elem(goal)
