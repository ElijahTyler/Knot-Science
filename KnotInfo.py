import pygame

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