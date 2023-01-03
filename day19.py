#Advent of Code 2022 Day 19
# https://pastebin.com/KDTmtHCk
import re

TEST_DATA = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""
 
input_pattern = re.compile('^Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.')

def get_daily_input():
    bps=[]
    with open("Day19TestInput.txt") as file:
        for line in file:
            m = input_pattern.match(line.strip())
            costs = {}
            costs = {"ore": {}, "clay": {}, "obsidian": {}, "geode": {}}
            costs["ore"]["ore"] = int(m.group(2))
            costs["clay"]["ore"] = int(m.group(3))
            costs["obsidian"]["ore"] = int(m.group(4))
            costs["obsidian"]["clay"] = int(m.group(5))
            costs["geode"]["ore"] = int(m.group(6))
            costs["geode"]["obsidian"] = int(m.group(7))
            bps.append(costs)
    return []

class Blueprint:
    __slots__ = ("id", "cost", "useful")
 
    def __init__(self, input_string: str) -> None:
        vals = [int(i) for i in re.findall(r"\d+", input_string)]
        self.id = vals[0]
        self.cost = {
            "ore": {"ore": vals[1]},
            "clay": {"ore": vals[2]},
            "obsidian": {"ore": vals[3], "clay": vals[4]},
            "geode": {"ore": vals[5], "obsidian": vals[6]}
        }
        self.useful = {
            "ore": max(self.cost["clay"]["ore"],
                       self.cost["obsidian"]["ore"],
                       self.cost["geode"]["ore"]),
            "clay": self.cost["obsidian"]["clay"],
            "obsidian": self.cost["geode"]["obsidian"],
            "geode": float("inf")
        }
 
 
class State:
    __slots__ = ("robots", "resources", "ignored")
 
    def __init__(self, robots: dict = None, resources: dict = None,
                 ignored: list = None):
        self.robots = robots.copy() if robots else {
            "ore": 1, "clay": 0, "obsidian": 0, "geode": 0
        }
        self.resources = resources.copy() if resources else {
            "ore": 0, "clay": 0, "obsidian": 0, "geode": 0
        }
        self.ignored = ignored.copy() if ignored else []
 
    def copy(self) -> "State":
        return State(self.robots, self.resources, self.ignored)
 
    def __gt__(self, other):
        return self.resources["geode"] > other.resources["geode"]
 
    def __repr__(self):
        return f"{{robots: {self.robots}, resources: {self.resources}}}"
 
 
def evaluate_options(
        blueprint: Blueprint,
        prior_states: list[State],
        timelimit: int = 26
) -> [tuple[int, list]]:
    time_remaining = timelimit - len(prior_states)
    curr_state = prior_states[-1]
 
    # determine options for what to build in the next state
    options: list[str] = []
    if time_remaining >= 0:
        # look for something affordable and useful and not ignored last time
        for robot, cost in blueprint.cost.items():
            if (curr_state.robots[robot] < blueprint.useful[robot]
                    and all(curr_state.resources[k] >= v for k, v in cost.items())
                    and robot not in curr_state.ignored):
                options.append(robot)
 
        # geodes before anything else, don't bother with other types at the end
        if "geode" in options:
            options = ["geode"]
        elif time_remaining < 1:
            options = []
        else:
            # cutting off plans that build resources more than 2 phases back
            if ((curr_state.robots["clay"] > 3 or curr_state.robots["obsidian"]
                 or "obsidian" in options) and "ore" in options):
                options.remove("ore")
            if ((curr_state.robots["obsidian"] > 3 or curr_state.robots["geode"]
                 or "geode" in options) and "clay" in options):
                options.remove("clay")
 
        # add new resources
        next_state = curr_state.copy()
        for r, n in next_state.robots.items():
            next_state.resources[r] += n
 
        # the 'do nothing' option
        next_state.ignored += options
        results = [evaluate_options(blueprint, prior_states + [next_state], timelimit)]
 
        # the rest of the options
        for opt in options:
            next_state_opt = next_state.copy()
            next_state_opt.ignored = []
            next_state_opt.robots[opt] += 1
            for r, n in blueprint.cost[opt].items():
                next_state_opt.resources[r] -= n
            results.append(
                evaluate_options(blueprint, prior_states + [next_state_opt], timelimit)
            )
 
        return max(results)
 
    return prior_states[-1].resources["geode"], prior_states
 
 
def part_1() -> int:
    blueprints = [Blueprint(bp) for bp in get_daily_input()]
    result = 0
    for bp in blueprints:
        r = evaluate_options(bp, [State()], 24)
        result += r[0] * bp.id
    return result
 
 
def part_2() -> int:
    blueprints = [Blueprint(bp) for bp in get_daily_input()]
    if len(blueprints) > 3:
        blueprints = blueprints[:3]
    result = 1
    for bp in blueprints:
        r = evaluate_options(bp, [State()], 32)
        result *= r[0]
    return result
 
 
def main():
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
 
 
if __name__ == "__main__":
    main()