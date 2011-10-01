from terrain import Terrain
from TiledGraphics import TiledGraphics

class Trampoline(Terrain):
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        super(Trampoline, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        self.graphics = TiledGraphics("img/tramp2.png", self.mylevel.meter, self.mylevel.meter)
    def collide(self, elem):
        elem.vy = -20
