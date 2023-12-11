from re import A
from util import *
sourcetargetmap={}
sourcetypetargettypemap={}

is_between= lambda start,end,num: True if (num >= start and num <= end) else False

def seed_tracer(source_number,sourcetype):
    if not sourcetype in sourcetypetargettypemap:
        return source_number
    targettype = sourcetypetargettypemap[sourcetype]
    for sstart,tstart,irange in sourcetargetmap[sourcetype][targettype]:
        if source_number >= sstart and source_number <= sstart+irange:
            diff=source_number - sstart
            tgtnum = tstart+diff
            break
    else:
        tgtnum = source_number
    # print(sourcetype,source_number, targettype, tgtnum)
    # print(sourcetype,source_number,targettype,tgtnum)
    return seed_tracer(tgtnum, targettype)

class myrange():
    def __init__(self, start, target, length):
        self.start = start
        self.length = length
        self.end = start+length
        self.target_start = target
        self.target_end = target+length

    def get_overlap(self, start, end):
        # response is overlap_target_start, overlap_target_end, remaining_start, remaining_end
        if start >= self.start and start <= self.end:
            if end <= self.end: #fully within
                start_diff = start - self.start
                return self.target_start+start_diff, self.target_start+start_diff+(end - start),0,0
            else: #end is greater than this range so send this range's end
                start_diff = start - self.start
                return self.target_start+start_diff, self.target_end,self.end+1, end
        elif end >=self.start and end <= self.end:
            return self.start, end # start is less than range start but end is within
        else:
            return -1, -1


def seed_tracerb(ranges,sourcetype,targettype):
    # find target ranges and return a list of ranges
    tranges=[]
    # search by existing ranges to see what can match
    for range in ranges:
        r_start = range[0]
        r_end = range[1]
        r_range = r_end - r_start
        while r_start != r_end:
            for s_start,s_end,t_start,t_end in sourcetargetmap[sourcetype][targettype]:
                # check if source and range fall within sstart -> sstart+irange
                # it can be a partial
                # if fully within then capture the 'new' target start and range
                if is_between (s_start,s_end ,r_start):
                    if is_between(s_start, s_end,r_end):
                        #this is wholly between
                        # ....xxxxxx... 
                        # .....xxxx.... 
                        start_diff = r_start - s_start
                        trange = [t_start+start_diff, t_start+start_diff+r_range]
                        tranges.append(trange)
                        r_start = r_end
                        break #all done
                    else: # start is after but end is not
                        # ....xxxxxx... 
                        # .....xxxxxx.. 
                        start_diff = r_start - s_start
                        trange = [t_start+start_diff, t_end]
                        tranges.append(trange)
                        # set new r_start to be where s_end is and redo while loop
                        r_start = s_end+1
                        break
                elif is_between(s_start, s_end, r_end): #end is between but start is not
                    # ....xxxxxx... 
                    # ..xxxxxxx.... 
                    end_diff =   s_end - r_end
                    trange = [t_start, t_end- end_diff]
                    tranges.append(trange)
                    # new end is s_start
                    r_end = s_start-1
                    break # go back to while loop
                elif s_start > r_start and r_end > s_end:
                    # ....xxxxxx... 
                    # ..xxxxxxxxxx. 
                    # this should split the range into two
                    # this could be a recursive call to figure out the split
                    trange = [ t_start, t_end] # the whole range
                    tranges.append(trange)
                    # two ranges come out of this
                    range1 = [r_start, s_start-1]
                    range2 = [s_end+1, r_end]
                    new_ranges = [range1,range2]
                    range_result = seed_tracerb(new_ranges, sourcetype, targettype)
                    tranges.extend(range_result)
                    r_start = r_end
                    break
                # if s_start is outside then loop through other items
            else: # if no match in entire set then it is target = source rule
                trange = [r_start, r_end]
                r_start=r_end
                tranges.append(trange)
    return tranges




def puzzle(lines):
    for l in lines:
        lstrip = l.strip()
        if len(lstrip)==0:
            continue
        if lstrip.startswith("seeds:"):
            seeds = [int(x) for x in lstrip.split(":")[1].split()]
            
            continue
        if lstrip[0].isalpha():
            mapfromcategories = lstrip.split()[0].split("-")
            source = mapfromcategories[0]
            target = mapfromcategories[-1]
            sourcetypetargettypemap[source]=target
            continue
        
        targetstart,sourcestart, irange = [int(x) for x in lstrip.split()]
        if source not in sourcetargetmap:
            sourcetargetmap[source]= {target: [[sourcestart,targetstart,irange]]}
        elif target not in sourcetargetmap[source]:
            sourcetargetmap[source][target]=[[sourcestart,targetstart,irange]]
        else:
            sourcetargetmap[source][target].append([sourcestart,targetstart,irange])
            
            

    locations=[]
    for seed in seeds:    
        location = seed_tracer(seed,"seed")
        locations.append(location)
    print(locations)
    print(min(locations))
    # print (seeds)
    pass

def puzzleb(lines):
    for l in lines:
        lstrip = l.strip()
        if len(lstrip)==0:
            continue
        if lstrip.startswith("seeds:"):
            seeds = [int(x) for x in lstrip.split(":")[1].split()]
            seedranges= [range(seeds[x],seeds[x]+seeds[x+1]+1) for x in range(0,len(seeds),2)]  
            continue
        if lstrip[0].isalpha():
            mapfromcategories = lstrip.split()[0].split("-")
            source = mapfromcategories[0]
            target = mapfromcategories[-1]
            sourcetypetargettypemap[source]=target
            continue
        
        targetstart,sourcestart, irange = [int(x) for x in lstrip.split()]
        targetrange = range(targetstart,irange+1)
        sourcerange = range(sourcestart , irange+1)
        if source not in sourcetargetmap:
            sourcetargetmap[source]= {target: [[sourcerange,targetrange]]}
        elif target not in sourcetargetmap[source]:
            sourcetargetmap[source][target]=[[sourcerange,targetrange]]
        else:
            sourcetargetmap[source][target].append([sourcerange,targetrange])

    locations=[]
    for seedandrange in seedranges:
        sourcetype = "seed"
        targettype = "soil"
        ranges = [seedandrange]
        while targettype != "location":
            ranges = seed_tracerb(ranges,sourcetype,targettype)
            sourcetype = targettype
            targettype = sourcetypetargettypemap[targettype]
        locations.extend(ranges)

    print(locations)
    print(min(locations)[0])
    # print (seeds)
    pass



if __name__ == "__main__":
    # sample(puzzleb)
    mainpuzzle(puzzleb)