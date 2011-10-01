from Graphics import Graphics
import pygame

class ImageGraphics(Graphics):
    def __init__(self, filename, w, h):
        self.pic = pygame.image.load(filename).convert_alpha()
        self.pic = pygame.transform.smoothscale(self.pic, (w, h))
    def draw(self, screen, x, y, w, h):
        screen.blit(self.pic, [x, y])
