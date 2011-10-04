from elements import *

class Monster(Element):
    run_velocity = 2
    jump_velocity = 5
    
    

    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co, dx, dy):
        super(Monster, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        self.x_lim, self.y_lim = dx, dy
        self.vx = 2
        self.vy = 0
        self.x_ori = self.x
        self.y_ori = self.y

    def sim(self, time):
        self.vx = self.vx/abs(self.vx) * self.run_velocity
        if abs(self.x_ori - self.x) > self.x_lim:
            self.vx = -self.vx
        self.vy = 0
        #print(self.exist) # Test
        Element.sim(self, time)

    def move(self, elem):
        from terrain import Terrain
        if isinstance(elem, Terrain):
            pass
        else:
            super(Monster, self).move(elem)

    def collide(self, elem):
        from block import Block
        from player import Player
        from terrain import Terrain
        if isinstance(elem, Block):
            Element.collide(self, elem)
        elif isinstance(elem, Player):
            self.set_exist(False)
            
            """direction = self.touch(elem)
            if direction == 4:
                self.exist = False
            else:
                elem.ch_health(-10)"""
        elif isinstance(elem, Terrain):
            pass
   

    
                
                
        

    
            
            
        
        

    
