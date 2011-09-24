from element import *

class Player(Element):
    run_velocity = 10
    jump_velocity = 10
    
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        super(Player, self).__init__(x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co)
        # self.ax = acc_x
        # self.ay = acc_y
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        self.health = 100

    def sim(self, time):
        if self.moveleft:
            self.vx -= run_velocity
        if self.moveright:
            self.vx += run_velocity
        if self.moveup:
            self.vy -= jump_velocity
        if self.movedown:
            self.vx += jump_velocity
        super(player, self).sim(time)

    def ch_health(amount):
        """
        change the health with certain amount in case of damage or curation
        """
        self.health +=amount

    
        
        
        
        
        
