from terrain import Terrain
from GoalBlock import GoalBlock
from TiledGraphics import TiledGraphics
class Goal(Terrain):
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, level_co, c_co):
        super(Terrain, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, level_co, c_co)
        self.graphics = TiledGraphics("img/goal.png", 40, 40)
    def collide(self, elem):
        print("collision")
        if isinstance(elem, GoalBlock):
            self.mylevel.game_over = True
            print("Game Over--You won")
        else:
            super(Goal, self).collide(elem)
