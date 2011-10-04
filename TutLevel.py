from elements import Element
from block import Block
from player import Player
from terrain import Terrain
from Level import Level
from Goal import Goal
from GoalBlock import GoalBlock

class TutLevel(Level):
    def __init__(self, width, height):
        Level.__init__(self, width, height)
        ##initialize blocks##
        boxtop = Terrain(20, -19, 40, 2, 0, 0,100, self, 0.5)
        boxleft= Terrain(-1,-5,2,30,0,0,100,self,0.5)
        boxbottom= Terrain(20,9,40,2,0,0,100,self,0.5)
        boxright= Terrain(41,-5,2,30,0,0,100,self,0.5)

        goal= Goal(38,5,1,5,0,0,100,self,0.5)
        
        
        b10 =   Block(1, 7,  2, 2, 0, 0,  1, self, 0.5)
        b20 =   Block(3, 7,  2, 2, 0, 0,  1, self, 0.5)
        b30 =   Block(5, 7,  2, 2, 0, 0,  1, self, 0.5)
        b40 =   Block(7, 7,  2, 2, 0, 0,  1, self, 0.5)
        b50 =   Block(9, 7,  2, 2, 0, 0,  1, self, 0.5)
        b11 =   Block(1, 5,  2, 2, 0, 0,  1, self, 0.5)
        b21 =   Block(3, 5,  2, 2, 0, 0,  1, self, 0.5)
        b31 =   Block(5, 5,  2, 2, 0, 0,  1, self, 0.5)
        b41 =   Block(7, 5,  2, 2, 0, 0,  1, self, 0.5)
        b51 =   Block(9, 5,  2, 2, 0, 0,  1, self, 0.5)
        b12 =   Block(1, 3,  2, 2, 0, 0,  1, self, 0.5)
        b22 =   Block(3, 3,  2, 2, 0, 0,  1, self, 0.5)
        b32 =   Block(5, 3,  2, 2, 0, 0,  1, self, 0.5)
        b42 =   Block(7, 3,  2, 2, 0, 0,  1, self, 0.5)
        b52 =   Block(9, 3,  2, 2, 0, 0,  1, self, 0.5)
        p =  Player(15, 5,  1, 2, 0, 0,  1, self, 0.5) 
        g =   GoalBlock(17, 5, 2, 2, 0, 0,  2, self, 0.5)  
        barrier = Terrain(35,-3,1,22,0,0,100,self,0.5)
        self.add_elem(p)
        self.add_elem(b10)
        self.add_elem(b20)
        self.add_elem(b30)
        self.add_elem(b40)
        self.add_elem(b50)
        self.add_elem(b11)
        self.add_elem(b21)
        self.add_elem(b31)
        self.add_elem(b41)
        self.add_elem(b51)
        self.add_elem(b12)
        self.add_elem(b22)
        self.add_elem(b32)
        self.add_elem(b42)
        self.add_elem(b52)
        self.add_elem(barrier)
        self.add_elem(g)
        self.add_elem(boxtop)
        self.add_elem(boxright)
        self.add_elem(boxbottom)
        self.add_elem(boxleft)
        self.add_elem(goal)
