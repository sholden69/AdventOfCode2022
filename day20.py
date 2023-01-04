
# Advent of Code Day 20
# https://adventofcode.com/2022/day/20
# courtesy of https://github.com/silentw0lf/advent_of_code_2022/blob/main/20/solve.py


from itertools import cycle

dec_key = 811589153


def solve(task):
    rounds, multiply = (1, 1) if task == 1 else (10, dec_key)
    with open("Day20Input.txt") as f:
        numbers = [int(n) * multiply for n in f.readlines()]
    mixed = [a for a in enumerate(numbers)]
    cyc = cycle(mixed.copy())
    zero_tuple = (numbers.index(0), 0)
    lm = len(mixed) - 1

    for _ in range(rounds * len(numbers)):
        curr = next(cyc)
        idx_old = mixed.index(curr)
        mixed.remove(curr)
        idx_new = (idx_old + curr[1] + lm) % lm
        mixed.insert(idx_new, curr)

    idx_zero_tuple = mixed.index(zero_tuple)
    print(sum([mixed[(idx_zero_tuple + i) % len(numbers)][1]
          for i in [1000, 2000, 3000]]))


solve(task=1)
solve(task=2)