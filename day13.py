
import ast

def strToList(aStr):
    s1= ast.literal_eval(aStr)
    return s1


def lrComp(left,right):
    print("comp left",left,"right",right)

    #just left with two ints
    if type(left) is int and type(right) is int:
        return left<right

    #if ive got a list on the left and nothing on the right then im false
    if left and not right:
        return False
   
    if type(left) is int and type(right) is list:
        tstRes= lrComp(list(left),right) 
        return tstRes
    
    if type(right) is int and type(left) is list:
        return lrComp(left,list(right))

   #deal with lists of lists - caters for empty as well
    if type(left) is list and type(right) is list:
        ll=len(left)
        lr=len(right)
        if ll>0 and lr>0:
            tl=type(left[0])
            tr=type(right[0])
            if tr is list and tl is list: 
                return lrComp(left[0],right[0])
        


    
    i=0
    success=True
    while True:
        # base case of two integers
        # quit if we are at the end of either list
        if (i>=len(left)) or (i>=len(right)):
            if i<len(left):
                success=False
            break
        cmpL=left[i]
        cmpR=right[i]
        tL=type(cmpL)
        tR=type(cmpR)

        #compare left[i] vs right[i] if they are integers
        if tL is int and tR is int:
            if (cmpL>cmpR):
               success=False
               break
        elif tL is list and tR is int:
            success= lrComp(cmpL[0],cmpR)
        elif tL is int and tR is list:
            success= lrComp(cmpL,cmpR[0])
        else: #both lists
            success=lrComp(cmpL,cmpR)
        i+=1

    return success


with open("Day13TestInput.txt") as f:
    raw_pairs = f.read().split("\n\n")
pairs=[p.split("\n")for p in raw_pairs]

mySum=0
for idx,p in enumerate(pairs):
    p0=strToList(p[0])
    p1=strToList(p[1])
    if lrComp(p0,p1):
        mySum+=idx+1
        print("pair",idx+1,"matches. Score now",mySum)
print("matching score",mySum) 




