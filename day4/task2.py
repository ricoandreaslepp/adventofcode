#!/usr/bin/python3
import re

total = 0
for li in open("case"):
    values = list(map(int, re.split(",|-", li.strip())))
    if values[0]>values[2]:
        values = [values[2], values[3], values[0], values[1]]
    new = sorted(values.copy())
    #print(values, new, (new!=values) or len(set(new))==2)
    if new!=values or len(set(new))==2 or values[1]==values[2]:
        total += 1

print(total)
