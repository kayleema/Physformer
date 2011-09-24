from Graphics import Graphics
import pygame

class TiledGraphics(Graphics):
    def __init__(self, path, w_op, h_op):
        self.pic = pygame.image.load(path).convert_alpha()
        self.width  = w_op
        self.height = h_op
    def draw(self, screen, x, y, w, h):
        elx = w // self.width
        ely = h // self.height
        for i in range(0, elx):
            for j in range(0, ely):
                screen.blit(self.pic, [i*self.width+x, j*self.height+y])
