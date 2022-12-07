#!/usr/bin/python3
# total size of each directory
# saaks kausta mappiga ID-ga, aga tundub väga palju tööd

m = {'/': {}}
sisu_otsas = False
cur_dir = ['/']
f = open("case")
f.readline()
while True:
    
    if not sisu_otsas:
        li = f.readline().strip()
    sisu_otsas = False

    if not li:
        break

    # we've found a command
    if li[0]=="$":
        cmd = li[2:]
        #print(cmd)

        if "ls" in cmd:
            # loe järgmised vajalikud read
            # kui on failid, siis liida suurused
            while not sisu_otsas:
                li = f.readline().strip()
                if not li:
                    break

                if "dir" in li:
                    x = m
                    for d in cur_dir:
                        x = x[d]
                    x[li[4:]] = {}
                    #print("lisasin", li[4:])
                elif "$" not in li:
                    suurus, nimi = li.split(" ")
                    x = m
                    for d in cur_dir:
                        x = x[d]
                    x[nimi] = int(suurus)
                else:
                    # kausta sisu sai otsa
                    sisu_otsas = True

        elif "cd" in cmd:
            where = li[5:]
            if where=="..":
                cur_dir.pop()
            else:
                cur_dir.append(where)
    else:
        #print(li)
        pass

#print(m)
from math import inf
ans, need_more = inf, 0
# recursively calc size of each directory?
def dir_to_size(g, cur='/'):
    global ans, need_more
    total = 0
    for item in g.values():
        if isinstance(item, dict):
            total += dir_to_size(item)
        else:
            total += item
    
    g[cur] = total
    if total >= need_more:
        ans = min(ans, total)
    return total

import copy
used = dir_to_size(copy.deepcopy(m), '/')
ans = inf
need_more = -40000000+used
dir_to_size(m, '/')
print(ans)


