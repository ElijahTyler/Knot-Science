import os
import json
import pygame
pygame.init()

from KnotPiece import *
from KnotInfo import *

maindir = os.path.dirname(os.path.abspath(__file__))
assetdir = os.path.join(maindir, 'assets')

HEIGHT = 15
WIDTH = 20

if os.path.exists("knot.json"):
    with open("knot.json", "r") as f:
        current_knot = json.load(f)["knot"]
else:
    current_knot = []
    [current_knot.append([0]*WIDTH) for i in range(HEIGHT)]

blocks_layout = []
[blocks_layout.append([0]*WIDTH) for i in range(HEIGHT)]
for i in range(HEIGHT):
    for j in range(WIDTH):
        blocks_layout[i][j] = KnotPiece(current_knot[i][j], i, j)
new_knot = blocks_layout

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Knot Science')

knot_background = pygame.image.load(os.path.join(assetdir, "background.png")).convert()

def make_new_knot_array(knot):
    new_knot_array = []
    [new_knot_array.append([0]*WIDTH) for i in range(HEIGHT)]

    for i in range(HEIGHT):
        for j in range(WIDTH):
            new_knot_array[i][j] = knot[i][j].id_num
    
    return new_knot_array

while True:
    mouse = pygame.mouse.get_pos()
    mouse_ij = [mouse[1]//40, mouse[0]//40]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            new_dict = {"knot": make_new_knot_array(new_knot)}
            json_object = json.dumps(new_dict)

            with open("knot.json", "w") as outfile:
                outfile.write(json_object)

            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                new_knot[mouse_ij[0]][mouse_ij[1]] = KnotPiece(keypress_tile_id_dict[event.key], mouse_ij[0], mouse_ij[1])

    screen.blit(knot_background, (0, 0))
    for i in range(HEIGHT):
        for j in range(WIDTH):
            screen.blit(new_knot[i][j].img, new_knot[i][j].img_rect)
    pygame.display.flip()