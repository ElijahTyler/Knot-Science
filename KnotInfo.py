'''
0: empty
1: h
2: v
3: h over
4: v over
5: l1
6: l2
7: l3
8: l4
9: dot_right
10: dot_up
11: dot_left
12: dot_down
13: dot
'''

import json

with open("knot.json", "r") as f:
    knot = json.load(f)["knot"]

def find_ends_of_knot(knot):
    ends = []
    for i in range(len(knot)):
        if knot[i] == 0:
            ends.append(i)
    return ends