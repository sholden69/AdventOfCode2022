"""
Day 16: Proboscidea Volcanium
https://adventofcode.com/2022/day/16
https://github.com/ephemient/aoc2022/blob/main/py/aoc2022/day16.py

"""

import heapq
import math
import re
from collections import defaultdict
from dataclasses import dataclass

PATTERN = re.compile(
    r"Valve (\w+) has flow rate=(\d+); "
    r"(?:tunnel leads to valve|tunnels lead to valves) (\w+(?:, \w+)*)"
)

SAMPLE_INPUT = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II",
]


def _parse(lines):
    return {
        (match := re.match(PATTERN, line)).group(1): (
            int(match.group(2)),
            match.group(3).split(", "),
        )
        for line in lines
    }


def _distances(adj):
    # creates store of shortest distance between each valve
    keys, distances = set(), defaultdict(lambda: math.inf)
    # loop through for each source and the list of dests on each source
    for src, dsts in adj:
        keys.add(src)
        distances[src, src] = 0  #distance to itself is zero
        for dst, weight in dsts:
            keys.add(dst)
            distances[dst, dst] = 0
            distances[src, dst] = weight
    
    # check every three step move
    for mid in keys:
        for src in keys:
            for dst in keys:
                distance = distances[src, mid] + distances[mid, dst]
                if distance < distances[src, dst]:
                    distances[src, dst] = distance
    return distances


@dataclass(order=True, frozen=True)
class _State:
    rooms: tuple[tuple[str, int]]
    valves: frozenset[str]
    flow: int
    total: int
    time: int


def _solve(lines, num_agents, total_time):
    # pylint: disable=too-many-branches,too-many-nested-blocks,too-many-locals
    # parse each valve, flow_value + list of connecting valves
    graph = _parse(lines) 

    #calculate the distances between each pair of valves. pass in a generator object
    # inner generator products srd, dst from each line in the file 
    # out loop then simply returns src,dst
    distances = _distances(
        (src, ((dst, 1) for dst in dsts)) for src, (_, dsts) in graph.items()
    )
    print(f"distances {distances}")
    seen, max_seen = set(), 0
    heap = [
        (
            0,
            _State(
                rooms=(("AA", 0),) * num_agents,
                valves=frozenset(src for src, (flow, _) in graph.items() if flow > 0),
                flow=0,
                total=0,
                time=total_time,
            ),
        )
    ]

    while heap:
        estimate, state = heapq.heappop(heap)
        estimate = -estimate
        if state in seen: #if weve been here before then skip
            continue
        seen.add(state)
        potential = estimate + sum(    #try all the valves from here
            max(
                (
                    graph[valve][0] * (state.time - delta - 1)
                    for room, age in state.rooms
                    if (delta := distances[room, valve] - age) in range(state.time)
                ),
                default=0,
            )
            for valve in state.valves
        )
        if estimate > max_seen: #record what the biggest pressure release was
            max_seen = estimate
        if potential < max_seen:
            continue

        moves_by_time = defaultdict(lambda: defaultdict(list))
        for valve in state.valves:
            for i, (room, age) in enumerate(state.rooms):
                delta = distances[room, valve] - age
                if delta in range(state.time):
                    moves_by_time[delta][i].append(valve)
        if not moves_by_time:
            continue

        for delta, moves_by_agent in moves_by_time.items():
            indices = [None] * num_agents
            while True:
                for i, index in enumerate(indices):
                    index = 0 if index is None else index + 1
                    if index < len(moves_by_agent[i]):
                        indices[i] = index
                        break
                    indices[i] = None
                else:
                    break
                valves = [
                    (i, moves_by_agent[i][index])
                    for i, index in enumerate(indices)
                    if index is not None
                ]
                if len(valves) != len(set(valve for _, valve in valves)):
                    continue
                new_rooms = [(room, age + delta + 1) for room, age in state.rooms]
                for i, valve in valves:
                    new_rooms[i] = valve, 0
                rate = sum(graph[valve][0] for _, valve in valves)
                new_state = _State(
                    rooms=tuple(sorted(new_rooms)),
                    valves=state.valves - set(valve for _, valve in valves),
                    flow=state.flow + rate,
                    total=state.total + state.flow * (delta + 1),
                    time=state.time - delta - 1,
                )
                heapq.heappush(heap, (-estimate - rate * new_state.time, new_state))
    return max_seen

def part1(lines):
    return _solve(lines, num_agents=1, total_time=30)

def part2(lines):
   return _solve(lines, num_agents=2, total_time=26)

with open("Day16TestInput.txt") as file:
    lines = [line.rstrip() for line in file]
print(part1(lines),part2(lines))
