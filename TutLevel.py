from elements import Element
from block import Block
from player import Player
from terrain import Terrain
from Level import Level

class TutLevel(Level):
    def __init__(self, width, height):
        super(TutLevel, self).__init__(width, height)
        ##initialize blocks##
        a = Terrain(5, 5, 20, 1, 0, 0, 10, self, 0.5)
        b =   Block(5, 0,  1, 1, 0, 0,  1, self, 0.5)
        c =  Player(0, 0,  1, 2, 0, 0,  1, self, 0.5)
		d =   Block(10, 0, 2, 2, 0, 1,  2, self, 0.5)  
        self.add_elem(c)
        self.add_elem(a)
        self.add_elem(b)
		self.add_elem(d)

