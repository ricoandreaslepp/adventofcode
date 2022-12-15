#!/usr/bin/python3
import re

total = 0
for li in open("case"):
    a,b,c,d = map(int, re.split(",|-", li.strip()))
    if (a<=c and b>=d) or (a>=c and b<=d):
        total += 1

print(total)
