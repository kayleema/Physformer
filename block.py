from elements import *
from ImageGraphics import ImageGraphics
from TiledGraphics import TiledGraphics

class Block(Element):
    
    
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        Element.__init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        # self.ax = acc_x
        # self.ay = acc_y
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        self.health = 100
        self.graphics = TiledGraphics("img/roundedblock.png", self.mylevel.meter*self.w, self.mylevel.meter*self.h)

    def collide(self, elem):
        from terrain import Terrain
        from player import Player
        from monster import Monster
        if isinstance(elem, Monster):
            pass
        direction = self.touch(elem)
        if (isinstance(elem, Player) and direction != 2) or isinstance(elem, Terrain) or isinstance(elem, Monster):
            return
        super(Block, self).collide(elem)

    def move(self, elem):
        from terrain import Terrain
        from player import Player
        direction = self.touch(elem)
        if isinstance(elem, Terrain):
            return
        if isinstance(elem, Player):
            elem.grounded = True
        Element.move(self, elem)
