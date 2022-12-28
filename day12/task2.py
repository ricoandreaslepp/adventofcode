#!/usr/bin/python3
from collections import deque
import numpy as np
from math import inf

def convert(now, then):
    xs, ys = map(lambda x: int(x[0]), np.where(a==now))
    a[xs, ys] = then
    return (xs, ys)

# shortest path from any 'a' to 'E'
def findShortestPath(a, start, end):
    q = deque([(start, 0)])
    visited = set()
    
    while q:      
        (i, j), steps = q.popleft()
        
        if (i, j) == end:
            return steps
                
        possible_moves = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
        for x, y in possible_moves:
            if x in range(0,n) and y in range(0,m) and all([(x, y) not in visited, ord(a[x,y])-ord(a[i,j]) <= 1]):
                q.append(((x, y), steps+1))
                # before I was generating a huge queue and only then putting these items to the visited list
                visited.add((x, y))

a = []
for li in open("case"):
    a.append(list(li.strip()))
a = np.array(a)

n, m = len(a), len(a[0])
xe, ye = convert('E', 'z')

best = inf
for (x, y) in zip(*np.where(a=='a')):
    current = findShortestPath(a, (x, y), (xe, ye))
    if current:
        best = min(best, current)
print(best)