#!/usr/bin/python3
import json
import numpy as np
from functools import cmp_to_key

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
         
packets = [[], [[2]], [[6]]]
for line in data.split("\n\n"):
    for x in map(json.loads, line.split("\n")):
        packets.append(x)

cmp = cmp_to_key(comparisons)
packets.sort(key=cmp, reverse=True)
print(packets.index([[2]])*packets.index([[6]]))
