#!/usr/bin/env python
#Advent of Code Day25: https://adventofcode.com/2022/day/25
# Courtesy of https://github.com/viliampucik/adventofcode/blob/master/2022/25.py
SNAFU = "=-012"

s1, s = "", sum(
    sum(5**i * (SNAFU.index(c) - 2) for i, c in enumerate(n[::-1]))
    for n in open("Day25Input.txt").read().splitlines()
)

while s:
    s, m = divmod(s + 2, 5)
    s1 = SNAFU[m] + s1

print(s1)