# Day 14
# https://adventofcode.com/2022/day/14


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
        self.grid[coord[1]-self.miny][coord[0]-self.minx]="o"

    def isAir(self,coord):
        if self.inRange(coord):
            yTest=coord[1]-self.miny
            xTest=coord[0]-self.minx
            el=self.grid[yTest][xTest]
            return (el==".")
        else:
            print("isRock passed out of range coord:",coord)
            return False

    def inRange(self,coord):
        x=coord[0]
        y=coord[1]
        return (  x>= self.minx and x<=self.maxx and y>=self.miny and y<=self.maxy)


    def dropSand(self,coord):
        #drops a unit of sand in at coord
        # returns false if it drops off the side 
        lastGoodSpot=nextSpot=coord
        inAbyss=False
        while True:
            success=False
            for chk in ['OneDown','DiagLeft','DiagRight']:
                match chk:
                    case 'OneDown':
                        nextSpot=(lastGoodSpot[0],lastGoodSpot[1]+1)
                    case 'DiagLeft':
                         nextSpot=(lastGoodSpot[0]-1,lastGoodSpot[1]+1)
                    case 'DiagRight':
                         nextSpot=(lastGoodSpot[0]+1,lastGoodSpot[1]+1)
                
                # if the next spot is sand then go round again
                if not self.inRange(nextSpot):
                    #we're in the abyss
                    inAbyss=True
                    break
                if self.isAir(nextSpot):
                    lastGoodSpot=nextSpot
                    bottomedOut=False
                    break  #want to break out of the for loop here.
                else:
                    #we've bottomed out
                    bottomedOut=True
            if  inAbyss or bottomedOut: #we've tried all three options from here without luck
                break
        # ive either come to rest or im in the abyss

        if inAbyss:
            return False

       # print("sand dropping at",lastGoodSpot)
        if self.inRange(lastGoodSpot):
            if self.isAir(lastGoodSpot):
                self.setSand(lastGoodSpot)
                return True
            else:
                return False
        else:
            return False

            
    def fillMe(self,startCoord):
    # keep dropping sand in until it flows into the abyss
        i=0
        while True:
            if not r.dropSand((500,0)):
                break
            else:
                i+=1
        return i

r=RockStructure("Day14Input.txt")
i=r.fillMe((500,0))
print(r,'\n',i,"sand units dropped")



