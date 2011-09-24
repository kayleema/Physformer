from Graphics import Graphics
"""This file has element class which contains everything you can see
"""

class Element(object):
    def __init__(self, x_co, y_co, w_co, h_co, vx_co, vy_co, mass, level_co, c_co):
        """
        initialize everything
        x_co, y_co: the center coordinates.
        w_co, h_co: the width and height.
        vx_co, vy_co: speed to 2 coordinates.
        c_co: coefficient of restitution
        """

        self.w = w_co
        self.h = h_co
        self.vx = vx_co
        self.vy = vy_co
        self.mylevel = level_co
        self.graphics = Graphics(self)
        self.m = mass
        self.c = c_co
        self.update(x_co, y_co)

    def update(self, x1, y1):
        """
        update the position of element
        """
        self.x = x1
        self.y = y1
        self.left = self.x - self.w/2
        self.right = self.x + self.w/2
        self.top = self.y - self.h/2
        self.bottom = self.y + self.h/2
        
        
    def in_inter(self, x, a, b):
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
        gapright =  self.right - elem.left
        gapleft =   elem.right - self.left
        gaptop =    self.top - other.bottom
        gapbottom = elem.top - self.bottom
        if gapleft > 0 and gapright > 0 and gaptop > 0 and gapbottom > 0:
            if min(gapleft, gapright) < min(gaptop, gapbottom):
                #collision horizontal
                if gapleft < gapright:
                    return 3
                else:
                    return 1
            else:
                #collision vertical
                if gaptop < gapbottom:
                    return 2
                else:
                    return 4
        else:
            return 0
    
    def touch_ammount(self, elem):
        gapright =  self.right - elem.left
        gapleft =   elem.right - self.left
        gaptop =    self.top - other.bottom
        gapbottom = elem.top - self.bottom
        direction =  self.touch(elem)
        if direction == 0:
            return 0
        elif direction == 1:
            return gapright
        elif direction == 2:
            return gaptop
        elif direction == 3:
            return gapleft
        elif direction == 4:
            return gapbottom
        else:
            assert False, "invalid direction"

    def move(self, elem):
        """
          move something out of another element under the presumption that those two elements are overlapped
          return nothing
        """
        if isinstance(elem, Terrain):
            return
        direction = self.touch(elem)
        ammount = self.touch_ammount(elem)
        if direction == 0:
            return
        elif direction == 1:
            elem.x += ammount
        elif direction == 2:
            elem.y -= ammount
        elif direction == 3:
            elem.x -= ammount
        elif direction == 4:
            elem.y += ammount
        else:
            assert False, "invalid direction"

        elem.update(elem.x, elem.y)
            

    def phy_for(self, va, vb, ma, mb, coef):
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
        if isinstance(elem, Terrain):
            return
        direction = self.touch(elem)
        coef = (self.c + elem.c)/2
        if direction == 1 or direction == 3:
            elem.vx = self.phy_for(self.vx, elem.vx, self.ma, self.mb, coef)
        elif direction == 2 or direction == 4:
            elem.vy = self.phy_for(self.vy, elem.vy, self.ma, self.mb, coef)
        else:
            return

    def sim(self, time):
        """
        simulate the element move in the certain direction for certain time.
        REMEMBER TO CHECK!
        """
        self.vy += self.mylevel.g * time
        x1 = self.x + time * self.vx
        y1 = self.y + time * self.vy
        self.update(x1, y1)
        
        

    def within_screen(self, scr_left, scr_right, scr_top, scr_bot):
        """
        return True if the element is in screen; False otherwise.
        scr_left: the left bound of the screen
        scr_right: the right bound of the screen
        """
#TODO:  Fixme
        return True
    

    def draw(self, screen, x, y, w, h):
        """
        convey the arguments x and y to graphics function to draw things.
        """
        self.graphics.draw(screen, x, y, w, h)

    
