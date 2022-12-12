#!/usr/bin/python3
from math import floor

class monkey:
    items = ops = test = t = f = None
    total = 0
    
## throw to the end of a monkey's list
## divided by 3 and rounded to nearest int
m = []
f = open("case")
while True:
    mk = monkey()
    if not f.readline():
        break
    
    mk.items = list(map(int, f.readline()[18:].strip().split(", ")))
    mk.ops = f.readline()[19:].strip()
    mk.test = int(f.readline()[21:].strip())
    mk.t = int(f.readline()[29:].strip())
    mk.f = int(f.readline()[30:].strip())
    
    m.append(mk)

    f.readline()

for rnd in range(10000):
    for i in range(len(m)):
        for j in range(len(m[i].items)):        
            m[i].total += 1
            old = m[i].items.pop(0)
            old = eval(m[i].ops)
            #print(old)
            if old%m[i].test==0:
                m[m[i].t].items.append(old)
                #print("thrown to monkey", m[i].t)
            else:
                m[m[i].f].items.append(old)
                #print("thrown to monkey", m[i].f)

    print("after round", rnd)
    print([m[xi].total for xi in range(len(m))])

totals = sorted(m[i].total for i in range(len(m)))
print(totals[-1]*totals[-2])
f.close()

