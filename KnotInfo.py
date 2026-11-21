import pygame

# tile id_num -> tile type
tile_id_type_dict = {
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

# tile type -> tile id_num
tile_type_id_dict = {v: k for k, v in tile_id_type_dict.items()}

# key pressed -> tile id_num
keypress_tile_id_dict = {
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
    13: [0, 0, 0, 0]
}