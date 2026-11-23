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

def are_adjacent(ij1, ij2):
    return (ij1[0] == ij2[0] and abs(ij1[1]-ij2[1]) == 1) or (ij1[1] == ij2[1] and abs(ij1[0]-ij2[0]) == 1)

def deduce_id_num(knot, mouse_ij, last_ij):
    if last_ij == None or not are_adjacent(mouse_ij, last_ij):
        return 13
    
    # cases
    # q1: last -> current (same dir) OR last -> current (different dir)
    # q2: current is occupied by perpendicular bar OR current is unoccupied

    if knot[mouse_ij[0]][mouse_ij[1]].id_num in [5, 6, 7, 8]: # current is occupied by a corner
        return -1

    # figure out direction of last -> current
    dir = [0, 1][mouse_ij[1] == last_ij[1]] # 0 is horizontal, 1 is vertical
    # LINKED LIST TIME huge news for the Linked List Truthers #LLT2026
    # if we're going horizontal: check the last LAST tile's vertical coordinate to know which L it becomes
    # if we're going vertical: check the last LAST tile's horizontal coordinate to know which L it becomes



global last_ij
last_ij = None

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
        
        if event.type == pygame.MOUSEBUTTONDOWN: # click-and-click for now, click-and-drag perhaps later
            if event.button == 1:
                deduced_id_num = deduce_id_num(new_knot, mouse_ij, last_ij)
                if deduced_id_num != -1:
                    last_ij = mouse_ij
                    new_knot[mouse_ij[0]][mouse_ij[1]] = Tile(deduced_id_num, mouse_ij[0], mouse_ij[1])

    screen.blit(knot_background, (0, 0))
    for i in range(HEIGHT):
        for j in range(WIDTH):
            screen.blit(new_knot[i][j].img, new_knot[i][j].img_rect)
    pygame.display.flip()