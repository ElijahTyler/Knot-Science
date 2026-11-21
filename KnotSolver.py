import json

from Tile import *

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
            if cell.type in [9, 10, 11, 12]: # dots are the ends
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
    dir = -1 # 0 is horizontal, 1 is vertical

    for i in range(len(knot)):
        for j in range(len(knot[0])):
            if knot[i][j].id_num in [9, 10, 11, 12]: # dots are the ends
                break
        if knot[i][j].id_num in [9, 10, 11, 12]:
            break

    if dir == -1: # The Santa Clause
        print("no end pieces found")
        return

    # i, j are coordinates for a dot tile, which is the start of the trace
    # and we only need to find one of them

    # TODO
    pass

def main():
    with open("knot.json", "r") as f:
        knot = json.load(f)["knot"]
    knot = ints_to_tiles(knot)

    r = find_outer_region(knot)
    print(r)

    trace(knot)

if __name__ == "__main__":
    main()