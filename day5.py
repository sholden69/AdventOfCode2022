#day5


#read the input file and split it into 2 arrays of lines around the blank lines

with open("Day5Input.txt") as file:
    lines = [line.rstrip() for line in file]

#find the index of the blank line 
split=lines.index('')
stack_data=lines[:split]
moves_data=lines[split+1:]

print("Stack Data",stack_data)
nstacks=int(stack_data.pop().split('  ').pop())
print("#Stacks",nstacks)

# use a list of lists for our stacks and populate from bottom up
# append adds, and pop removes
#print(stack_data)
print("Initialising Stacks...")
stacks=[[] for i in range(nstacks)]
print("Stacks",len(stack_data),stack_data)
for n in range(len(stack_data),0,-1):
    #grab 4 chars at a time per stack
    #print("line",n)
    crates=[stack_data[n-1][i:i+4].rstrip() for i in range(0, len(stack_data[n-1]), 4)]
    res=[stacks[i].append(j) for i, j in enumerate(crates) if j!= '']
print(stacks)
        
def part1_mover():
# Part 1 mover - simply pop and push
    print('moving....')
    for move in moves_data:
        instr=move.split()
        cnt=int(instr[1])  # how many
        src=int(instr[3])  # from 
        dst=int(instr[5])
        for i in range(cnt):
            itm=stacks[src-1].pop()
            stacks[dst-1].append(itm)
            print ("moved",itm,"from",src,"to",dst)

def part2_mover():
    # this time need to preserve order so its a slice and append
    print('moving....')
    for move in moves_data:
        instr=move.split()
        cnt=int(instr[1])  # how many
        src=int(instr[3])  # from 
        dst=int(instr[5])
        #take the last cnt items from src and append to dst
        slc=stacks[src-1][-cnt:]
        for item in slc:
            stacks[dst-1].append(item)
        #now drop what we moved
        cutoff=len(stacks[src-1])-cnt
        stacks[src-1]=stacks[src-1][0:cutoff]
            

part2_mover()
print("Final Stacks",stacks)
res=''
for s in stacks:
    res+=s.pop()[1]
print(res)



