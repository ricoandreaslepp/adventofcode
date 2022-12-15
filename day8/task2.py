#!/usr/bin/python3
import numpy as np
with open("case") as f:
    m = np.array(list(map(lambda x: list(map(int, x.strip())), f.readlines())), dtype=int)

def calc_score(l):
    x = 0
    for elem in l:
        x += 1
        if elem>=m[i][j]:
            break
    return x

def scenic_score(i, j):
    total = 1
    for l in [np.flip(m[i, :j]), m[i, j+1:], np.flip(m[:i, j]), m[i+1:, j]]:
        total *= calc_score(l)
    return total

score = 0
for i in range(1, len(m[0])-1):
    for j in range(1, len(m)-1):
        score = max(score, scenic_score(i, j))
print(score)
