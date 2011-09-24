from elements import *

class Block(Element):
    
    
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        super(Block, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        # self.ax = acc_x
        # self.ay = acc_y
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        self.health = 100


    def collide(self, elem):
        from terrain import Terrain
        from player import Player
        if isinstance(elem, Player) or isinstance(elem, Terrain):
            return
        super(Block, self).collide(elem)

    def move(self, elem):
        from terrain import Terrain
        from player import Player
        if isinstance(elem, Player) or isinstance(elem, Terrain):
            return
        super(Block, self).move(elem)
