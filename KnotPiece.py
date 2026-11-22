import os
import pygame
pygame.init()

from KnotInfo import *

maindir = os.path.abspath(os.path.dirname(__file__))
assetdir = os.path.join(maindir, 'assets')
ldir = os.path.join(assetdir, 'bent_l')

class Tile:
    def __init__(self, id_num, x_given, y_given):
        self.id_num = id_num
        self.type = tile_id_type_dict[id_num]
        if id_num in [5, 6, 7, 8]:
            self.img = pygame.image.load(os.path.join(ldir, f'{self.type}.png'))
        else:
            self.img = pygame.image.load(os.path.join(assetdir, f'{self.type}.png'))
        self.img_rect = pygame.Rect(40*y_given, 40*x_given, 40, 40)
        self.adjacencies = tile_id_adjacency_dict[id_num].copy()
    
    def get_img(self):
        return self.img
    
    def get_img_rect(self):
        return self.img_rect