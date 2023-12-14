#!/usr/bin/env python3

import collections
import fileinput
import re

def weight(grid):
    w = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                w += len(grid) - y
    return w

def print_grid(grid):
    for y in range(len(grid)):
        print("".join(grid[y]))



def part1():
    grid = [ [c for c in line.strip()] for line in fileinput.input()]
    for x in range(len(grid[0])):
        did_move = True
        while did_move:
            did_move = False
            next_rock_place = None
            for y in range(len(grid)):
                if grid[y][x] == "." and next_rock_place is None:
                    next_rock_place = y
                elif grid[y][x] == "O" and next_rock_place is not None:
                    grid[y][x] = "."
                    grid[next_rock_place][x] = "O"
                    did_move = True
                    next_rock_place = None
                elif grid[y][x] == "#":
                    next_rock_place = None
    #print_grid(grid)
    return weight(grid)



def part2():
    # [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())