#!/usr/bin/env python3

import collections
import fileinput
import re

NOT_SYMBOL = frozenset(".0123456789")

def safe_check_symbol(x, y, grid):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return not (grid[y][x] in NOT_SYMBOL)

def has_adjacent_symbol(y, match, grid):
    x_start = match.start()
    x_end = match.end()
    candidates = [(x_start - 1, y), (x_end, y)]
    for _x in range(x_start - 1, x_end +1):
        candidates.append((_x, y - 1))
        candidates.append((_x, y + 1))
    return any(safe_check_symbol(x, y, grid) for x, y in candidates)



def part1():
    grid = [line.strip() for line in fileinput.input()]
    total = 0
    for y, line in enumerate(grid):
        for match in re.finditer(r"\d+", line):
            if has_adjacent_symbol(y, match, grid):
                total += int(match.group(0))
    return total


def part2():
    # [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())