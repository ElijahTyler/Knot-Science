import json

from KnotPiece import *

def ints_to_tiles(knot):
    new_knot = []
    for i, row in enumerate(knot):
        new_row = []
        for j, cell in enumerate(row):
            new_row.append(Tile(cell, i, j))
        new_knot.append(new_row)
    return new_knot

def find_ends_of_knot(knot):
    ends = []
    for i, row in enumerate(knot):
        for j, cell in enumerate(row):
            if cell.id_num in [9, 10, 11, 12]: # dots are the ends
                ends.append((i, j))
    return ends if len(ends) == 2 else []

def find_regions(knot):
    # identify regions in the 2d view of the knot
    # but! we gotta be careful because of the knot pieces
    # solution: the knot pieces will be included in the INNER regions, not the OUTER region
    
    outer_region = find_outer_region(knot)

    inner_regions = find_inner_regions(knot)

    return outer_region, inner_regions

def find_outer_region(knot):
    outer_region = []
    visited = set()
    stack = [(0, 0)]

    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        outer_region.append((i, j))

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(knot) and 0 <= nj < len(knot[0]) and knot[ni][nj].id_num == 0:
                stack.append((ni, nj))

    return outer_region

def find_inner_regions(knot):
    # the knot pieces create the regions based on the type of knot piece
    # corner piece: 2 regions
    # line/dot: 1 or 2 regions (only ever one region if it's a tail on either end of the knot)
    # overpass: 2, 3 or 4 regions (4 regions minus number of tails it's directly connected to)
    # (directly connected := no crossings between pieces)

    # TODO
    pass

def trace(knot):
    dir = -1

    for i in range(len(knot)):
        for j in range(len(knot[0])):
            if knot[i][j].id_num in [9, 10, 11, 12]: # dots are the ends
                dir = -2
                break
        if knot[i][j].id_num in [9, 10, 11, 12]:
            dir = -2
            break

    if dir == -1: # The Santa Clause
        print("no end pieces found")
        return
    dir = knot[i][j].id_num - 9 # 0 is right, 1 is up, 2 is left, 3 is down

    # i, j are now coordinates for a dot tile, which is the start of the trace
    # (we only needed to find one of them)

    current_i, current_j = i, j
    visited_list = [(i, j)]

    idx_dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)] # right, up, left, down

    while (current_i, current_j) not in find_ends_of_knot(knot) or len(visited_list) == 1:
        # 1. check current tile's adjacency (only one should show up in the direction we're going)
        # 2. go to the new tile 
        # 3. block off the adjacency behind the new tile
        # 4. repeat until we reach the other end of the knot (the other dot tile)

        # 1.
        dir = dir # lmao
        
        # 2.
        di, dj = idx_dirs[dir]
        ni, nj = current_i + di, current_j + dj

        # 3.
        print(ni, nj)
        print(knot[ni][nj].id_num)
        knot[ni][nj].adjacencies[(dir + 2) % 4] = 0

        # 4.
        if knot[ni][nj].id_num in [5, 6, 7, 8]: # corner pieces
            if dir == 0: # right
                if knot[ni][nj].adjacencies[1] == 1: # up
                    dir = 1
                elif knot[ni][nj].adjacencies[3] == 1: # down
                    dir = 3
            elif dir == 1: # up
                if knot[ni][nj].adjacencies[0] == 1: # right
                    dir = 0
                elif knot[ni][nj].adjacencies[2] == 1: # left
                    dir = 2
            elif dir == 2: # left
                if knot[ni][nj].adjacencies[1] == 1: # up
                    dir = 1
                elif knot[ni][nj].adjacencies[3] == 1: # down
                    dir = 3
            elif dir == 3: # down
                if knot[ni][nj].adjacencies[0] == 1: # right
                    dir = 0
                elif knot[ni][nj].adjacencies[2] == 1: # left
                    dir = 2

        current_i, current_j = ni, nj
        visited_list.append((current_i, current_j))

    return visited_list





def main():
    with open("knot.json", "r") as f:
        knot = json.load(f)["knot"]
    knot = ints_to_tiles(knot)

    knot_list = trace(knot)

    print(knot_list)

if __name__ == "__main__":
    main()