"""This file has element class which contains everything you can see
"""

class Element():
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, world_name):
        """
        initialize everything
        x_co, y_co: the center coordinates.
        w_co, h_co: the width and height.
        vx_co, vy_co: speed to 2 coordinates.
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
        self.up = y_co + h_co/2
        self.down = y_co - h_co/2
        self.graphics = Graphics(self)

    def update(x1, y1):
        """
        update the position of element
        """
        self.x = x1
        self.y = y1
        self.left = self.x - self.w/2
        self.right = self.x + self.w/2
        self.up = self.y + self.h/2
        self.down = self.y - self.h/2
        
        
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
        return true if the two elements are touched by the other
        """
        other_l = elem.get_left()
        otehr_r = elem.get_right()
        other_u = elem.get_up()
        other_d = elem.get_down()
        if in_inter(other_l, self.l, self.r) or in_inter(other_r, self_l, self_r) or in_inter(other_u, self.down, self.up) or in_inter(other_d, self.down, self.up):
            return True
        return False

    def move(self, elem):
        """
        move something out of another element under the presumption that those two elements are overlapped
        """
        l = elem.
        if self.vx >= 0: # the element is moving towards right
            x1 = 
            
        
        
        

    def sim(time):
        """
        simulate the element move in the certain direction for certain time.
        REMEMBER TO CHECK!
        """
        x1 = self.x + time * self.vx
        y1 = self.y + time * self.vy
        update(x1, y1)
        
        

    def within_screen(self, scr_left, scr_right):
        """
        return True if the element is in screen; False otherwise.
        scr_left: the left bound of the screen
        scr_right: the right bound of the screen
        """
        if in_inter(self.left, scr_left, scr_right) and in_inter(self.right, scr_left, scr_right):
            return True
        return False
    

    def draw(screen, x, y):
        graphics.draw(screen, x, y)

    
    
    
    
    

    

    
