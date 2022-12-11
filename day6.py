srch_len=14

data = list(open("Day6Input.txt").read())
print(data)

comp=['@' for i in range(srch_len)] 
print(comp)

for i in range(0, len(data)):
    #print(data[i])
    comp=list(data[i])+comp[0:srch_len-1]
    if ((i>=srch_len) and (len(set(comp))==srch_len)):  #dont compare untl weve got to srch_len
        print("bingo",i+1,comp)
        break


