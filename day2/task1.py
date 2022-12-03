#!/usr/bin/python3
import string

score = 0
for r in open("example_case"):
    a, b = r.strip().split(" ")

    if (a, b) in [("C", "X"), ("A", "Y"), ("B", "Z")]:
        score += 6
    elif (a, b) in [("C", "Z"), ("A", "X"), ("B", "Y")]:
        score += 3
    
    score += ord(b)-ord('W')

print(score)
