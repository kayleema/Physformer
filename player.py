from elements import *
from terrain import Terrain
from ImageGraphics import ImageGraphics
from block import Block

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
        self.grounded = False
        self.graphics = ImageGraphics("img/ninja.png", self.w*self.mylevel.meter, self.h*self.mylevel.meter)
        self.picked_up = False
        self.recovery = 0

    def sim(self, time):
        if self.recovery >= 0:
            self.recovery -= time

        #print("Player Position: ", self.x, self.y)
        if self.moveleft:
            self.vx = -self.run_velocity
        elif self.moveright:
            self.vx =  self.run_velocity
        else:
            self.vx = 0

        if self.moveup and self.grounded:
            self.vy = -self.jump_velocity
            self.grounded = False
        self.grounded = False
        
        if self.movedown == True:
            if self.picked_up != False:
                self.picked_up.vx = self.vx
                self.picked_up.vy = self.vy
                self.picked_up = False
                self.movedown = False
            else:
                self.movedown = False
                closest = 0
                closest_dist = 99999
                for element in self.mylevel.elem_list:
                    if isinstance(element, Block):
                        dist = (element.x-self.x)**2+(element.y-self.y)**2
                        if(dist < closest_dist):
                            closest_dist = dist
                            closest = element
                        if closest_dist < 5:
                            #print(closest)
                            closest.x = self.x
                            closest.y = self.top - closest.h
                            closest.update(closest.x, closest.y)
                            self.picked_up = closest

        if self.picked_up != False:
            self.picked_up.x = self.x
            self.picked_up.y = self.top - self.picked_up.h
            self.picked_up.update(self.picked_up.x, self.picked_up.y)
            self.picked_up.vx = 0
            self.picked_up.vy = 0

        super(Player, self).sim(time)

    def ch_health(self, amount):
        """
        change the health with certain amount in case of damage or curation
        """
        if self.recovery > 0:
            return
        self.health +=amount
        self.recovery = 1
        if self.health <= 0:
            #print("DEATH")
            self.mylevel.game_won = False
            self.mylevel.game_over = True

    
    def move(self, elem):
        from monster import Monster
        if isinstance(elem, Monster) and self.touch(elem) == 2:
            Monster.exist = False

        if not isinstance(elem, Terrain):
            super(Player, self).move(elem)

    def collide(self, elem):
        from monster import Monster
        if isinstance(elem, Monster):
            pass
        if not isinstance(elem, Terrain):
            super(Player, self).collide(elem)

    
