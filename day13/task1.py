#!/usr/bin/python3
"""
if both are ints
    left<right -> right order
    right>left -> wrong order
    else       -> continue
if both are lists
    repeat first
    left runs out  -> right order 
    right runs out -> wrong order
    same len       -> continue
else
    convert int to list -> repeat snd step
"""
# has to be recursive
# True : "right order", False : "wrong order"
def comparisons(l1, l2):
    print(f"comparing {l1} {l2}")
    for x, y in zip(l1, l2):
        if isinstance(x, int) and isinstance(y, int):
            if x<y:
                return True
            elif x>y:
                return False
        elif isinstance(x, list) and isinstance(y, list):
            if len(x)==0:
                return True
            elif len(y)==0:
                return False
            # compare the lists themselves
            inner = comparisons(x, y)
            if inner!=None:
                return inner 

        else:
            # one of them is integer
            # still needs additions
            if isinstance(l1, list):
                return comparisons(l1, [l2])
            elif isinstance(l2, list):
                return comparisons([l1], l2)

f = open("test_case")
while True:
    p1 = eval(f.readline().strip())
    p2 = eval(f.readline().strip())
    more = f.readline()
    print(comparisons(p1, p2))

    if not more:
        break
