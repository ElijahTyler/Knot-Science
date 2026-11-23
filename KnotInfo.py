import pygame

# tile id_num -> tile type
tile_id_type_dict = {
    0: "empty",
    1: "bar_h",
    2: "bar_v",
    3: "cross_h",
    4: "cross_v",
    5: "l1",
    6: "l2",
    7: "l3",
    8: "l4",
    9: "dot_right",
    10: "dot_up",
    11: "dot_left",
    12: "dot_down",
    13: "dot",
    14: "double_l1",
    15: "double_l2"
}

# tile type -> tile id_num
tile_type_id_dict = {v: k for k, v in tile_id_type_dict.items()}

# key pressed -> tile id_num
keypress_tile_id_dict = {
    pygame.K_z: 0,
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_q: 5,
    pygame.K_w: 6,
    pygame.K_e: 7,
    pygame.K_r: 8,
    pygame.K_v: 9,
    pygame.K_d: 10,
    pygame.K_x: 11,
    pygame.K_c: 12,
    pygame.K_f: 13,
    pygame.K_a: 14,
    pygame.K_s: 15
}

keys = list(keypress_tile_id_dict.keys())

# tile id_num -> adjacencies [right, up, left, down]
# ex: "dot_right": [1, 0, 0, 0]
tile_id_adjacency_dict = {
    0: [0, 0, 0, 0],
    1: [1, 0, 1, 0],
    2: [0, 1, 0, 1],
    3: [1, 1, 1, 1],
    4: [1, 1, 1, 1],
    5: [1, 1, 0, 0],
    6: [0, 1, 1, 0],
    7: [0, 0, 1, 1],
    8: [1, 0, 0, 1],
    9: [1, 0, 0, 0],
    10: [0, 1, 0, 0],
    11: [0, 0, 1, 0],
    12: [0, 0, 0, 1],
    13: [0, 0, 0, 0],
    14: [1, 1, 1, 1],
    15: [1, 1, 1, 1]
}