import os
import pygame
pygame.init()

maindir = os.path.abspath(os.path.dirname(__file__))
assetdir = os.path.join(maindir, 'assets')

tile_type_dict = {
    0: "empty",
    1: "bar_h",
    2: "bar_v",
    3: "over_h",
    4: "over_v",
    5: "l1",
    6: "l2",
    7: "l3",
    8: "l4",
    9: "dot_right",
    10: "dot_up",
    11: "dot_left",
    12: "dot_down",
    13: "dot"
}

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