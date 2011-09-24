from elements import Element
from terrain import Terrain
from player import Player
from ImageGraphics import ImageGraphics
from TiledGraphics import TiledGraphics

class Spike(Terrain):
     def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
         super(Spike, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
         self.graphics = TiledGraphics("img/spike.png", 40, 40)
     def collide(self, elem):
         super(Spike, self).collide(elem)
         if isinstance(elem, Player):
             elem.ch_health(-34)
             pass##add damage here
     
