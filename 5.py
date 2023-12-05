#!/usr/bin/env python3

import collections
import fileinput
import re

class Range:
    def __init__(self, dst_start, src_start, length):
        self.dst_start = dst_start
        self.src_start = src_start
        self.length = length

    def in_range(self, src):
        return src >= self.src_start and src < self.src_start + self.length
    
    def translate(self, src):
        if not self.in_range(src):
            return None
        return src - self.src_start + self.dst_start
    
def translate(src, ranges):
    for r in ranges:
        if r.translate(src) is not None:
            return r.translate(src)
    return src

def ints_from_line(line):
    return list(map(int, re.findall(r"\d+", line)))

def read_map(iter):
     # skip map name
    line = next(iter)
    map = []
    while len(line) > 2:
        dest_start, src_start, length = ints_from_line(line)
        map.append(Range(dest_start, src_start, length))
        try:
            line = next(iter)
        except StopIteration:
            return map
    return map

def resolve_seed(seed, maps):
    l = seed
    for m in maps:
        l = translate(l, m)
    return l


def part1():
    # [line.strip() for line in fileinput.input()]
    t = 0
    iter = fileinput.input()
    seeds_raw = next(iter)
    seeds = ints_from_line(seeds_raw)
    next(iter)
    maps = []
    try:
        while "map" in next(iter):
            maps.append(read_map(iter))
    except StopIteration:
        pass
    return min(resolve_seed(s, maps) for s in seeds)


def part2():
    # [line.strip() for line in fileinput.input()]
    t = 0
    for line in fileinput.input():
        pass
    return t

print(part1())
#print(part2())