

#build my list scoring elf_dict
scores=[i+1 for i in range(52)]
chars=[chr(c+ord('a')) for c in range(26)] + [chr(c+ord('A')) for c in range(26)]
scorer=dict(zip(chars, scores))


## PART 1
# read the file and split each line in half
total=0
with open("day3input.txt") as file:
     for line in file:
        part1, part2 = line[:len(line)//2], line[len(line)//2:]
        intsec = set(part1).intersection(part2)
        # traverse intesc and calc priorities
        this_score=sum(scorer[c] for c in intsec)
        total+=this_score
        #print(line, part1, part2, intsec, this_score)
print("Part 1 Total", total)

## PART2
total=0
with open("day3input.txt") as file:
    lines = [line.rstrip() for line in file]
for i in range(0,len(lines),3):
    intsec = set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2])
    total+=scorer[intsec.pop()]
print("Part 2 Total",total)








