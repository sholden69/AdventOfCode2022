# advent of code 2022. Day 1
# https://adventofcode.com/2022/day/1

with open("day1input.txt") as file:
    lines = [line.rstrip() for line in file]

elf=1  #keep track of elf number
max_cals=0
max_elf=-1
elf_cals=0
elf_dict = {}
for line in lines:
    if line=="": #onto a new elf so check totals
       if (elf_cals>max_cals) :
            max_elf=elf
            max_cals=elf_cals
       elf_dict[elf] = elf_cals #record the calories for each elf
       elf+=1
       elf_cals=0
    else:
       elf_cals+=int(line)
print('elf',max_elf,'cals:',max_cals)

# part 2
# sort the dict on the second element, slice to top 3 and then use sum
total=sum(x[1] for x in sorted(elf_dict.items(), key=lambda x:x[1],reverse=True)[:3]) 
print ("top 3 elves carrying",total)