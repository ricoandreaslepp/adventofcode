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
    i = 0
    while True:
        print(f"comparing {l1} {l2}")
        # siin probleem
        if len(l1)==i and len(l2)==i:
            return None

        if i>=len(l1):
            return True
        elif i>=len(l2):
            return False

        x, y = l1[i], l2[i]
        if isinstance(x, int) and isinstance(y, int):
            if x<y:
                return True
            elif x>y:
                return False
        elif isinstance(x, list) and isinstance(y, list):
            if len(x)==0 and len(y)==0:
                return None

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
            if isinstance(x, list):
                return comparisons(x, [y])
            elif isinstance(y, list):
                return comparisons([x], y)
        
        i += 1

i, ans = 1, 0
f = open("case")
while True:
    p1 = eval(f.readline().strip())
    p2 = eval(f.readline().strip())
    more = f.readline()
    if comparisons(p1, p2): 
        ans += i
        print("\n")
    else:
        print(i)
        print(p1)
        print(p2)
        print("False ^", end="\n\n")
    if not more:
        break

    i += 1

print(ans)
