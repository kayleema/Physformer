import pygame

class Graphics(object):
    def __init__(self, element):
        self.color = (0, 255, 0)
        self.elem = element
    def draw(self, screen, x, y, w, h):
        #print("drawing at: ", x, y, w, h, self.elem)
        """draws a rectangle representation of the element defined in the
        constructor
        """
        pygame.draw.rect(screen,self.color,[x,y,w,h],2)
