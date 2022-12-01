#!/usr/bin/python3

ans, i = 0, 0

for elf in open("puzzle1"):
    if elf.strip()=='':
        ans = max(ans, i)
        i = 0
        continue

    i += int(elf.strip())

print(ans)
