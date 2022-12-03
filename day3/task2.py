#!/usr/bin/python3
import string
import sys

a = "."+string.ascii_lowercase+string.ascii_uppercase
score = 0
f = open(sys.argv[1])
while x := f.readline().strip():
    s = set(x)
    for _ in range(2):
        s = s.intersection(set(f.readline().strip()))
    score += a.index(list(s)[0])

f.close()
print(score)
