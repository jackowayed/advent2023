#!/usr/bin/env python3

import collections
import functools
import fileinput
import re


#@functools.cache
#def ways()

def distance(time_held, total_time):
    return time_held * (total_time - time_held)

def ints_from_line(line):
    return list(map(int, re.findall(r"\d+", line)))

def combined_ints_from_line(line):
    return int("".join(str(i) for i in ints_from_line(line)))

def part1():
    iter = fileinput.input()
    times = ints_from_line(next(iter))
    distances = ints_from_line(next(iter))
    product = 1
    for t, d in zip(times, distances):
        ways = 0
        for held_time in range(t):
            ways += distance(held_time, t) > d
        product *= ways
    return product


def part2():
    iter = fileinput.input()
    time = combined_ints_from_line(next(iter))
    dist = combined_ints_from_line(next(iter))
    ways = 0
    for held_time in range(time):
        ways += distance(held_time, time) > dist
    return ways

    return

#print(part1())
print(part2())