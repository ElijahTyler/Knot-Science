import os
import pygame
pygame.init()

maindir = os.path.abspath(os.path.dirname(__file__))
assetdir = os.path.join(maindir, 'assets')

class Tile:
    def __init__(self, type, x_given, y_given):
        self.id_num = type
        match type:
            case 0:
                self.type = None
                self.img = pygame.image.load(os.path.join(assetdir, 'empty.png'))
                self.img.set_colorkey((255, 0, 0))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 1:
                self.type = 'bar_h'
                self.img = pygame.image.load(os.path.join(assetdir, 'bar_h.png'))
                self.collision = True
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 2:
                self.type = 'bar_v'
                self.img = pygame.image.load(os.path.join(assetdir, 'bar_v.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 3:
                self.type = 'over_h'
                self.img = pygame.image.load(os.path.join(assetdir, 'over_h.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 4:
                self.type = 'over_v'
                self.img = pygame.image.load(os.path.join(assetdir, 'over_v.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 5:
                self.type = 'l1'
                self.img = pygame.image.load(os.path.join(assetdir, 'l1.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 6:
                self.type = 'l2'
                self.img = pygame.image.load(os.path.join(assetdir, 'l2.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 7:
                self.type = 'l3'
                self.img = pygame.image.load(os.path.join(assetdir, 'l3.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 8:
                self.type = 'l4'
                self.img = pygame.image.load(os.path.join(assetdir, 'l4.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 9:
                self.type = 'dot_right'
                self.img = pygame.image.load(os.path.join(assetdir, 'dot_right.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 10:
                self.type = 'dot_up'
                self.img = pygame.image.load(os.path.join(assetdir, 'dot_up.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 11:
                self.type = 'dot_left'
                self.img = pygame.image.load(os.path.join(assetdir, 'dot_left.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 12:
                self.type = 'dot_down'
                self.img = pygame.image.load(os.path.join(assetdir, 'dot_down.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
            case 13:
                self.type = 'dot'
                self.img = pygame.image.load(os.path.join(assetdir, 'dot.png'))
                self.collision = False
                self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
    
    def get_img(self):
        return self.img
    
    def get_img_rect(self):
        return self.img_rect