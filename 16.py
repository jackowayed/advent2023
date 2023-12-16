#!/usr/bin/env python3

import collections
import enum
import functools
import fileinput
import math
import re

import sys
sys.setrecursionlimit(10000)

#class Direction(enum.Enum):
UP = (-1, 0)
LEFT = (0, -1)
DOWN = (1, 0)
RIGHT = (0, 1)

#DIRECTIONS = [d for d in Direction]
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

def direction_index(d):
    return DIRECTIONS.index(d)

def clockwise(d):
    return DIRECTIONS[(direction_index(d) + 1) % len(DIRECTIONS)]

def counter_clockwise(d):
    return DIRECTIONS[(direction_index(d) - 1) % len(DIRECTIONS)]


class Square:
    def __init__(self, thing):
        self.thing = thing
        self.beams = set()

    def add_beam(self, direction):
        if direction in self.beams:
            return True
        self.beams.add(direction)
        return False
    
    def is_energized(self):
        return bool(len(self.beams))
    
def maybe_move_from(y, x, direction, grid):
    looped = grid[y][x].add_beam(direction)
    if not looped:
        move_to(y + direction[0], x + direction[1], direction, grid)

def is_clockwise(thing, direction):
    return (thing == "/" and direction in (UP, DOWN)) or (
        thing == "\\" and direction in (LEFT, RIGHT)
    )


def move_to(y, x, direction, grid):
    print(y,x)
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]):
        return
    square = grid[y][x]
    if square.thing == "." or (
      square.thing == "-" and direction in (LEFT, RIGHT) or (
     square.thing == "|") and direction in (UP, DOWN)):
        maybe_move_from(y, x, direction, grid)
    elif square.thing == "\\" or square.thing == "/":
        new_direction = clockwise(direction) if is_clockwise(square.thing, direction) else counter_clockwise(direction)
        maybe_move_from(y, x, new_direction, grid)
    else:
        maybe_move_from(y, x, clockwise(direction), grid)
        maybe_move_from(y, x, counter_clockwise(direction), grid)

    
def print_energy(grid):
    energy_grid = ["".join(["#" if s.is_energized() else "." for s in row]) for row in grid]
    for row in energy_grid:
        print(row)

def part1():
    lines = [line.strip() for line in fileinput.input()]
    grid = [[Square(c) for c in line] for line in lines]
    move_to(0, 0, RIGHT, grid)
    print_energy(grid)
    return sum(sum(s.is_energized() for s in row) for row in grid)


def part2():
    lines = [line.strip() for line in fileinput.input()]
    for line in lines:
        pass
    return

print(part1())
print(part2())