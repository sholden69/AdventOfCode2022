from collections import namedtuple
from itertools import islice
import time

class Monkey:
    def __init__(self):
        self.items=[]
        self.divisor=0
        self.worry_rule=None
        self.throw_rule=None
        self.true_monkey=-1
        self.false_monkey=-1
        self.inspections=0
        return None
    
    def addItems(self,items):
        self.items=[int(i) for i in items]

    def addBoolMonkeys(self,trueMky, falseMky):
        self.true_monkey=trueMky
        self.false_monkey=falseMky

    def addOperation(self, opStr):
        self.worry_rule=opStr.rstrip()
        return None

    def addDivisor(self, dvsor):
        self.divisor=dvsor
    
    def popItem(self):
        if len(self.items)>0:
            self.inspections+=1
            return(self.items.pop(0))
        else:
            return None

    def getItems(self):
        return self.items

    def getInspections(self):
        return self.inspections

    def pushItem(self,itm):
        self.items.append(itm)

    def applyWorryRule(self,itm):
        #parse the worry rule and apply 
        #old/value  operator    value
        opd1,opr,opd2=self.worry_rule.split(' ')
        if opd1=="old":
            v1=itm
        else:
            v1=int(opd1)
        if opd2=="old":
            v2=itm
        else:
            v2=int(opd2)
        match opr:
            case "+" : return v1+v2
            case "*" : return v1*v2
            case "-" : return v1-v2
            case "/" : return v1/v2


    def applyThrowRule(self,itm):
        #returns the number of the monkey to throw to 
        if itm % self.divisor == 0:
            return self.true_monkey
        else:
            return self.false_monkey

    def applyThrowRule2(self,itm):
        #returns the number of the monkey to throw to 
        rem= itm % self.divisor 
        if rem== 0:
            return [self.true_monkey,0]
        else:
            return [self.false_monkey,rem]

    def __repr__(self):
        outstr='Starting items:'
        for i in self.items:
            outstr+=str(i)+' '
        outstr+='\n Worry Rule:'+self.worry_rule
        outstr+='\n Divisor:'+str(self.divisor)
        outstr+='\n True\False:'+str(self.true_monkey)+' '+str(self.false_monkey)
        return(outstr)
        
def buildMonkeyList(filename)-> list:
    mkList=[]
    with open(filename) as f:
        thisMky=0
        while True:
            mkyBlock = list(islice(f, 7))
            if not mkyBlock:
                break
            mk=Monkey()
            # line 0: is Monkey #
            #line 1: is the starting items
            mk.addItems(mkyBlock[1][18:].rstrip().split(','))
            
            #line 2: is the operation
            mk.addOperation(mkyBlock[2][19:])
        
            # line 3: is the divisor
            mk.addDivisor(int(mkyBlock[3][21:].rstrip()))
            
            # line 4 is true mky, 5 is fasl e
            tm=int(mkyBlock[4][29:].rstrip())
            fm=int(mkyBlock[5][30:].rstrip())
            mk.addBoolMonkeys(tm,fm)     

            mkList.append(mk)
            thisMky+=1
    return mkList


def part1Run(mklist, rounds): 
    t1=time.perf_counter()
    print('*** Lets Start')
    for round in range(1,rounds+1):
        if round % 100 ==0:
            t2=time.perf_counter()
            print('round',round,'in',t2-t1,'seconds')
            t1=t2
        for mky in mylist:
            while True:
                itm=mky.popItem()
                if itm is None:
                    break
                itm=mky.applyWorryRule(itm) // 3
            
                # find out which monkey to throw to             
                mylist[mky.applyThrowRule(itm) ].pushItem(itm) 

    # list out the inspection count
    for mky in mylist:
        print(mky.getInspections())
            
    top2=sorted([mky.getInspections() for mky in mylist],reverse=True)[0:2]
    print("Monkey Busines",top2[0]*top2[1])



mylist=buildMonkeyList('Day11Input.txt')    
#part1Run(mylist,20)

itemPaths={}
for idx,mky in enumerate(mylist):
    for itm in mky.getItems():
        # first mky, remainder
        thisValue=itm
        nextVal=mky.applyWorryRule(itm) 
        nextMky,firstRem=mky.applyThrowRule2(itm)
        itemPaths[thisValue]=[[idx,firstRem]] # initialise a blank list
        while True:
            # follow each monkey pass until you are back at first monkey with same output
            thisMky=nextMky
            thisVal=nextVal
            nextVal=mylist[thisMky].applyWorryRule(thisVal) 
            nextMky,thisRem=mylist[thisMky].applyThrowRule2(itm)
            # need to scan through to see whther we have thisMyy, thisRem
            breakOut=False
            for items in itemPaths[thisValue]:
                if items[0]==thisMky and items[1]==thisRem:
                    breakOut=True
                    break
            itemPaths[thisValue].append([thisMky,thisRem])
            print("start item",thisValue,"monkey",thisMky,"Remainder",thisRem)
            if breakOut:
                break
for items in itemPaths:
    print(items)



