#!/usr/bin/env python
#Advent of Code Day25: https://adventofcode.com/2022/day/25
# Courtesy of https://github.com/viliampucik/adventofcode/blob/master/2022/25.py
SNAFU = "=-012"



def smartPart1():
    # translate SNAFU to decimal and sum in s
    s1, s = "", sum(
        sum(5**i * (SNAFU.index(c) - 2) for i, c in enumerate(n[::-1]))
        for n in open("Day25Input.txt").read().splitlines()
    )

    # reverse integer s into output string s1
    while s:
        #The divmod() method takes two numbers as arguments and returns their quotient and remainder in a tuple.
        s, m = divmod(s + 2, 5)
        s1 = SNAFU[m] + s1

    print(s1)

def unpickPart1():
    s1, s = "", sum(
        sum(5**i * (SNAFU.index(c) - 2) for i, c in enumerate(n[::-1]))
        for n in open("Day25Input.txt").read().splitlines()
    )

    s=0
    lines=open("Day25Input.txt").read().splitlines()
    s=0
    for n in lines: 
        for i,c in enumerate(n[::-1]):
            thisVal=5**i * (SNAFU.index(c)-2)
            s+=thisVal

    while s:
        s, m = divmod(s + 2, 5)
        s1 = SNAFU[m] + s1

    print(s1)


smartPart1()
