from terrain import Terrain

class Monster(Terrain):
    run_velocity = 5
    jump_velocity = 5
    

    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co, dx, dy):
        super(Monster, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        self.x_lim, self.y_lim = dx, dy
        self.vx = self.run_velocity
        self.vy = self.jump_velocity
        self.x_ori = self.x
        self.y_ori = self.y

    def sim(self, time):
        if abs(self.x_ori - self.x) > self.x_lim:
            vx = -vx
        super(Monster, self).sim(time)

    def collide(self, elem):
        super(Monster, self).collide(elem)
        if isinstance(elem, Player):
            direction = self.touch(elem)
            if direction == 4:
                self.exit = False
            else:
                elem.ch_health(-10)

    
                
                
        

    
            
            
        
        

    
