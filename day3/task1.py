#!/usr/bin/python3
import string
import sys

a = "."+string.ascii_lowercase+string.ascii_uppercase
score = 0
for li in open(sys.argv[1]):
    li = li.strip()
    upper = set(li[len(li)//2:])
    for i in range(0, len(li)//2):
        if li[i] in upper:
            score += a.index(li[i])
            break

print(score)
