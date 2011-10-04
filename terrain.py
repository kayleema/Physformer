from elements import *
from TiledBoxGraphics import TiledBoxGraphics

class Terrain(Element):
    
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        Element.__init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        self.graphics = TiledBoxGraphics(self, "img/tilec.png", "img/tileel.png", "img/tileer.png", "img/tileeu.png", "img/tileed.png", "img/tileul.png", "img/tileur.png", "img/tiledl.png", "img/tiledr.png")

    def sim(self, time):
        pass

    def move(self, elem):
        from monster import Monster
        if isinstance(elem, Monster):
            pass
        Element.move(self,elem)
        

    def collide(self, elem):
        from block import Block
        from player import Player
        from monster import Monster
        
 
        if isinstance(elem, Block):
            Element.collide(self,elem)
        elif isinstance(elem, Player):
            direction = self.touch(elem)
            if direction == 0 or direction == 3:
                elem.vx = 0
            elif direction == 2:
                elem.vy = 0
                elem.grounded = True
            else:
                elem.vy = 0
        if isinstance(elem, Monster):
            direction = self.touch(elem)
            if direction == 0 or direction == 3:
                elem.vx = 0
            else:
                elem.vy =  0
 
