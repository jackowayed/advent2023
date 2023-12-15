#!/usr/bin/env python3

import collections
import fileinput
import re

def update_hash(hash_value, char):
    hash_value += char
    return (hash_value * 17) % 256

def hash(string):
    hash_value = 0
    for c in string:
        hash_value = update_hash(hash_value, ord(c))
    return hash_value

def part1():
    steps = [line.strip() for line in fileinput.input()][0].split(",")
    return sum(hash(step) for step in steps)

def find_label(box, label):
    for i, tup in enumerate(box):
        if tup[0] == label:
            return i
    return None

def part2():
    boxes = []
    for _ in range(256):
        boxes.append(list())
    steps = [line.strip() for line in fileinput.input()][0].split(",")
    for step in steps:
        match = re.match(r"^(\w+)[=|-](\d)?", step)
        label = match.group(1)
        box = hash(label)
        lens = match.group(2)
        i = find_label(boxes[box], label)
        if lens:
            new_tuple = (label, int(lens))
            if i is not None:
                boxes[box][i] = new_tuple
            else:
                boxes[box].append(new_tuple)
        elif i is not None:
            del boxes[box][i]
    power = 0
    for box_no, box in enumerate(boxes):
        for lens_no, lens in enumerate(box):
            power += (box_no + 1 ) * (lens_no + 1) * lens[1]
    return power

#print(part1())
print(part2())