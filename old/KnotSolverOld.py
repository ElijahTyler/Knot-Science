import json

from KnotPiece import *

def ints_to_tiles(knot):
    new_knot = []
    for i, row in enumerate(knot):
        new_row = []
        for j, cell in enumerate(row):
            new_row.append(KnotPiece(cell, i, j))
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
    # double corners: 2 or 3 regions
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
        di, dj = idx_dirs[dir]
        
        # 2.
        ni, nj = current_i + di, current_j + dj
        current_i, current_j = ni, nj
        visited_list.append((current_i, current_j))

        # 3.
        knot[current_i][current_j].adjacencies[(dir + 2) % 4] = 0

        # 4.
        # only change direction if we're at a corner
        if knot[current_i][current_j].id_num in [5, 6, 7, 8]: # corner pieces
            dir = knot[current_i][current_j].adjacencies.index(1)

    return visited_list

def notate_crossings(knot):
    crossing_order = []
    seen_crosses = {}
    traced_knot = trace(knot)

    index = 1

    for t in traced_knot:
        if knot[t[0]][t[1]].id_num in [3, 4]: # crossings
            if t not in seen_crosses:
                seen_crosses[t] = index
                index += 1
            crossing_order.append(seen_crosses[t])

    return crossing_order



def main():
    with open("knot.json", "r") as f:
        knot = json.load(f)["knot"]
    knot = ints_to_tiles(knot)

    crossing_order = notate_crossings(knot)

    print(crossing_order)

if __name__ == "__main__":
    main()