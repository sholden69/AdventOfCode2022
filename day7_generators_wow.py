def parse(path): return (
    x for x in [[y.strip() for y in x.split('\n') if y and '$' not in y]  
    for x in ''.join(
        cmd for cmd in open(path).readlines() if '..' not in cmd
).split('$ cd')] if x)

def build_tree(ops): return {
    y[1]: build_tree(ops) if y[0] == 'dir' else int(y[0]) 
    for y in [x.split() for x in next(ops)[1:]]
}

def solve(tree, part):
    flat = lambda k: (y for x in k for y in (flat(x) if type(x) is list else (x,)))
    size = lambda d: sum([v if type(v) is int else size(v) for v in d.values()])
    vals = lambda d: [size(d), [vals(x) for x in [x for x in d.values() if type(x) is dict]]]
    return part(list(flat(vals(tree))))

def part_one(sizes): 
    return sum(filter(lambda x: x < 100000, sizes))

def part_two(sizes): 
    return min(filter( lambda x: x > 30000000 - (70000000 - max(sizes)), sizes))

tree=build_tree(parse('Day7Input.txt'))

print('part 1:', solve(tree, part_one))
print('part 2:', solve(tree, part_two))