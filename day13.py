# https://adventofcode.com/2022/day/13
from collections import defaultdict
from functools import cmp_to_key


def lrComp(left,right):
    # -1 = success - in right order; 1=failure; 0=inconclusive
    # can then use this as the sort function for part 2
    # https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/
    #print("comp left",left,"right",right)

    print("comp",left,right)
    if type(left) == type(right) == int:
        if left < right:
            return -1
        elif  left > right:
            return 1
        else:
            return 0
    elif type(left) == type(right) == list:
        n = len(left)
        m = len(right)
        res = 0
        for i in range(min(n, m)):
            res = lrComp(left[i], right[i])
            if res:  #either -1 or +1 - we've got a result
                break
        if res == 0: #we didnt get a result so check which list ran out or not
            if n < m: #ran out on the LHS so success
                return -1
            elif n > m:  #ran nout on the RHS so failure
                return 1
            else: return 0  #inconclusive so keep going
    elif type(left) == int: #int + a list 
        res = lrComp([left], right)
    else:   #list + an int
        res = lrComp(left, [right])
    return res

FILE="Day13TestInput.txt"
#part 1
with open(FILE) as f:
    raw_pairs = f.read().split("\n\n")
pairs=[p.split("\n")for p in raw_pairs]
mySum=0
for idx,p in enumerate(pairs):
    if lrComp(eval(p[0]),eval(p[1]))==-1:
        mySum+=idx+1
print("matching score",mySum) 

# Part 2
d = defaultdict(list)
with open(FILE) as file:
    lines = [line.strip() for line in file.readlines()]
for i, line in enumerate(lines):
    if not line:
        continue
    d[i] = eval(line)
# add in the two dividers
d[i+1] = [[2]]
d[i+2] = [[6]]
# sort the dicionary using our function
a = sorted(d.values(), key=cmp_to_key(lrComp))
# find the two indices straight after the dividers
i = a.index([[2]]) + 1
j = a.index([[6]]) + 1
print(i * j)


