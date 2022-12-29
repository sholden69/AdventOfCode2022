# Day 14
# https://adventofcode.com/2022/day/14


class RockStructure:

    def __init__(self,filename):
        # parse the file 
        myCoords={}
        self.minx=self.miny=self.maxx=self.maxy=-1
        with open(filename) as file:
            for idx,line in enumerate(file):
                coords=line.rstrip().split("->")
                thisLine=[]
                for coord in coords:
                    x,y=coord.split(',')
                    x=int(x)
                    y=int(y)
                    thisLine.append((x,y))
                    if self.minx==-1 or x<self.minx:
                        self.minx=x
                    if self.miny==-1 or y<self.miny:
                        self.miny=y
                    if self.maxx==-1 or x>self.maxx:
                        self.maxx=x
                    if self.maxy==-1 or y>self.maxy:
                        self.maxy=y
                myCoords[idx]=thisLine

        # build the rocks structure using the dictionary
        self.grid=[ ['.']*n for n in range(0,self.maxx-self.minx+1)]
        for key in myCoords.keys():
            c1=myCoords[key][0]
            i=1
            while i<len(myCoords[key]):
                c2=myCoords[key][i]
                #self.setRock(c1,c2)
                c2=c1
                i+=1

    def __repr__(self):
        myStr=''
        for i in range(self.miny,self.maxy):
            myStr+=''.join(str(e) for e in self.grid[i]) +'\n'
        return myStr

    def setRock( self, coord1,cord2):
        # sets the rock between coord1 and coord2
        x1,y1=coord1
        x2,y2=coord2
        if x1==x2 :
            #vertical
            step=-1 if y1>y2 else 1
            for i in range(y1,y2,step):
                x=x1-self.minx
                y=i+y1-self.miny
                self.grid[x][y]="#"
        else :
            #horizontal
            step=-1 if x1>x2 else 1
            for i in range(x1,x2,step):
                x=i+x1-self.minx
                y=y1-self.miny
                self.grid[x][y]="#"
   

r=RockStructure("Day14TestInput.txt")
print(r)