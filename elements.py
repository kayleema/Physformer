"""This file has element class which contains everything you can see
"""

class Element():
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, world_name, c_co):
        """
        initialize everything
        x_co, y_co: the center coordinates.
        w_co, h_co: the width and height.
        vx_co, vy_co: speed to 2 coordinates.
        c_co: coefficient of restitution
        """
        self.x = x_co
        self.y = y_co
        self.w = w_co
        self.h = h_co
        self.vx = vx_co
        self.vy = vy_co
        sefl.myworld = world_name
        self.left = x_co - w_co/2
        self.right = x_co + w_co/2
        self.up = y_co - h_co/2
        self.down = y_co + h_co/2
        self.graphics = Graphics(self)
        self.m = mass
        self.c = c_co

    def update(x1, y1):
        """
        update the position of element
        """
        self.x = x1
        self.y = y1
        self.left = self.x - self.w/2
        self.right = self.x + self.w/2
        self.up = self.y - self.h/2
        self.down = self.y + self.h/2
        
        
    """
    get everything you want
    """
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_w(self):
        return self.w
    def get_h(self):
        return self.h
    def get_vx(self):
        return self.vx
    def get_vy(self):
        return self.vy
    def get_myworld(self):
        return self.myworld
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def get_up(self):
        return self.up
    def get_down(self):
        return self.down

    def in_inter(x, a, b):
        """
        return true when x is inside the interval [a, b]
        """
        assert a <= b, 'Invalid interval'
        if x >= a and x <= b:
            return True
        return False
    
    
    
    

    def touch(self, elem):
        """
        return true if the two elements are overlapped by the other
        """
        other_l = elem.get_left()
        otehr_r = elem.get_right()
        other_u = elem.get_up()
        other_d = elem.get_down()
        # horizontal overlap
        horiz = in_inter(self.left, other_l, otehr_r) or in_inter(other_l, self.left, self.right) or in_inter(self.right, other_l, other_r) or in_inter(other_r, self.left, self.right)
        # vertical overlap
        vert = in_inter(self.up, other_d, other_u) or in_inter(self.down, other_d, other_u) or in_inter(other_d, self.down, self.up) or (other_u, self.down, self.up)
        if horiz and vert:
            return True
        return False

    def move(self, elem):
        """
          move something out of another element under the presumption that those two elements are overlapped
        """
        l = elem.left
        r = elem.right
        u = elem.up
        d = elem.down
        if self.vx >= 0: # the element is moving towards right
            x1 = l - self.w/2
        else:
            
            
        

    def phy_for(va, vb, ma, mb, coef):
        """
        take in objects a and b's speed and mass and return the speed for object b
        coef is the coefficient of restitution which is the average of the c of two elements
        """
        v = (coef * ma * (va - vb) + ma * va + mb * vb) / (ma + mb)
        return v
        


    def collide(self, elem):
        """
        modify the other element's speed; return nothing
        """
        coef = (self.c + elem.c)/2
        elem.vx = phy_for(self.vx, elem.vx, self.ma, self.mb, coef)
        elem.vy = phy_for(self.vy, elem.vy, self.ma, self.mb, coef)d
            
        
        
        

    def sim(self, time):
        """
        simulate the element move in the certain direction for certain time.
        REMEMBER TO CHECK!
        """
        x1 = self.x + time * self.vx
        y1 = self.y + time * self.vy
        update(x1, y1)
        
        

    def within_screen(self, scr_left, scr_right, scr_top, scr_bot):
        """
        return True if the element is in screen; False otherwise.
        scr_left: the left bound of the screen
        scr_right: the right bound of the screen
        """
        if in_inter(self.left, scr_left, scr_right) or in_inter(self.right, scr_left, scr_right) or in_inter(self.up, scr_bot, scr_top) or in_inter(self.down, scr_bot, scr_top):
            return True
        return False
    

    def draw(screen, x, y, w, h):
        """
        convey the arguments x and y to graphics function to draw things.
        """
        graphics.draw(screen, x, y, w, h)

    
    
    
    
    

    

    
