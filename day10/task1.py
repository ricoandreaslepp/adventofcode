#!/usr/bin/python3
# signal strengths
x, c = 1, 0
strength = 0
cycles = [(20+40*i) for i in range(6)]

with open("case") as f:
    ins = list(map(str.strip, f.readlines()))

def check():
    global c, strength
    c += 1
    if c in cycles:
        strength += (c*x)
    

for i in ins:
    if i=="noop":
        check()
        continue
    
    for _ in range(2):
        check()
    x += int(i[4:])

print(strength)
