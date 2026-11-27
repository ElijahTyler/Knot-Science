import json

from KnotPiece import *
from Crossing import *
from KnotEditor import make_new_knot_array

class Knot:
    def __init__(self, pieces):
        self.pieces = self.ints_to_tiles(pieces)
        self.update()

    def update(self):
        self.knot = self.trace()
        self.knot_coords = self.get_trace_coords()
        self.crossings = self.notate_crossings()

    def ints_to_tiles(self, knot):
        new_knot = []
        for i, row in enumerate(knot):
            new_row = []
            for j, cell in enumerate(row):
                new_row.append(KnotPiece(cell, i, j))
            new_knot.append(new_row)
        return new_knot

    def find_ends_of_knot(self):
        ends = []
        for i, row in enumerate(self.pieces):
            for j, cell in enumerate(row):
                if cell.id_num in [9, 10, 11, 12]: # dots are the ends
                    ends.append(self.pieces[i][j])
        return ends if len(ends) == 2 else []

    def find_regions(self):
        # identify regions in the 2d view of the knot
        # but! we gotta be careful because of the knot pieces
        # solution: the knot pieces will be included in the INNER regions, not the OUTER region
        
        outer_region = self.find_outer_region()

        inner_regions = self.find_inner_regions()

        return outer_region, inner_regions

    def find_outer_region(self):
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
                if 0 <= ni < len(self.pieces) and 0 <= nj < len(self.pieces[0]) and self.pieces[ni][nj].id_num == 0:
                    stack.append((ni, nj))

        return outer_region

    def find_inner_regions(self):
        # the knot pieces create the regions based on the type of knot piece
        # corner piece: 2 regions
        # line/dot: 1 or 2 regions (only ever one region if it's a tail on either end of the knot)
        # overpass: 2, 3 or 4 regions (4 regions minus number of tails it's directly connected to)
        # double corners: 2 or 3 regions
        # (directly connected := no crossings between pieces)

        # TODO
        pass

    def trace(self):
        end_pieces = self.find_ends_of_knot()

        if end_pieces == []: # The Santa Clause
            print("no end pieces found")
            return
        
        dir = end_pieces[0].id_num - 9 # 0 is right, 1 is up, 2 is left, 3 is down

        # i, j are now coordinates for a dot tile, which is the start of the trace
        # (we only needed to find one of them)

        current_i, current_j = end_pieces[0].coords
        visited_list = [end_pieces[0]]

        idx_dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)] # right, up, left, down

        while (current_i, current_j) != end_pieces[1].coords or len(visited_list) == 1:
            # 1. check current tile's adjacency (only one should show up in the direction we're going)
            # 2. go to the new tile 
            # 3. block off the adjacency behind the new tile
            # 4. repeat until we reach the other end of the knot (the other dot tile)

            # 1.
            di, dj = idx_dirs[dir]
            
            # 2.
            ni, nj = current_i + di, current_j + dj
            current_i, current_j = ni, nj
            visited_list.append(self.pieces[current_i][current_j])

            # 3.
            self.pieces[current_i][current_j].adjacencies[(dir + 2) % 4] = 0

            # 4.
            # only change direction if we're at a corner or double corner
            curr_id_num = self.pieces[current_i][current_j].id_num
            if curr_id_num in [5, 6, 7, 8]: # corner pieces
                dir = self.pieces[current_i][current_j].adjacencies.index(1)
            if curr_id_num in [14, 15]: # double corners
                if curr_id_num == 14: # double corner 1 (l1 + l3)
                    dir = 3 - dir
                if curr_id_num == 15: # double corner 2 (l2 + l4)
                    dir = [1, 0, 3, 2][dir]

        for v in visited_list:
            v.reset_adjacencies()

        return visited_list

    def get_dir(self, last_ij, curr_ij):
        d = {(0, 1): 0, (-1, 0): 1, (0, -1): 2, (1, 0): 3}

        i = curr_ij[0] - last_ij[0]
        j = curr_ij[1] - last_ij[1]

        return d[(i, j)]

    def notate_crossings(self):
        crossing_order = []
        seen_crossings = {}

        index = 1

        last_ij = None
        dir = -1

        for t in self.knot:
            curr_ij = t.coords
            if last_ij is not None:
                dir = self.get_dir(last_ij, curr_ij)
            
            if t.id_num in [3, 4]: # crossings
                if t not in seen_crossings:
                    seen_crossings[t] = index
                    index += 1

                if (t.id_num == 3 and dir in [0, 2]) or (t.id_num == 4 and dir in [1, 3]):
                    path = 'over'
                else:
                    path = 'under'

                crossing_order.append(Crossing(t, seen_crossings[t], dir, path)) # knot piece, crossing index, direction, over/under

            last_ij = curr_ij

        return crossing_order

    def get_trace_coords(self):
        l = []
        for k in self.knot:
            l.append(k.coords)
        return l
    
    def reidemeister(self, change=True, moves_to_check=[1,2,3]):
        changelog = [] # (old knot piece, new knot piece)
        new_changes_found = True
        # move 1: twist / untwist string
        # move 2: move middle of string over/under another line of string
        # move 3: move middle of string to other side of crossing

        while new_changes_found:
            new_changes_found = False
            
            # for move 1, check for adjacent crossings of same crossing index
            # if i find two, connect the two directions of what i found
            if 1 in moves_to_check:
                for t in range(len(self.crossings) - 1):
                    if (self.crossings[t].index != self.crossings[t + 1].index):
                        continue

                    dir1 = self.crossings[t].dir
                    dir2 = self.crossings[t + 1].dir

                    d = (dir1 + dir2) % 4 # FIXME
                    coords_to_change = self.crossings[t].knot_piece.coords

                    if d == 1:
                        new_kp = KnotPiece(14, coords_to_change[0], coords_to_change[1])
                    if d == 3:
                        new_kp = KnotPiece(15, coords_to_change[0], coords_to_change[1])

                    new_changes_found = True
                    changelog.append((self.pieces[coords_to_change[0]][coords_to_change[1]], new_kp))
                    if change:
                        self.pieces[coords_to_change[0]][coords_to_change[1]] = new_kp
                        self.update()
                        break

            # for move 2, check for adjacent crossings of same path
            if 2 in moves_to_check:
                for t in range(len(self.crossings) - 1):
                    if (self.crossings[t].path != self.crossings[t + 1].path):
                        continue
                    if (self.crossings[t].dir == self.crossings[t + 1].dir):
                        continue
                    if (self.crossings[t].knot_piece.id_num not in [3, 4]) or (self.crossings[t + 1].knot_piece.id_num not in [3, 4]):
                        continue

                    print('potential match found for reidemeister move 2')
                    print(self.crossings[t].knot_piece.coords, self.crossings[t + 1].knot_piece.coords)
                    # print('id nums:')
                    # print(self.crossings[t].knot_piece.id_num, self.crossings[t + 1].knot_piece.id_num)

                    # each crossing has 2 directions
                    # make sure the two directions are the terminals of one of the double corners
                    coords_1_dir_a = self.crossings[t].dir
                    coords_1_dir_b = None
                    coords_2_dir_a = self.crossings[t + 1].dir
                    coords_2_dir_b = None

                    for c in self.crossings:
                        if (c.knot_piece.coords == self.crossings[t].knot_piece.coords) and (c.dir != self.crossings[t].dir):
                            coords_1_dir_b = c.dir
                        if (c.knot_piece.coords == self.crossings[t + 1].knot_piece.coords) and (c.dir != self.crossings[t + 1].dir):
                            coords_2_dir_b = c.dir

                    if coords_1_dir_b == None or coords_2_dir_b == None:
                        print("i've met a terrible fate")
                        return

                    print(coords_1_dir_a, coords_1_dir_b)
                    print(coords_2_dir_a, coords_2_dir_b)

                    dir1 = (coords_1_dir_a + coords_1_dir_b) % 4 # FIXME
                    dir2 = (coords_2_dir_a + coords_2_dir_b) % 4 # FIXME

                    coords1 = self.crossings[t].knot_piece.coords
                    coords2 = self.crossings[t + 1].knot_piece.coords

                    if dir1 == 1:
                        new_kp1 = KnotPiece(14, coords1[0], coords1[1])
                    if dir1 == 3:
                        new_kp1 = KnotPiece(15, coords1[0], coords1[1])
                    if dir2 == 1:
                        new_kp2 = KnotPiece(14, coords2[0], coords2[1])
                    if dir2 == 3:
                        new_kp2 = KnotPiece(15, coords2[0], coords2[1])

                    new_changes_found = True
                    changelog.append((self.pieces[coords1[0]][coords1[1]], new_kp1))
                    changelog.append((self.pieces[coords2[0]][coords2[1]], new_kp2))
                    if change:
                        self.pieces[coords1[0]][coords1[1]] = new_kp1
                        self.pieces[coords2[0]][coords2[1]] = new_kp2
                        self.update()
                        break

            # for move 3, ???
            if 3 in moves_to_check:
                pass

        # redraw all that jawn into jsawn
        self.update()
        make_new_knot_array(self.pieces)
        new_dict = {"knot": make_new_knot_array(self.pieces)}
        json_object = json.dumps(new_dict)

        with open("knot.json", "w") as outfile:
            outfile.write(json_object)

        return changelog