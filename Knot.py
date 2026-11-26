from KnotPiece import *

class Knot:
    def __init__(self, pieces):
        self.pieces = self.ints_to_tiles(pieces)
        self.knot = self.trace()
        self.knot_coords = self.get_trace_coords()
        self.crossings = self.notate_crossings()

    def ints_to_tiles(self, knot):
        new_knot = []
        for i, row in enumerate(knot):
            new_row = []
            for j, cell in enumerate(row):
                new_row.append(Tile(cell, i, j))
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

        return visited_list

    def get_dir(self, last_ij, curr_ij):
        d = {(0, 1): 0, (-1, 0): 1, (0, -1): 2, (1, 0): 3}

        i = curr_ij[0] - last_ij[0]
        j = curr_ij[1] - last_ij[1]

        return d[(i, j)]

    def notate_crossings(self):
        crossing_order = []
        seen_crosses = {}

        index = 1

        last_ij = None
        dir = -1

        for t in self.knot:
            curr_ij = t.coords
            if last_ij is not None:
                dir = self.get_dir(last_ij, curr_ij)
            
            if t.id_num in [3, 4]: # crossings
                if t not in seen_crosses:
                    seen_crosses[t] = index
                    index += 1

                if (t.id_num == 3 and dir in [0, 2]) or (t.id_num == 4 and dir in [1, 3]):
                    path = 'over'
                else:
                    path = 'under'

                crossing_order.append((seen_crosses[t], dir, path)) # crossing index, direction, over/under

            last_ij = curr_ij

        return crossing_order

    def get_trace_coords(self):
        l = []
        for k in self.knot:
            l.append(k.coords)
        return l
    
    def reidemeister(self):
        pass