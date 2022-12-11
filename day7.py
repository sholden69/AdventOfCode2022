# build a nested set of dictionaries to represent the file strucure and then /
# trverse recusrively accumulating the directory size at each level from sum of files + sum of sub_dirs

from collections import defaultdict


def change_directory(s: str, cd: list[str]) -> None:
# maintains list of paths as we travers
    match s:
        case '/':
            cd = ['root']
        case '..':
            cd.pop()
        case _:
            cd.append(s)

    return cd


def get_dict_path(d: dict, path: list) -> dict:
# returns the correct key to append the size info to
    if len(path) == 1:
        return d[path[0]]
    else:
        return get_dict_path(d[path[0]], path[1:])


def directory_size(d: dict) -> int:
# recursive function to return size of a directory via files in its directory and sub_dirs
    return sum(directory_size(v) if isinstance(v, dict) else v for v in d.values())


def traverse_dict(d: dict, res=None) -> None:
# Builds a list of the directory sizes under the directories in this dict structure
# eg for the test input:
# {'root': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514,
#  'c.dat': 8504156, 'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}

    if not res:  #make sure we dont have an empty list
        res = []

    for k, v in d.items():
        if not isinstance(v, dict):  #skip over individual files
            continue
        #print("traversing",k,v)
        res.append(directory_size(v))  #add the size of sub_dirs to list 
        traverse_dict(v, res)
    
    return res

def pretty_print(d: dict, dir: str) -> None: 
    for k, v in d.items():
        if not isinstance(v, dict):
           continue
        else:
            print(k,directory_size(v))
            pretty_print(v,dir+"/"+k)


def p1(instructions: list[str]) -> None:
# builds a nested dictionary structure "files" of the file system containing file sizes.
# eg for the test input:
# {'root': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514,
#  'c.dat': 8504156, 'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}

    files = {'root': {}}
    cd = ['root']
    
    for line in instructions:
        if '$ cd' in line:
            cd = change_directory(line.split()[-1], cd=cd)
        elif '$ ls' in line:
            continue
        else:  #file or dir here
            marker, name = line.split()
            if marker.isnumeric():  #got a file so store the size 
                get_dict_path(files, cd)[name] = int(marker)
            else: #got a dictionary so create a new dict on the path key for this directory
                get_dict_path(files, cd)[name] = {}
   
    print(sum(n for n in traverse_dict(files) if n <= 100_000))
    return files

def p2(files: dict) -> None:
    directory_sizes = traverse_dict(files)
    
    used = max(directory_sizes)
    total_size = 70000000
    need_at_least = 30000000
    unused = total_size - used
    target = need_at_least - unused

    return min(n for n in directory_sizes if n >= target)

#need to be able to sum up total number of files at every level of the directory structures
with open("Day7Input.txt") as file:
    lines = [line.rstrip() for line in file]
file_parse=p1(lines)
#pretty_print(file_parse,"/")
p2ans=p2(file_parse)
print("p2", p2ans)