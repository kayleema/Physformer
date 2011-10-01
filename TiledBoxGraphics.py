from Graphics import Graphics
import pygame

class TiledBoxGraphics(Graphics):
    def __init__(self, elem, pc,  pel,per,peu,ped,  pcul,pcur,pcdl,pcdr):
        self.pics = {}
        self.pics['ctr'] = pygame.image.load(pc).convert_alpha()

        self.pics['el'] = pygame.image.load(pel).convert_alpha()
        self.pics['er'] = pygame.image.load(per).convert_alpha()
        self.pics['eu'] = pygame.image.load(peu).convert_alpha()
        self.pics['ed'] = pygame.image.load(ped).convert_alpha()

        self.pics['cul'] = pygame.image.load(pcul).convert_alpha()
        self.pics['cur'] = pygame.image.load(pcur).convert_alpha()
        self.pics['cdl'] = pygame.image.load(pcdl).convert_alpha()
        self.pics['cdr'] = pygame.image.load(pcdr).convert_alpha()

        self.elem = elem
        self.scale = elem.mylevel.meter

        for pic in self.pics:
            self.pics[pic] = pygame.transform.smoothscale(self.pics[pic], (self.scale, self.scale))

    def draw(self, screen, x, y, w, h):
        elx = int(w // self.scale)
        ely = int(h // self.scale)
        for i in range(0, elx):
            for j in range(0, ely):
                if i == 0 and j == 0:
                    pic_to_draw = self.pics['cul']
                elif i == elx - 1 and j == 0:
                    pic_to_draw = self.pics['cur']
                elif i == 0 and j == ely-1:
                    pic_to_draw = self.pics['cdl']
                elif i == elx-1 and j == ely-1:
                    pic_to_draw = self.pics['cdr']
                elif i == 0:
                    pic_to_draw = self.pics['el']
                elif i == elx-1:
                    pic_to_draw = self.pics['er']
                elif j == 0:
                    pic_to_draw = self.pics['eu']
                elif j == ely-1:
                    pic_to_draw = self.pics['ed']
                else:
                    pic_to_draw = self.pics['ctr']
                #pic_to_draw = self.pics['ctr']
                screen.blit(pic_to_draw, [i*self.scale+x, j*self.scale+y])
