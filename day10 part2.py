instr_cost = {'noop': 1, 'addx': 2}

class CPU:
    
    def __init__(self):
        self.x=1
        self.instrs=[]
        self.total=0

    def loadProgram(self,filename):
        with open(filename) as file:
            for line in file:
                dir,*rest=line.rstrip().split() 
                if len(rest)>0:
                    self.instrs.append([dir,int(rest[0])])
                else:
                    self.instrs.append([dir,''])

    def runProgram(self):
        cycle=1
        outstr=''
        for i,instr in enumerate(self.instrs):
            opr=instr[0]
            opd=instr[1]
            cost=instr_cost[opr]

            # if im on a special value or if cycle cost trips me past a special boundary log me
           
            
            #tick through the cycle
            for i in range(1,cost+1):
                if len(outstr)==40:
                    print(outstr)
                    outstr=''
               
                CRTcol=(cycle % 40)-1
                if CRTcol in (self.x-1, self.x, self.x+1):
                    outstr+='#'
                else:
                    outstr+='.'

                cycle+=1
                if i==cost: #run the instruction
                    match opr:
                        case 'addx' : self.x+=opd

                if cycle in (20, 60, 100, 140, 180, 220):
                    self.total+=(self.x*cycle)
                    #print("special moment",cycle,self.x*cycle)
                
        print(outstr)
            #operate at the end of the cycle
            #print(cycle,opr,opd,self.x)
            
        print("total idx on special cycles",self.total)

cp=CPU()
cp.loadProgram("Day10Input.txt")
cp.runProgram()

