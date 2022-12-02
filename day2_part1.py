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


with open("day2input.txt") as file:
    lines = [line.rstrip().split() for line in file]

n=1
score=0
for round in lines:
    elf,me=round
    round_score=pair_scores[elf+me]+item_scores[me]
    #print ("Round",n,":",me," ",elf," my score:", round_score)
    score+=round_score
    n+=1
print("final score:", score, "after round",n-1)


