import json

from Knot import *

def main():
    with open("knot.json", "r") as f:
        pieces = json.load(f)["knot"]
    knot = Knot(pieces)

    for c in knot.crossings:
        print(c)

if __name__ == "__main__":
    main()