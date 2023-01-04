#!/usr/bin/env pypy3
#Advent of Code 2022 Day 24: https://adventofcode.com/2022/day/24
#courtesy of: https://github.com/viliampucik/adventofcode/blob/master/2022/24.py
def solve(start, stop, step):
    #find our way from start to stop in the smallest nuber of steps
    positions = set([start]) #initialise set with our starting point

    while True:
        next_positions = set()
        for r, c in positions:
            # try moving in all directions, starting with stannding still.
            for x, y in ((r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (x, y) == stop: # if we've made it to end then stop
                    return step
                # fmt:off
                # use step modulo width/height to see where the blizzards are.
                # if this is a legitimate  move then add this to the next set of positions.
                if 0 <= x < height and 0 <= y < width \
                   and grid[x][(y - step) % width] != ">" \
                   and grid[x][(y + step) % width] != "<" \
                   and grid[(x - step) % height][y] != "v" \
                   and grid[(x + step) % height][y] != "^":
                    next_positions.add((x, y))
                # fmt:on
        positions = next_positions
        if not positions: #if nowhere to go then jump back to the start
            positions.add(start)
        step += 1


#read in the grid, find height and width and start, stop.
grid = [row[1:-1] for row in open("Day24Input.txt").read().splitlines()[1:-1]]
height, width = len(grid), len(grid[0])
start, stop = (-1, 0), (height, width - 1)

print(s1 := solve(start, stop, 1))
print(solve(start, stop, solve(stop, start, s1)))