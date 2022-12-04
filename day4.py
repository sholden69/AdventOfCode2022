
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

recs=[]
with open("day4input.txt") as file:
     for line in file:
        r1,r2=line.rstrip().split(",",1) 
        lo1,hi1=r1.split("-",1)
        lo2,hi2=r2.split("-",1)
        recs.append(srch_rec(lo1,hi1,lo2,hi2)) 

#tst=srch_rec(53,62,8,87)
#print(tst, tst.isContained())

cnt=0
for s in recs:
    if s.isContained():
        #print("Contained",s)
        cnt+=1
print("part 1 count",cnt)





