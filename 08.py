import math
from util import *

def puzzle(lines):
    rlseq=lines[0]
    mapsequence=[]
    sourcemap={}
    count=0
    for l in lines[2:]:
        lstrip = l.replace(" ","")
        src, rhlh = lstrip.split("=")
        src = src.strip()
        lh,rh  = rhlh.strip().replace("(","").replace(")","").strip().split(",")
        print (src, lh, rh)
        mapsequence.append((src,lh,rh))
        sourcemap[src]=count
        count+=1
    #find start
    i = sourcemap["AAA"]
    direction = "AAA"
    # start with line 'i'
    steps=0
    while direction != "ZZZ":
        lh,rh = mapsequence[i][1:]
        rlindex = steps % len(rlseq) 
        left_or_right = rlseq[rlindex]
        if left_or_right=="R":
            print(rh)
            direction = rh
        else:
            print(lh)
            direction = lh
        i= sourcemap[direction]
        steps += 1
    print(steps)        


def puzzleb(lines):
    rlseq=lines[0]
    rlseq= rlseq.replace("L","0").replace("R", "1")
    rlseq = [ int(x) for x in rlseq]
    mapsequence=[]
    sourcemap={}
    count=0
    for l in lines[2:]:
        lstrip = l.replace(" ","")
        src, rhlh = lstrip.split("=")
        src = src.strip()
        lh,rh  = rhlh.strip().replace("(","").replace(")","").strip().split(",")
        print (src, lh, rh)
        mapsequence.append((src,lh,rh))
        sourcemap[src]=count
        count+=1
    newmapsequence=[]
    for src, lh, rh in mapsequence:
        newmapsequence.append([src,sourcemap[lh],sourcemap[rh]])
    mapsequence=newmapsequence
    #find start
    startingpoints=[k for k in sourcemap.keys() if k.endswith("A")]
    endingpoints=[k for k in sourcemap.keys() if k.endswith("Z")]
    endingindices = set([sourcemap[x] for x in endingpoints])

    startingindices = [sourcemap[x] for x in startingpoints]
    print(startingpoints)
    print(startingindices)
    print(endingpoints)
    print(endingindices)
    # start with line 'i'
    rlseqlen=len(rlseq)
    
    milliold = currenttimemillis()
    stepsperpath=[]
    for startindex in startingindices:
        steps=0
        path=startindex
        while path not in endingindices:
            rlindex = steps % rlseqlen
            left_or_right = rlseq[rlindex]
            path = mapsequence[path][1+left_or_right]
            steps += 1
        print(steps)
        stepsperpath.append(steps)
    print(stepsperpath)
    lcm(stepsperpath)
def lcm(stepsperpath):
    lcm = 1
    for i in stepsperpath:
        lcm = lcm*i//math.gcd(lcm, i)
    print(lcm)

if __name__ == "__main__":
    # sample(puzzleb,fnextn="sample3")
    mainpuzzle(puzzleb)