#!/usr/bin/python3
# positions the tail visits at least once
import numpy as np
import math

x = y = 50
visited = np.array(np.zeros((x, y), dtype=int))

def between(x1, y1, x2, y2):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return max([dx, dy])

with open("example") as f:
    moves = list(map(str.strip, f.readlines()))

hp, tp = [y//2, y//2], [y//2, y//2]
visited[y//2, y//2] = 1
for m in moves:
    d, n = m.split(" ")
    n = int(n)
    while n != 0:
        if d=="R" and hp[1]+1<x:
            hp[1]+=1
            if between(*hp, *tp)>1:
                tp[1]+=1
                if hp[0]>tp[0]:
                    tp[0]+=1
                elif hp[0]<tp[0]:
                    tp[0]-=1
        elif d=="U" and hp[0]-1>=0:
            hp[0]-=1
            if between(*hp, *tp)>1:
                tp[0]-=1
                if hp[1]>tp[1]:
                    tp[1]+=1
                elif hp[1]<tp[1]:
                    tp[1]-=1
        elif d=="L" and hp[1]-1>=0:
            hp[1]-=1
            if between(*hp, *tp)>1:
                tp[1]-=1
                if hp[0]>tp[0]:
                    tp[0]+=1
                elif hp[0]<tp[0]:
                    tp[0]-=1
        elif d=="D" and hp[0]+1<x:
            hp[0]+=1
            if between(*hp, *tp)>1:
                tp[0] = (tp[0]+1)%y
                if hp[1]<tp[1]:
                    tp[1]-=1
                elif hp[1]>tp[1]:
                    tp[1]+=1
        visited[tp[0], tp[1]] = 1
        print(visited)
        n -= 1

print(np.count_nonzero(visited))
