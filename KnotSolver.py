import json

from Knot import *

def main():
    with open("knot.json", "r") as f:
        pieces = json.load(f)["knot"]
    knot = Knot(pieces)

    crossings = knot.notate_crossings()

    print(crossings)

if __name__ == "__main__":
    main()