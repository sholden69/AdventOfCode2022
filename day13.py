
import ast

def strToList(aStr):
    s1= ast.literal_eval(aStr)
    return s1

def flatten(aList):
    #takes nested list and flattens it out
    if not aList:
        return None
    i=0
    ret=[]
    while i<len(aList):
        if type(aList[i]) is int:
            ret.append(aList[i])
        else:
            for el in flatten(aList[i]):
                ret.append(el)
        i+=1
    return ret





def lrComp(left,right):
    print("comp left",left,"right",right)

    #just left with two ints
    if type(left) is int and type(right) is int:
        return left<right

    #if ive got a list on the left and nothing on the right then im false
    if left and not right:
        return False
   
    if type(left) is int and type(right) is list:
        return lrComp(list(left),right) 
    
    if type(right) is int and type(left) is list:
        return lrComp(left,list(right))

   #deal with empty lists
    if type(left) is list and type(right) is list: #both lists
        if len(right)==1 and len(left)==1:
            return lrComp(left[0],right[0])
        elif len(left)==1:
            return True
        elif len(right)==1:
            return False
    
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
        i+=1

    return success

def lrComp2(left,right):
    print("lrComp2",left,right)
    i=0
    success=True
    while True:
        if i>=len(left) and i>=len(right):
            break
        if i>=len(left):
            break
        if i>=len(right):
            success=False
            break
        if left[i]<=right[i]:
            i+=1
        else:
            return False
    return success


with open("Day13TestInput.txt") as f:
    raw_pairs = f.read().split("\n\n")
pairs=[p.split("\n")for p in raw_pairs]

mySum=0
for idx,p in enumerate(pairs):
    p0=flatten(strToList(p[0]))
    p1=flatten(strToList(p[1]))
    if lrComp2(p0,p1):
        mySum+=idx+1
        print("pair",idx+1,"matches. Score now",mySum)
print("matching score",mySum) 




