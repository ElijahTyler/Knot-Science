from KnotPiece import *

class Crossing:
    def __init__(self, knot_piece: KnotPiece, index, dir, path):
        self.knot_piece = knot_piece
        self.index = index
        self.dir = dir
        self.path = path

    def __str__(self):
        return f"coords: {self.knot_piece.coords}, index: {self.index}, dir: {self.dir}, path: {self.path}"