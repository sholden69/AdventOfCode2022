
# this was my first go which falls down on not being recursive 

with open("Day7Input.txt") as file:
    lines = [line.rstrip() for line in file]

cwd="/"  # current working directory
idx=0
dirtotal=0
res={}
while idx < len(lines):
    line=lines[idx]
    # command  types:
    #"$ cd" - extract command and change cwd
    if line[0]=="$":
        #we're processing a command
        if line[0:4]=="$ cd":
            trgt=line[5:].rstrip()
            #print("total for ",cwd,"=",dirtotal)
            #print("cd ->", trgt)
            match trgt:
                case "..": 
                    #take last dir off cwd
                    cwd=cwd[0:cwd.rfind("/")-1]
                    #print("up a dir ->", cwd)
                case "/": 
                    cwd="/"
                case _: 
                    if (cwd=="/"):
                        cwd+=trgt
                    else:
                        cwd+="/"+trgt
                    #print ("cwd=",cwd)
            dirtotal=0  #reset dirtotal for new directory
            idx+=1
        elif line[0:4]=="$ ls":
            #print("dir listing")
            idx+=1
    else:
        #we're accumulating a file into our list
        while True:
            thisline=lines[idx].split() 
            if thisline[0]!="dir":
                dirtotal+=int(thisline[0])
            idx+=1
            if (idx>=len(lines)) or (lines[idx][0]=="$"):
                #print("files in",cwd,dirtotal)
                res[cwd]=dirtotal
                break


print("results*")
for r in res:
    print(r,res[r])


def sub_dirs(akey,ares):
    #sum any sub-dir sizes into
    mytot=0
    for k in ares:
        if (k!=akey) and (akey in k) : ##ignore me
            mytot+=ares[k]
    return mytot

     

# build a tree of res and look for answer 
print("final results***")
cum_res={}
ans=0
for key in res:
    # / = / + /a + /a/e + /d + /d 
    # /a = /a + /e 
    cum_res[key]=res[key]+sub_dirs(key,res)
    if cum_res[key]<100000:
        ans+=cum_res[key]
        print("including",key,cum_res[key])
    else:
        print("excluding",key,cum_res[key])

print("part 1 ans",ans)
