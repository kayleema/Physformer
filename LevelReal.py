from elements import Element
from block import Block
from player import Player
from terrain import Terrain
from Level import Level
from monster import Monster
from Goal import Goal
from GoalBlock import GoalBlock
from Spike import Spike

class TutLevel(Level):
    def __init__(self, width, height):
        super(TutLevel, self).__init__(width, height)
        ##initialize blocks##
        boxtop = Terrain(50, 2, 100, 2, 0, 0,100, self, 0.5)
        boxleft= Terrain(1,50,2,100,0,0,100,self,0.5)
        boxbottom= Terrain(50,100,100,2,0,0,100,self,0.5)
        boxright= Terrain(100, 50,2,100,0,0,100,self,0.5)
        goal= Goal(95,95,1,5,0,0,100,self,0.5)
        a =   GoalBlock(4, 90, 2, 2, 0, 5,  2, self, 0.5)
        
        t1 = Terrain(8, 70, 2, 56, 0, 0, 100, self, 0.5)
        c =  Player(3, 90,  1, 2, 0, 0,  1, self, 0.5)
        self.add_elem(c)
        for i in range (0, 10):
            e = Spike(15+i, 98, 1, 1, 0, 0, 100, self, 0.5)
            self.add_elem(e)

        for i in range (0, 10):
            e = Spike(35+i, 98, 1, 1, 0, 0, 100, self, 0.5)
            self.add_elem(e)

        for i in range (0, 10):
            e = Spike(40+i, 98, 1, 1, 0, 0, 100, self, 0.5)
            self.add_elem(e)

        b = Block (4, 90, 2, 2, 0, 5, 2, self, 0.5)

        c =  Player(3, 90,  1, 2, 0, 0,  1, self, 0.5)

        
        
        



        
        self.add_elem(t1)
        self.add_elem(boxtop)
        self.add_elem(boxright)
        self.add_elem(boxbottom)
        self.add_elem(boxleft)
        self.add_elem(a)
        self.add_elem(goal)
