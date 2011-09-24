from elements import *

class Terrain(Element):

    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        super(Terrain, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        self.graphics = TiledGraphics("img/sandstone.png", 40, 40)

    def sim(self, time):
        pass

    def move(self, elem):
        from monster import Monster
        if isinstance(elem, Monster):
            pass
        super(Terrain, self).move(elem)
        

    def collide(self, elem):
        from block import Block
        from player import Player
        from monster import Monster
        
 
        if isinstance(elem, Block):
            super(Terrain, self).collide(elem)
        elif isinstance(elem, Player):
            direction = self.touch(elem)
            if direction == 0 or direction == 3:
                elem.vx = 0
            else:
                elem.vy = 0
                elem.grounded = True
        if isinstance(elem, Monster):
            direction = self.touch(elem)
            if direction == 0 or direction == 3:
                elem.vx = 0
            else:
                elem.vy =  0
 
