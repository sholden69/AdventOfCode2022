

with open("day1input.txt") as file:
    lines = [line.rstrip() for line in file]

elf=1  #keep track of elf number
max_cals=0
max_elf=-1
elf_cals=0
elf_dict = {}
for line in lines:
    if line=="":
       if (elf_cals>max_cals) :
            max_elf=elf
            max_cals=elf_cals
       elf_dict[elf] = elf_cals 
       elf+=1
       elf_cals=0
    else:
       elf_cals+=int(line)
print('elf',max_elf,'cals:',max_cals)

# part 2
sorted_elves = sorted(elf_dict.items(), key=lambda x:x[1],reverse=True)
#top 3 elves
total=0
for i in range(3):
    print(sorted_elves[i])
    total+=sorted_elves[i][1]
print ("top 3 elves carrying",total)