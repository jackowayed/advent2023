#!/usr/bin/env python3

import collections
import fileinput
import re


def part1():
    # [line.strip() for line in fileinput.input()]
    iter = fileinput.input()
    sequence = next(iter).strip()
    next(iter)
    tree = dict()
    for line in iter:
        node, left, right = re.findall(r"\w\w\w", line)
        tree[node] = (left, right)
    cur = "AAA"
    ct = 0
    while cur != "ZZZ":
        step = sequence[ct % len(sequence)]
        if step == "L":
            cur = tree[cur][0]
        elif step == "R":
            cur = tree[cur][1]
        else:
            assert False, step
        ct += 1
    return ct


def part2():
    # [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())