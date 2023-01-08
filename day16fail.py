# Advent Of Code 2022 Day 16:  https://adventofcode.com/2022/day/16

# file: Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

# Valves (flow,[valves])

# This is a graph traversal problem with a twist.
# as traverse the paths the cumulative impact of each subsequent node in the remaining time is less

# use what we learned in day12

import re
from heapq import heappush, heappop


def getNeighbours(vlist,valve):
    return vlist[valve][1]
  

def findBestRoute(vlist,valve,time)-> int:
    # try each path from here
    if time>30:
        return 0
    print("starting at",valve,"time",time)
    nbors=getNeighbours(vlist,valve)
    res=[]
    for nbor in nbors:
        # move without opening the valve
        res.append(findBestRoute(vlist,nbor,time+1))
        #open the valve if its closed
        if not vlist[nbor][2]:
            flow=vlist[nbor][0]
            tunnels=vlist[nbor][1]
            vlist[nbor]=(flow,tunnels,True)
            res.append(findBestRoute(vlist,nbor,time+2))
    if len(res)==0 :
        return 0
    else:       
        res.sort(reverse=True)
        return res[0]


def readinput(filename):
    #Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    valves={}
    with open(filename) as f:
            for line in f.readlines():
                v=line[6:8]
                vflow=int(re.findall(r"=(-?\d+)", line)[0]) 
                if len(line)<=52: 
                    tunnels=[line[-3:].strip()]
                else:
                    tunnels=line[line.find("valves")+7:].strip().split(", ")
                valves[v]=(vflow,tunnels,False)
    return valves


vList=readinput('Day16TestInput.txt')
print(vList)
print(findBestRoute(vList,"AA",0))


