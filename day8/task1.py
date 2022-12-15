#!/usr/bin/python3
import numpy as np
with open("case") as f:
    m = np.array(list(map(lambda x: list(map(int, x.strip())), f.readlines())), dtype=int)

def is_visible(i, j):
    return any(max(x, default=m[i][j])<m[i][j] for x in [m[i, :j], m[i, j+1:], m[:i, j], m[i+1:, j]])

visible = 2*(len(m)+len(m[0]))-4
for i in range(1, len(m[0])-1):
    for j in range(1, len(m)-1):
        visible += is_visible(i, j)
print(visible)
