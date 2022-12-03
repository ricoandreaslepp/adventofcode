#!/usr/bin/python3
import string

lose = {"A": "Z", "B": "X", "C":"Y"}
win = {"A": "Y", "B": "Z", "C": "X"}

score = 0
for r in open("example_case"):
    a, b = r.strip().split(" ")

    if b=='X': # lose
        score += ord(lose[a])-ord('X')+1
    if b=='Y':
        score += ord(a)-ord('A')+1
        score += 3
    if b=='Z': # win
        score += ord(win[a])-ord('X')+1
        score += 6
    

print(score)
