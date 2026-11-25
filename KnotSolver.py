import json

from Knot import *

def main():
    with open("knot.json", "r") as f:
        pieces = json.load(f)["knot"]
    knot = Knot(pieces)

    # crossing_order = knot.notate_crossings()

    print(knot.knot_coords)

if __name__ == "__main__":
    main()