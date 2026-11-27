import json

from Knot import *

def main():
    with open("knot.json", "r") as f:
        pieces = json.load(f)["knot"]
    knot = Knot(pieces)

    # for c in knot.crossings:
    #     print(c)

    # knot.reidemeister(True)

    # for k in knot.knot:
    #     print(k.coords)

    v = knot.trace(knot.pieces[0][1], True)
    for k in v:
        print(k.coords)

if __name__ == "__main__":
    main()