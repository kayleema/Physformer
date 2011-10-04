from elements import Element
from terrain import Terrain
from player import Player
from ImageGraphics import ImageGraphics
from TiledGraphics import TiledGraphics
from Graphics import Graphics

class Spike(Terrain):
     def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
         Terrain.__init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
         self.graphics = TiledGraphics("img/spike.png", self.mylevel.meter, self.mylevel.meter)
     def collide(self, elem):
          Terrain.collide(self, elem)
          if isinstance(elem, Player):
               elem.ch_health(-34)
     
