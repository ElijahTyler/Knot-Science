from Tile import *
import os
import json
import pygame

pygame.init()
maindir = os.path.dirname(os.path.abspath(__file__))
assetdir = os.path.join(maindir, 'assets')

HEIGHT = 15
WIDTH = 20

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

key_tile_dict = {
    pygame.K_0: 0,
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_RIGHT: 9,
    pygame.K_UP: 10,
    pygame.K_LEFT: 11,
    pygame.K_DOWN: 12,
    pygame.K_PERIOD: 13
}
keys = list(key_tile_dict.keys())

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
        blocks_layout[i][j] = Tile(current_knot[i][j], i, j)
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
                new_knot[mouse_ij[0]][mouse_ij[1]] = Tile(key_tile_dict[event.key], mouse_ij[0], mouse_ij[1])

    screen.blit(knot_background, (0, 0))
    for i in range(HEIGHT):
        for j in range(WIDTH):
            screen.blit(new_knot[i][j].img, new_knot[i][j].img_rect)
    pygame.display.flip()