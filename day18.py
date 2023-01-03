# Advent of Code 2022 Day 18
# Soln from: https://github.com/silentw0lf/advent_of_code_2022/blob/main/18/solve.py

import re

#input file is x,y,z coords of 1*1*1 cubes
with open("Day18TestInput.txt") as f:
    cubes = [tuple(map(int, re.findall("(\d+)", l))) for l in f.readlines()]

# find smallest and largest values with a buffer of 1 each side
minout = [min(c[i]-1 for c in cubes) for i in range(3)]
maxout = [max(c[i]+1 for c in cubes) for i in range(3)]


def in_space(cube):
    # check whether this cube is in our space
    # all() returns true if all the items in the list meet the condition
    return all(minout[i] <= cube[i] <= maxout[i] for i in range(3))


def get_neighbors(cube):
# work out what the cubes surrounding this one would be:
    return [tuple(sum(x) for x in zip(cube, d)) for d in \
         [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]


# part 1
exposed = 0
for cube in cubes:
    for n in get_neighbors(cube):
        if n not in cubes: #if the cube that would cover this face is inst in our set then this face is exposed
            exposed += 1

# part 2
exposed_outside = 0
seen = set()
queue = [tuple(maxout)]
while queue:
    curr_cube = queue.pop(0)
    if curr_cube in cubes:
        exposed_outside += 1
        continue
    if curr_cube not in seen:
        seen.add(curr_cube)
        for n in get_neighbors(curr_cube):
            if in_space(n):
                queue.append(n)

print(exposed)
print(exposed_outside)