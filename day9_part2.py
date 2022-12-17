class Knot:
    def __init__(self):
        self.myx=self.myy=0

    def getX(self):
        return self.myx

    def getY(self):
        return self.myy

    def pullMe(self,kx,ky):
        #given coords of rhe next knot up, (kx,ky), change my posn
        if (abs(ky-self.myy)==2 or abs(kx-self.myx)==2) and (self.myx!=kx) and (self.myy!=ky): 
            #print("diagonal")
            if self.myx>kx and self.myy>ky: #top is top right of heead
                self.myx+=-1
                self.myy+=-1
            elif self.myx>kx and self.myy<ky: #tail is bottom right of head
                self.myx+=-1
                self.myy+=1
            elif self.myx<kx and self.myy<ky: #tail is bottom left of head
                self.myx+=1
                self.myy+=1
            else: #tail is top left of head
                self.myx+=1
                self.myy+=-1

        # Check if more than one space apart on same row or column and move closer
        if (abs(kx-self.myx)>1):
            self.myx+=(kx-self.myx)//2   
        if (abs(ky-self.myy)>1):
            self.myy+=(ky-self.myy)//2
        return None


class Rope2:
    def __init__(self,tailLength:int):
        self.myLength=tailLength
        self.tail=[Knot() for i in range(tailLength) ]
        # coords of head
        self.hx=self.hy=0  # head coords
        self.minx=self.maxx=self.miny=self.maxy=0  #grid bounds
        self.tailVisits=set()
        self.moves=[]
        self.logMove()

    def logMove(self):
        # record the position of the last knot
        tx=self.tail[self.myLength-1].getX()
        ty=self.tail[self.myLength-1].getY()
        self.tailVisits.add(str(tx)+":"+str(ty))
        
        #update the min/max vars for the gridPlot based on the head 
        if self.hx<self.minx:
            self.minx=self.hx
        if self.hx>self.maxx:
            self.maxx=self.hx
        if self.hy<self.miny:
            self.miny=self.hy
        if self.hy>self.maxy:
            self.maxy=self.hy

    def moveMe(self,dir):
    # move hd one space in dir and pull tail
        match dir :
            case "U" : self.hy+=1
            case "D" : self.hy-=1
            case "L" : self.hx-=1
            case "R" : self.hx+=1
        cx=self.hx
        cy=self.hy
        for i in range(self.myLength):
            self.tail[i].pullMe(cx,cy)
            cx=self.tail[i].getX()
            cy=self.tail[i].getY() 
        self.logMove()
        return None

    def tailCount(self) -> int : 
        return len(self.tailVisits)

    def runMoves(self,filename):
        #load up the moves list from given file
        with open(filename) as file:
            for line in file:
                dir,cnt=line.rstrip().split() 
                for i in range(int(cnt)):
                    self.moveMe(dir)
                    #rp.gridPrint()

def part2():
    rp=Rope2(9)
    rp.runMoves("Day9Input.txt")
    print("tail visited",rp.tailCount(),"unique locations")

part2()








