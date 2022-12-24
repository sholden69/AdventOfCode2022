from heapq import heappush, heappop

# uses dijkstra's algorithm to find short path between two nodes on a graph
# implemented on top of a priority queue
# see https://realpython.com/python-heapq-module/


with open("Day12TestInput.txt") as f:
    grid = [list(row.strip()) for row in f.readlines()]


def get_neightbors(r, c):
    # get the legitimate neighbours
    h = get_height(r, c)
    neighbors = []
    for dis_r, dis_c in ([-1, 0], [1, 0], [0, -1], [0, 1]):
        r1, c1 = r + dis_r, c + dis_c
        if r1 >= 0 and r1 < len(grid) and c1 >= 0 and c1 < len(grid[0]):
            if get_height(r1, c1) <= h + 1:
                neighbors.append((r1, c1))
    return neighbors


def get_height(r, c):
    # convert the char into a height
    s = grid[r][c]
    if s == "S":
        return 0
    if s == "E":
        return 25
    return ord(s) - 97


def get_steps(start, end):
    # Dijkstra for shortest path finding
    visited = set()
    prio_queue = []
    heappush(prio_queue, (0, start))

    while True:
        if not prio_queue: # no more neighbours to check out so bail
            break

        #get the next node and the step count  to here tuple off the heap
        # heap will return the item with the highest number of steps first
        steps, node = heappop(prio_queue)
        #print("processing",node,"count=",steps)
        if node not in visited:  #if this is a new node
            visited.add(node)
            if node == end:  #we've reached the end
                return steps
            # find all the legitimate neighbours of this node and push to heap with count incremented
            for rnew, cnew in get_neightbors(node[0], node[1]):
                heappush(prio_queue, (steps+1, (rnew, cnew)))


# get start(s) + end
starts = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            start_fix = (r, c)
            starts.append((r, c))
        if grid[r][c] == "E":
            end = (r, c)
        if grid[r][c] == "a":
            starts.append((r, c))


# task 1
print(get_steps(start_fix, end))

# task 2 # try every square that starts wwith a
steps_all = []
for start in starts:
    steps = get_steps(start, end)
    if steps is not None:
        steps_all.append(steps)

print(min(steps_all))