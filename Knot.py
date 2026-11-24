from KnotPiece import *

class Knot:
    def __init__(self, pieces):
        self.pieces = self.ints_to_tiles(pieces)
        self.knot = self.trace()

    def ints_to_tiles(self, knot):
        new_knot = []
        for i, row in enumerate(knot):
            new_row = []
            for j, cell in enumerate(row):
                new_row.append(Tile(cell, i, j))
            new_knot.append(new_row)
        return new_knot

    def find_tile(self, i, j):
        i = 0
        while self.pieces[i].coords != [i, j]:
            i += 1
        return self.pieces[i]

    def find_ends_of_knot(self):
        ends = []
        for i, row in enumerate(self.pieces):
            for j, cell in enumerate(row):
                if cell.id_num in [9, 10, 11, 12]: # dots are the ends
                    ends.append(self.pieces[i][j])
        return ends if len(ends) == 2 else []

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
            # only change direction if we're at a corner
            if self.pieces[current_i][current_j].id_num in [5, 6, 7, 8]: # corner pieces
                dir = self.pieces[current_i][current_j].adjacencies.index(1)

        return visited_list

    def notate_crossings(self):
        crossing_order = []
        seen_crosses = {}

        index = 1

        for t in self.knot:
            if t.id_num in [3, 4]: # crossings
                if t not in seen_crosses:
                    seen_crosses[t] = index
                    index += 1
                crossing_order.append(seen_crosses[t])

        return crossing_order