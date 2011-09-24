from Graphics import Graphics
import pygame

class ImageGraphics(Graphics):
    def __init__(self, filename):
        self.pic = pygame.image.load(filename).convert_alpha()
    def draw(self, screen, x, y, w, h):
        screen.blit(self.pic, [x, y])
