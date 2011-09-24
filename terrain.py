from elements import *

class Terrain(Element):

    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        super(Terrain, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)

    def sim(self, time):
        pass

    def collide(self, elem):
        from block import Block
        from player import Player
        if isinstance(elem, Block):
            super(Terrain, self).collide(elem)
        elif isinstance(elem, Player):
            direction = self.touch(elem)
            if direction == 0 or direction == 3:
                elem.vx = 0
            else:
                elem.vy = 0
                elem.grounded = True

