#!/usr/bin/python3
# positions the tail visits at least once
import numpy as np
import math

x = y = 20
visited = np.array(np.zeros((x, y), dtype=int))

def between(x1, y1, x2, y2):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return max([dx, dy])

with open("test2") as f:
    moves = list(map(str.strip, f.readlines()))

hp, tp = [y//2, y//2], [y//2, y//2]
a = [[y//2,y//2] for _ in range(10)]
visited[y//2, y//2] = 1
for m in moves:
    d, n = m.split(" ")
    n = int(n)
    while n != 0:
        # move head
        hp = a[0]
        if d=="R":
            hp[1]+=1
        elif d=="U":
            hp[0]-=1
        elif d=="L":
            hp[1]-=1
        elif d=="D":
            hp[0]+=1
          
        # move tails
        for i in range(1,10):
            if between(*a[i-1], *a[i])>1:
                print(between(*a[i-1], *a[i]))

        visited[a[-1][0], a[-1][1]] = 1
        print(visited)
        n -= 1

print(np.count_nonzero(visited))
