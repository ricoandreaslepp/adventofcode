#!/usr/bin/python3
# after which character do we have 4 different last chars
from collections import deque

def check(q):
    return len(set(q))==14

def case():
    dq = deque(list(li[:14]))
    if check(dq):
        return 14

    for i in range(14, len(li.strip())):
        dq.popleft()
        dq.extend(li[i])
        if check(dq):
            return i+1
        

for li in open("case"):
    print(case())
