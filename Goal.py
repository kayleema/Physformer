from terrain import Terrain
from GoalBlock import GoalBlock

class Goal(Terrain):
    def collide(self, elem):
        if isinstance(elem, GoalBlock):
            mylevel.game_over = True
            print("Game Over--You won")
        else:
            super(Goal, self).collide(elem)
