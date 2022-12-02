item_scores={"X":1, "Y":2, "Z":3}
pair_scores={"AX":3, #Rock/Rock
            "AY":6,  #Rock/Paper
            "AZ":0,  #Rock/Scissors
            "BX":0,  #Paper/Rock
            "BY":3,  #Paper/Paper
            "BZ":6,  #Paper/Scissors
            "CX":6, #Scissors/Rock
            "CY":0, #Scissors/Paper
            "CZ":3}   #Scisssor/Scissors

winners= {"A":"Y","B":"Z","C":"X"}
losers={"A":"Z","B":"X","C":"Y"}
draw={"A":"X","B":"Y","C":"Z"}

def select_move(elf_move,outcome):
    # elf_move will be A, B, C for rick, paper, scissors and paper
    # outcome will be X, Y, Z for lose, draw, win 
    if outcome=="Y":
        return draw[elf_move]
    elif outcome=="X":   #lose
        return losers[elf_move]
    else:  #win 
        return winners[elf_move]

with open("day2input.txt") as file:
    lines = [line.rstrip().split() for line in file]

n=1
score=0
for round in lines:
    elf,outcome=round
    me=select_move(elf,outcome)
    print("elf plays",elf,"outcome",outcome,"my move",me)
    round_score=pair_scores[elf+me]+item_scores[me]
    #print ("Round",n,":",me," ",elf," my score:", round_score)
    score+=round_score
    n+=1
print("final score:", score)


