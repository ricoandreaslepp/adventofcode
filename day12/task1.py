#!/usr/bin/python3
from collections import deque
import numpy as np

def find_and_convert(item, to_what, a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==item:
                a[i][j] = to_what
                return (i, j)

def findShortestPath(a, start, end):
    q = deque([(start, 0)])
    visited = set()
    
    while q:      
        (i, j), steps = q.popleft()
        
        if (i, j) == end:
            return steps
                
        possible_moves = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
        for x, y in possible_moves:
            if (x, y) not in visited:
                if x>=0 and x<n and y>=0 and y<m:
                    if a[x][y]-a[i][j] <= 1:
                        q.append(((x, y), steps+1))
                        # before I was generating a huge queue and only then putting these items to the visited list
                        visited.add((x, y))

a = []
for li in open("case"):
    a.append(list(map(ord, li.strip())))

n, m = len(a), len(a[0])
xs, ys = find_and_convert(ord('S'), ord('a'), a)
xe, ye = find_and_convert(ord('E'), ord('z'), a)

print(findShortestPath(a, (xs, ys), (xe, ye)))