import Tile as T
import os
import json
import pygame
pygame.init()
maindir = os.path.dirname(os.path.abspath(__file__))
assetdir = os.path.join(maindir, 'assets')

if os.path.exists("knot.json"):
    with open("knot.json", "r") as f:
        current_knot = json.load(f)["knot"]
else:
    current_knot = []
    [current_knot.append([0]*20) for i in range(15)]

blocks_layout = []
[blocks_layout.append([0]*20) for i in range(15)]
for i in range(15):
    for j in range(20):
        blocks_layout[i][j] = T.Tile(current_knot[i][j], i, j)
new_knot = blocks_layout

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Knot Science')

knot_background = pygame.image.load(os.path.join(assetdir, "background.png")).convert()

def make_new_knot_array(knot):
    new_knot_array = []
    [new_knot_array.append([0]*20) for i in range(15)]

    for i in range(15):
        for j in range(20):
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
            if event.key in [pygame.K_0, pygame.K_KP0]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(0, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_1, pygame.K_KP1]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(1, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_2, pygame.K_KP2]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(2, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_3, pygame.K_KP3]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(3, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_4, pygame.K_KP4]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(4, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_5, pygame.K_KP5]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(5, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_6, pygame.K_KP6]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(6, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_7, pygame.K_KP7]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(7, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_8, pygame.K_KP8]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(8, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_RIGHT]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(9, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_UP]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(10, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_LEFT]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(11, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_DOWN]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(12, mouse_ij[0], mouse_ij[1])
            if event.key in [pygame.K_PERIOD, pygame.K_KP_PERIOD]:
                new_knot[mouse_ij[0]][mouse_ij[1]] = T.Tile(13, mouse_ij[0], mouse_ij[1])
            
    screen.blit(knot_background, (0, 0))
    for i in range(15):
        for j in range(20):
            screen.blit(new_knot[i][j].img, new_knot[i][j].img_rect)
    pygame.display.flip()