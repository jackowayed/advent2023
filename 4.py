#!/usr/bin/env python3

import collections
import fileinput
import re


def part1():
    # [line.strip() for line in fileinput.input()]
    t = 0
    for line in fileinput.input():
        line = line.split(":")[1]
        winning, mine = line.split("|")
        winning_n = {int(n) for n in winning.strip().split(" ") if n}
        mine_n = [int(n) for n in mine.strip().split(" ") if n]
        num_winning = len([n for n in mine_n if n in winning_n])
        if num_winning:
            t += 2 ** (num_winning-1)
    return t


def part2():
    t = 0
    line_num = 0
    copies = collections.defaultdict(int)
    for line in fileinput.input():
        t += 1
        line = line.split(":")[1]
        winning, mine = line.split("|")
        winning_n = {int(n) for n in winning.strip().split(" ") if n}
        mine_n = [int(n) for n in mine.strip().split(" ") if n]
        num_winning = len([n for n in mine_n if n in winning_n])
        for i in range(line_num + 1, line_num + num_winning + 1):
            copies[i] += copies[line_num] + 1
        t += copies[line_num]
        line_num += 1
    return t
    # [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

#print(part1())
print(part2())