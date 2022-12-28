#!/usr/bin/python3
from collections import deque
import numpy as np

def convert(now, then):
    xs, ys = map(lambda x: int(x[0]), np.where(a==now))
    a[xs, ys] = then
    return (xs, ys)

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
xs, ys = convert('S', 'a')
xe, ye = convert('E', 'z')

print(findShortestPath(a, (xs, ys), (xe, ye)))