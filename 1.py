#!/usr/bin/env python3

import collections
import fileinput
import re


def part1():
    t = 0
    for line in fileinput.input():
        print(line)
        first = None
        last = None
        for c in line:
            if c.isdigit():
                first = c
                break
        for c in reversed(line):
            if c.isdigit():
                last = c
                break
        t += int(first + last)
    return

def first_num(s, from_end=False):
    NUMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if from_end:
        s = s[::-1]
        NUMS = [n[::-1] for n in NUMS]
    best_idx = None
    best_n = None
    for i in range(1, 10):
        idx = s.find(str(i))
        if idx > -1 and (best_idx is None or best_idx > idx):
            best_idx = idx
            best_n = i
    for n, nstr in enumerate(NUMS):
        idx = s.find(nstr)
        if idx > -1 and (best_idx is None or best_idx > idx):
            best_idx = idx
            best_n = n + 1
    return best_n
    

def part2():
    t = 0
    import pdb
    pdb.set_trace()
    for line in fileinput.input():
        f = first_num(line)
        l = first_num(line, True)
        print((f, l))
        t += 10 * f + l
    return t

#print(part1())
print(part2())