#!/usr/bin/python3
import json

# 1: right order, -1: wrong order, 0: continue
def comparisons(l1, l2):       
    # both ints
    if isinstance(l1, int) and isinstance(l2, int):
        if l1<l2:
            return 1
        elif l1>l2:
            return -1
        
        return 0
        
    # one int
    if isinstance(l1, int):
        l1 = [l1]
    elif isinstance(l2, int):
        l2 = [l2]
    
    # both lists
    for x, y in zip(l1, l2):
        pair = comparisons(x, y)
        if pair==0:
            continue
        return pair
    
    if len(l1)<len(l2):
        return 1
    elif len(l2)<len(l1):
        return -1
    
    return 0
       
with open("case") as f:
    data = f.read().strip()
         
ans = 0
for i, line in enumerate(data.split("\n\n"), start=1):
    x1, x2 = map(json.loads, line.split("\n"))
    if comparisons(x1, x2)==1:
        ans += i
print(ans)
