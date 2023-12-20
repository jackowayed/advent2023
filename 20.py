#!/usr/bin/env python3

import collections
import functools
import fileinput
import math
import re

Module = collections.namedtuple("Module", ["name", "type", "dests"])
Pulse = collections.namedtuple("Pulse", ["src", "dest", "is_high"])

FF = "flipflop"
CONJ = "conjunction"
BROADCASTER = "broadcaster"

graph = dict()
reverse_graph = collections.defaultdict(set)
state = dict()
low_count = high_count = 0

def bfs(pulses):
    import pdb
    #pdb.set_trace()
    pulses = collections.deque(pulses)
    while pulses:
        p = pulses.popleft()
        #print(p)
        new_pulses = process(p.src, p.dest, p.is_high)
        #print(new_pulses)
        pulses.extend(new_pulses)

def process(src, dest, is_high):
    print((src, dest, is_high))
    global graph
    global state
    global low_count
    global high_count
    if is_high:
        high_count += 1
    else:
        low_count += 1
    if dest not in graph:
        # for output in the test file
        return []
    dest = graph[dest]
    if dest.type == BROADCASTER:
        return [Pulse(dest.name, d, False) for d in dest.dests]
    elif dest.type == FF and not is_high:
        is_on = state.get(dest.name, False)
        state[dest.name] = not is_on
        return [Pulse(dest.name, d, not is_on) for d in dest.dests]
    elif dest.type == CONJ:
        if is_high:
            state[dest.name].add(src)
        else:
            state[dest.name].discard(src)
        send_high = len(state[dest.name]) != len(reverse_graph[dest.name])
        return [Pulse(dest.name, d, send_high) for d in dest.dests]
    return []
            

            

def part1():
    lines = [line.strip() for line in fileinput.input()]
    for line in lines:
        src, dest = line.split(" -> ")
        name = src[1:]
        if src == "broadcaster":
            name = typ = BROADCASTER
        elif src.startswith("%"):
            typ = FF
        elif src.startswith("&"):
            typ = CONJ
            state[name] = set()
        else:
            assert False, line
        graph[name] = Module(name, typ, dest.split(", "))
        for d in graph[name].dests:
            reverse_graph[d].add(name)
    for _ in range(1000):
        bfs([Pulse(None, BROADCASTER, False)])
    global low_count
    global high_count
    print(low_count)
    print(high_count)
    return low_count * high_count


def part2():
    lines = [line.strip() for line in fileinput.input()]
    for line in lines:
        pass
    return

print(part1())
#print(part2())