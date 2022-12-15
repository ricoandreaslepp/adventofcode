#!/usr/bin/python3
# total of top 3 elves
import heapq

ans, i = [], 0
heapq.heapify(ans)

for elf in open("puzzle1"):
    if elf.strip()=='':
        heapq.heappush(ans, i)
        i = 0
        continue

    i += int(elf.strip())

print(sum(heapq.nlargest(3, ans)))
