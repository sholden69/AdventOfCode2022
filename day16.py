# Advent Of Code 2022 Day 16:  https://adventofcode.com/2022/day/16

# file: Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

# Valves (flow,[valves])

# This is a graph traversal problem with a twist.
# as traverse the paths the cumulative impact of each subsequent node in the remaining time is less

# use what we learned in day12

import re
from heapq import heappush, heappop




def getNeighbours(valve, vlist):
    return vlist[valve][1]
  


def getPressure(start,vList):
    # Dijkstra for shortest path finding
    # Our tuple will be totalpressure,time,node
    visited = set()
    prio_queue = []
    heappush(prio_queue, (0, 0, start))

    while True:
        if not prio_queue: # no more neighbours to check out so bail
            break

        #get the next node and the step count  to here tuple off the heap
        # heap will return the item with the highest number of steps first
        pressure, time, node = heappop(prio_queue)
        print("processing",node,"pressure=",pressure,"time=",time)
        if node not in visited:  #if this is a new node
            visited.add(node)
            if time==30:  #we've reached the end
                return pressure
            # find all the legitimate neighbours of this node and push to heap with count incremented
            time+=2
            for aNode in getNeighbours(node,vList):
                myPressure=pressure+vList[aNode][0]
                heappush(prio_queue, (myPressure, time,aNode))


def readinput(filename):
    #Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    valves={}
    with open(filename) as f:
            for line in f.readlines():
                v=line[6:8]
                vflow=int(re.findall(r"=(-?\d+)", line)[0])*-1
                if len(line)<=52: 
                    tunnels=[line[-3:].strip()]
                else:
                    tunnels=line[line.find("valves")+7:].strip().split(", ")
                valves[v]=(vflow,tunnels)
    return valves


vList=readinput('Day16TestInput.txt')
print(vList)
print(getPressure("AA",vList))


