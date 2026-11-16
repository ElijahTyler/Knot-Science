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
9: dot_r
10: dot_u
11: dot_l
12: dot_d
13: dot
'''

import json

with open("knot.json", "r") as f:
    knot = json.load(f)["knot"]

