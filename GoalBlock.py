from block import Block
from TiledGraphics import TiledGraphics

class GoalBlock(Block):
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        super(GoalBlock, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        self.graphics = TiledGraphics("img/bluerounded.png", self.mylevel.meter*self.w, self.mylevel.meter*self.h)
