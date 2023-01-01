# Day   - part 2
# https://adventofcode.com/2022/day/14
# answer is 30214 


class RockStructure:

    def __init__(self,filename):
        # parse the file 
        myCoords={}
        self.minx=self.maxx=500
        self.miny=self.maxy=0
        with open(filename) as file:
            for idx,line in enumerate(file):
                coords=line.rstrip().split("->")
                thisLine=[]
                for coord in coords:
                    x,y=coord.split(',')
                    x=int(x)
                    y=int(y)
                    thisLine.append((x,y))
                    if x<self.minx:
                        self.minx=x
                    if y<self.miny:
                        self.miny=y
                    if x>self.maxx:
                        self.maxx=x
                    if y>self.maxy:
                        self.maxy=y
                myCoords[idx]=thisLine

        # add a floor for part 2
        self.minx-=10
        self.maxx+=1000
        self.maxy+=2
        myCoords[idx+1]=[(self.minx,self.maxy),(self.maxx,self.maxy)]

        # build the rocks structure using the dictionary
        self.grid=[ ['.']*(self.maxx-self.minx+1) for n in range(0,self.maxy-self.miny+1)]
        for key in myCoords.keys():
            c1=myCoords[key][0]
            i=1
            while i<len(myCoords[key]):
                c2=myCoords[key][i]
                self.setRock(c1,c2)
                c1=c2
                i+=1
        
    def __repr__(self):
        myStr='Minx, MaxX, MinY, MaxY - '+ \
            str(self.minx)+","+str(self.maxx)+","+str(self.miny)+","+str(self.maxy)+"\n"
        for i in range(self.miny,self.maxy+1):
            myStr+=''.join(str(e) for e in self.grid[i-self.miny]) +'\n'
        return myStr

    def setRock( self, coord1,coord2):
        # sets the rock between coord1 and coord2
        #print("setRock",coord1,coord2)
        x1,y1=coord1
        x2,y2=coord2
        if x1==x2 :
            #vertical
            x=x1-self.minx
            step=-1 if y1>y2 else 1
            for i in range(y1,y2+step,step):
                y=i-self.miny
                self.grid[y][x]="#"
        else :
            #horizontal
            y=y1-self.miny
            step=-1 if x1>x2 else 1
            for i in range(x1,x2+step,step):
                x=i-self.minx
                self.grid[y][x]="#"
    
    def setSand(self,coord):
        y=coord[1]-self.miny
        x=coord[0]-self.minx
        self.grid[y][x]="o"

    def isAir(self,coord):
        y=coord[1]-self.miny
        x=coord[0]-self.minx
        return (self.grid[y][x]==".")

    def inRange(self,coord):
        x=coord[0]
        y=coord[1]
        return (x>= self.minx and x<=self.maxx and y>=self.miny and y<=self.maxy)


    def fillMe2(self) -> int : 
        #version of fillMe for part 2 takes advantage of knowing the floor
        sandCount=0
        while True:
            thisX=500
            thisY=0
            while True:
                if self.isAir((thisX,thisY+1)): 
                    thisY+=1
                elif self.isAir((thisX-1,thisY+1)): 
                    thisY+=1
                    thisX-=1
                elif self.isAir((thisX+1,thisY+1)): 
                    thisY+=1
                    thisX+=1
                else:
                    if self.isAir((thisX,thisY)):
                        self.setSand((thisX,thisY))
                        sandCount+=1
                    break
            if thisX==500 and thisY==0:
                break
        return sandCount

r=RockStructure("Day14Input.txt")
i=r.fillMe2()
print(r,'\n',i,"sand units dropped")



