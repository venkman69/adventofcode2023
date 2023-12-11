from nis import match
from util import *
source_to_target_map={}
targetmap={}

is_between= lambda start,end,num: True if (num >= start and num <= end) else False

def overlap(s_range, t_range):
    # given two ranges return two things
    # 1. range match - single range, the start,end of overlap
    # 2. list of ranges remaining missing part
    s_start = s_range[0] 
    s_end = s_range[1] 
    t_start = t_range[0] 
    t_end = t_range[1] 
    if s_start > t_end or s_end < t_start:
        return [], [(s_start,s_end)]
    if is_between(t_start,t_end,s_start):
        if is_between(t_start, t_end,s_end):
            #wholly within
            # ....xxxxxx... 
            # .....xxxx.... 
            return (s_start, s_end),[]
        else:
            # start is inside but
            # ....xxxxxx... 
            # .....xxxxxx.. 
            return (s_start,t_end),[(t_end+1, s_end)]
    elif s_start < t_start:
        if is_between(t_start, t_end,s_end):
            # start is lower but end is inside
            # ....xxxxxx... 
            # ..xxxxxxx.... 
            return (t_start,s_end),[(s_start, t_start-1)]
        elif s_end > t_end:
            # start is lower and end is higher
            # ....xxxxxx... 
            # ..xxxxxxxxxx. 
            return (t_start, t_end),[(s_start,t_start-1),(t_end+1, s_end)]
        else:
            # start is lower and end is lower than t_start
            # ......xxxx... 
            # ..xxx........ 
            return [], [(s_start,s_end)]
    else:
        # start is higher and therefore end is also higher
        # ..xxx........ 
        # ......xxxx... 
        return [], [(s_start,s_end)]

def get_target_range_for_source(input_s_range, st_range_map):
    s_range = st_range_map[0]
    t_range = st_range_map[1]
    delta = input_s_range[0] - s_range[0]
    len_s_range = input_s_range[1] - input_s_range[0]
    new_t_start = t_range[0]+delta
    new_t_end  = t_range[0]+delta + len_s_range
    return new_t_start,new_t_end


def range_finder(stack, targettype): 
    """_summary_

    Args:
        s_range (_type_): _description_
        targettype (_type_): _description_
    Return: 
        list of matched target ranges
    """
    # 3 outcomes:
    # 1 entire range is within some range in the target map: delete this range
    #   get the target range store in another list
    # 2 part of the range is within some range: return missing parts and push to stack
    #   get the matched target range and store
    # 3 range is not in any range: delete range
    #   get the target == source range
    # stack=[s_range]
    targetlist=[]
    while stack:
        rangeitem = stack.pop()
        missing_ranges=[]
        for source_target_range in targetmap[targettype]:
            matchedrange, missingranges = overlap(rangeitem,source_target_range[0])
            if matchedrange:
                target_range=get_target_range_for_source(matchedrange, source_target_range)
                targetlist.append(target_range)
                # check for missing range if something is left
                if missingranges:
                    stack.extend(missingranges)
                break
        else:
            #if nothing matched this range
            # then set the source and target the same
            # print(f"target=source {rangeitem}")
            targetlist.append(rangeitem)

    return targetlist
   

def puzzleb(lines):
    lines=strip_lines(lines)
    for l in lines:
        if l=="":
            continue
        if l.startswith("seeds:"):
            seeds = [int(x) for x in l.split(":")[1].split()]
            seedranges= [(seeds[x],seeds[x]+seeds[x+1]-1) for x in range(0,len(seeds),2)]  
            continue
        if l[0].isalpha():
            mapfromcategories = l.split()[0].split("-")
            source = mapfromcategories[0]
            target = mapfromcategories[-1]
            source_to_target_map[source]=target
            continue
        targetstart,sourcestart, irange = [int(x) for x in l.split()]
        targetrange = (targetstart,targetstart+irange-1)
        sourcerange = (sourcestart , sourcestart+irange-1)
        if target not in targetmap:
            targetmap[target]=[[sourcerange,targetrange]]
        else:
            targetmap[target].append([sourcerange,targetrange])
    stack = seedranges
    sourcetype = "seed"
    while stack:
        targettype = source_to_target_map[sourcetype]
        stack = range_finder(stack, targettype)
        print(sourcetype,targettype) #,stack)
        sourcetype=targettype
        if targettype=="location":
            break
    print(stack)
    flat=[]
    for x in stack:
        flat.extend(x)

    print(min(flat))  

        

if __name__ == "__main__":
    # sample(puzzleb)
    mainpuzzle(puzzleb)