def checkTreeVisible(l:list, posn:int, ht:int) -> bool:
        # checks along in both directions for visible
        lftSlice=l[0:posn-1]
        if max(lftSlice)<ht:
            return True
        rSlice=l[posn:]
        if max(rSlice)<ht:
            return True
        return False
        
def checkTreeScenic(l:list, posn:int, ht:int) -> int:
        # checks along in both directions for visible
        res1=0
        lftSlice=l[0:posn-1]
        #go backwards from end of list until we reach edge or a tree >=ht
        i=len(lftSlice)-1
        while (i>=0):
            res1+=1
            if (lftSlice[i]>=ht):  #stop when we hit a tree of equal height
                break
            i-=1
        res2=0
        rSlice=l[posn:]
        #go forwards from here  
        i=0
        while(i<len(rSlice) ):
            res2+=1
            if (rSlice[i]>=ht): 
                break
            i+=1
        
        return res1*res2


class Forest:
#holds the rectangle of the forest
# row, columns. top right coord [1,1]
    def __init__(self,fn):
        self.rows=[]
        with open(fn) as f:
            for line in f:
                thisrow=[int(c) for c in line if c.isnumeric()]
                self.rows.append(thisrow)
        self.nrows = len(self.rows)
        self.ncols = len(self.rows[0])

    def getHeight(self,row,col) -> int:
        #return the height of the tree at coord x,Y
        return(self.rows[row-1][col-1])

    def __repr__(self):
        res=''
        for r in self.rows:
            res+=r.__repr__()+'\n'
        return res

    def getCol(self,col) -> list[int]:
        return [x[col-1] for x in self.rows]
    
    def getRow(self,row) -> list[int]:
        return self.rows[row-1]

    def isVisible(self,row,col) -> bool:
        ##anything round the edge us visibile
        #print("checking row:",row,"col:",col)
        if ((row==1) or (col==1) or (row==self.nrows) or (col==self.ncols)) :
            return True
        myHeight=self.getHeight(row,col) 
        #check along my row & columns
        #print("checking (row,col) (",row,",",col,")")
        if checkTreeVisible(self.getRow(row),col,myHeight) or \
           checkTreeVisible(self.getCol(col),row,myHeight):
            #print("visible tree (row,col) (",row,",",col,") height=",myHeight)
            return True
        return False

    def width(self):
        return self.ncols

    def height(self):
        return self.nrows


    def countVisible(self) -> int:
        res=0
        for r in range(1,self.nrows+1):
            for c in range(1,self.ncols+1):
                if self.isVisible(r,c):
                    res+=1
        return res

    def scenicScore(self,row,col) -> int:
    # go up down and left/right and count to edge or tree >= height
        myHeight=self.getHeight(row,col) 
        return checkTreeScenic(self.getRow(row),col,myHeight) * \
               checkTreeScenic(self.getCol(col),row,myHeight)



fst=Forest("Day8Input.txt")
print(fst)
print("Part 1: visible trees",fst.countVisible())
max_score=0
for r in range(1,fst.nrows):
    for c in range(1,fst.ncols):
        if (r!=1) and (c!=1) and (r!=fst.nrows) and (c!=fst.ncols):
           this_score=fst.scenicScore(r,c)
           #print("row,col:height",r,c,":",fst.getHeight(r,c),"score:",this_score)
           if (this_score>max_score):
                max_score=this_score

print("Part 2: max_score:",max_score)





