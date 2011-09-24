from elements import Element
from terrain import Terrain
from player import Player
from ImageGraphics import ImageGraphics

class Spike(Terrain):
     def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
         super(Spike, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
         self.graphics = ImageGraphics("img/spike.png")
     def collide(self, elem):
         super(Spike, self).collide(elem)
         if isinstance(elem, Player):
             elem.ch_health(-1)
             pass##add damage here
     
