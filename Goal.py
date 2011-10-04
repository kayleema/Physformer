from terrain import Terrain
from GoalBlock import GoalBlock
from TiledGraphics import TiledGraphics
class Goal(Terrain):
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, level_co, c_co):
        Terrain.__init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, level_co, c_co)
        self.graphics = TiledGraphics("img/goal.png", self.mylevel.meter, self.mylevel.meter)
    def collide(self, elem):
        if isinstance(elem, GoalBlock):
            self.mylevel.game_over = True
        else:
            Terrain.collide(self, elem)
