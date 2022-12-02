item_scores={"Rock":1, "Paper":2, "Scissors":3}
# elf / me  1 =win, -1 = defeat 
item_rank={"Rock/Scissors":-1, "Rock/Paper":1, "Rock/Rock":0,
           "Paper/Rock":-1, "Paper/Scissors":1, "Paper/Paper":0,
           "Scissors/Rock":1, "Scissors/Paper":-1, "Scissors/Scissors":0}
elf_map={"A":"Rock","B":"Paper","C":"Scissors"}

losers=dict([key.split('/') for key in item_rank if item_rank[key]==-1])
winners=dict([key.split('/') for key in item_rank if item_rank[key]==1])
draws=dict([key.split('/') for key in item_rank if item_rank[key]==0])

#could go a bit further and make a named tuple with a record like:
# item_type: item_score, elf_map, beats, loses
#   Rock:     1, A, Scissors, Paper  
#   Paper:    2, B, Rock, Scissors
#   Scissors: 3, C, Paper, Rock
# All of the above data structures could then be auto-generated from there 


def select_move(elf_move,outcome):
    # elf_move will be Rock, Paper, Scissors 
    # outcome will be X, Y, Z for lose, draw, win 
    if outcome=="Y":
        return draws[elf_move]
    elif outcome=="X":   #lose: find the -1 key that matches elf_move
        return losers[elf_move]
    else:  #win: find the 1 key that matches elf_move
        return winners[elf_move]

with open("day2input.txt") as file:
    lines = [line.rstrip().split() for line in file]

n=1
score=0
for round in lines:
    elf,outcome=round
    elf_move=elf_map[elf]
    me=select_move(elf_move,outcome)
    round_score=3*item_rank[elf_move+"/"+me]+3+item_scores[me]
    #print("elf plays",elf_map[elf],"outcome",outcome,"my move",me,"score",round_score)
    score+=round_score
    n+=1
print("final score:", score, "after round",n-1)
#15457
