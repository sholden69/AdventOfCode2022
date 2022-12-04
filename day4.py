
class srch_rec:

    def __init__(self, lo1, hi1, lo2,hi2):
        self.lo1 = int(lo1)
        self.hi1 = int(hi1)
        self.lo2 = int(lo2)
        self.hi2 = int(hi2 )
   
    def __repr__(self):
        return "srch_rec:"+str(self.lo1)+"-"+str(self.hi1)+" "+str(self.lo2)+"-"+str(self.hi2)

    def equals(self):
        return( (self.lo1==self.lo2) and (self.hi1==self.hi2) )

    def isContained(self):
        #print("testing",self)
        return ((self.lo2>=self.lo1) and (self.hi2<=self.hi1)) or \
              ((self.lo1>=self.lo2) and (self.hi1<=self.hi2))  

    def overlaps(self):
        # turn lo1..hi1 and lo2..hi2 into a set and look for intersection
        set1=set(range(self.lo1, self.hi1+1))
        set2=set(range(self.lo2, self.hi2+1))
       # print ("**overlap:",self,set1, set2)
        return( len(set1.intersection(set2))>0 )

recs=[]
with open("day4input.txt") as file:
     for line in file:
        r1,r2=line.rstrip().split(",",1) 
        lo1,hi1=r1.split("-",1)
        lo2,hi2=r2.split("-",1)
        recs.append(srch_rec(lo1,hi1,lo2,hi2)) 

#part1 - count the number of contained items (equal=contained)
print ("part 1: list comp:",len([1 for s in recs if s.isContained() ]))
#part2 - just count the intersections 
print ("part 2: list comp:",len([1 for s in recs if s.overlaps() ]))

# older long-winded code
# part 1 
cnt=0
for s in recs:
    if s.isContained():
        #print("Contained",s)
        cnt+=1
print("part 1 count - containments",cnt)

cnt=0
print("#pairs",len(recs))
for s in recs:
    if s.overlaps():
        cnt+=1
print("part 2 count - intersections",cnt)





