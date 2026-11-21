import json

def find_ends_of_knot(knot):
    ends = []
    for i, row in enumerate(knot):
        for j, cell in enumerate(row):
            if cell.type in [9, 10, 11, 12]: # dots are the ends
                ends.append((i, j))
    return ends if len(ends) == 2 else []

def main():
    with open("knot.json", "r") as f:
        knot = json.load(f)["knot"]