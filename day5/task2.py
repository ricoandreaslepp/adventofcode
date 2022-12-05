#!/usr/bin/python3
# move creates, output each top
# map of stacks
import re

f = open("case")
g = {}
for li in f:
    # read by 3/4 chars
    if not li.strip():
        break
    
    for i in range(0, len(li.strip("\n")), 4):
        if li[i]!=' ':
            g[(i//4)+1] = [li[i+1:i+2]] + g.get((i//4)+1, [])
        else:
            continue    

# not one at a time anymore with CrateMover9001
for li in f:
    _, n, _, a, _, b = li.strip().split(" ")
    n, a, b = map(int, [n,a,b])
    g[b] = g.get(b) + g[a][len(g[a])-n:]
    g[a] = g[a][:len(g[a])-n]

for i in range(1, max(g.keys())+1):
    print(g[i][-1], end="")
print()
f.close()
