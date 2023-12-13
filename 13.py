#!/usr/bin/env python3

import collections
import fileinput
import re

def read_input():
    lines = [line.strip() for line in fileinput.input()]
    grids = []
    cur_grid = []
    i = 0
    for line in lines:
        if not line:
            grids.append(cur_grid)
            cur_grid = []
        else:
            cur_grid.append(line)
    if cur_grid:
        grids.append(cur_grid)
    return grids
    
def is_reflection_after(grid, i):
    before = i
    after = i + 1
    while before >= 0 and after < len(grid):
        if grid[before] != grid[after]:
            return False
        before -= 1
        after += 1
    return True
    

def solve_horiz(grid, skipped):
    for i in range(len(grid) - 1):
        if skipped is not None and skipped == i + 1:
            continue
        if is_reflection_after(grid, i):
            return i + 1
    return -1


def rotate(grid):
    new_grid = []
    for new_row in range(len(grid[0])):
        s = []
        for new_col in range(len(grid)):
            s.append(grid[new_col][new_row])
        new_grid.append(s)
    return new_grid

def score(g):
    rotated = rotate(g)
    v = solve_horiz(rotated, None)
    if v > 0:
        return v
    else:
        h = solve_horiz(g, None)
        assert h > 0
        return h * 100


def part1():
    grids = read_input()
    s = 0
    for g in grids:
        s += score(g)
    return s

def smudge_score(g, y, x, skipped_score):
    grid = [[c == "#" for c in s] for s in g]
    grid[y][x] = not grid[y][x]
    rotated = rotate(grid)
    skipped = None if skipped_score >= 100 else skipped_score
    v = solve_horiz(rotated, skipped)
    if v > 0:
       return v
    skipped = None if skipped_score < 100 else skipped_score // 100
    h = solve_horiz(grid, skipped)
    if h > 0:
        return h * 100

def solve_smudged(g):
    skipped_score = score(g)
    for y in range(len(g)):
        for x in range(len(g[0])):
            s = smudge_score(g, y, x, skipped_score)
            if s:
                return s
    assert False


def part2():
    grids = read_input()
    score = 0
    for g in grids:
        score += solve_smudged(g)
    return score

#print(part1())
print(part2())