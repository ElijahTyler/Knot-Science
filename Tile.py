import os
import pygame
pygame.init()

from KnotInfo import *

maindir = os.path.abspath(os.path.dirname(__file__))
assetdir = os.path.join(maindir, 'assets')

class Tile:
    def __init__(self, type, x_given, y_given):
        self.id_num = type
        self.type = tile_type_dict[type]
        self.img = pygame.image.load(os.path.join(assetdir, f'{self.type}.png'))
        self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
    
    def get_img(self):
        return self.img
    
    def get_img_rect(self):
        return self.img_rect