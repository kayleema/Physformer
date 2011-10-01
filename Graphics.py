import pygame

class Graphics(object):
    def __init__(self, element):
        self.color = (0, 0, 0)
        self.elem = element
    def draw(self, screen, x, y, w, h):
        from Spike import Spike
        #print("drawing at: ", x, y, w, h, self.elem)
        """draws a rectangle representation of the element defined in the
        constructor
        """
        if isinstance(self.elem, Spike):
            print(y)
        pygame.draw.rect(screen,self.color,[int(x),int(y),w,h],2)
