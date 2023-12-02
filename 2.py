#!/usr/bin/env python3

import collections
import fileinput
import re

def parse_round(s):
    round = collections.defaultdict(int)
    for part in s.split(","):
        m = re.match(r" (\d+) (\w+)", part)
        round[m.group(2)] = int(m.group(1))
    return round

def impossible(round):
    return round["red"] > 12 or round["green"] > 13 or round["blue"] > 14

def part1():
    # [line.strip() for line in fileinput.input()]
    answer = []
    for line in fileinput.input():
        gid = int(re.match(r"^Game (\d+):", line).group(1))
        parts = line.split(":")[1].split(";")
        #import pdb
        #pdb.set_trace()
        if sum(impossible(parse_round(p)) for p in parts) == 0:
            answer.append(gid)
    print(answer)
    return sum(answer)

def power(rounds):
    colors = ["red", "green", "blue"]
    p = 1
    for c in colors:
        p *= max(r[c] for r in rounds)
    return p


def part2():
    answer = []
    for line in fileinput.input():
        gid = int(re.match(r"^Game (\d+):", line).group(1))
        parts = line.split(":")[1].split(";")
        #import pdb
        #pdb.set_trace()
        rounds = [parse_round(p) for p in parts]
        answer.append(power(rounds))
    print(answer)
    return sum(answer)

#print(part1())
print(part2())