class Rope:
    def __init__(self):
        self.hx=0
        self.hy=0
        self.tx=0
        self.ty=0
        self.minx=0
        self.miny=0
        self.maxx=0
        self.maxy=0
        self.tailVisits=set()
        self.logMove()
        
    def logMove(self):
        self.tailVisits.add(str(self.tx)+":"+str(self.ty))

    def adjustTail(self):
        if (abs(self.hx-self.tx)>1)  or (abs(self.hy-self.ty)>1):
            #need to move the tail
            if self.tx==self.hx:
                #in same row hy-ty will be +/-2 
                self.ty+=(self.hy-self.ty)//2
            elif self.ty==self.hy:
                #in same column hx-tx will be +/- 2
                self.tx+=(self.hx-self.tx)//2
            else:
                #diagonal move
                #print("diagonal")
                if abs(self.hy-self.ty)==2:
                    if self.tx<self.hx:
                        self.tx+=1
                        self.ty+=1
                    else:
                        self.tx-=1
                        self.ty-=1
                elif abs(self.hx-self.tx)==2:
                    if self.hx<self.tx:
                        self.tx-=1
                        self.ty+=1
                    else:
                        self.tx+=1
                        self.ty-=1
        return None

    def moveMe(self,dir):
    # meat will go here...
        match dir :
            case "U" : self.hy+=1
            case "D" : self.hy-=1
            case "L" : self.hx-=1
            case "R" : self.hx+=1
        self.adjustTail()
        self.logMove()
        #print("head is at",self.hx,self.hy," tail is at",self.tx,self.ty)
        if self.hx<self.minx:
            self.minx=self.hx
        if self.hx>self.maxx:
            self.maxx=self.hx
        if self.hy<self.miny:
            self.miny=self.hy
        if self.hy>self.maxy:
            self.maxy=self.hy
        return None

    def moveCount(self) -> int:
        return len(self.tailVisits)

    def gridPrint(self):
        for y in range(self.maxy,self.miny-1,-1):
            outStr=''
            for x in range(self.minx, self.maxx+1,1):
                if x==self.hx and y==self.hy:
                    outStr+='H'
                elif x==self.tx and y==self.ty:
                    outStr+="T"
                else:
                    outStr+="."
            print(outStr)
        print("\n")

    def showVists(self) :
        print(self.tailVisits)


def part1():
    rp=Rope()
    with open("Day9TestInput.txt") as file:
        for line in file:
            dir,cnt=line.rstrip().split() 
            for i in range(int(cnt)):
                rp.moveMe(dir)
                rp.gridPrint()
    print("tail visited",rp.moveCount()," unique locations")
   # rp.showVists()


part1()




