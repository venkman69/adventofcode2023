from util import *
import re

def sort_by_strlen(dictitem):
    return sorted(dictitem.keys(),key=lambda x : len(x), reverse=True)

nummap={"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5",
     "ten":"10", "eleven":"11",
    "twelve":"12", "thirteen":"13", "fourteen":"14", "fifteen":"15", 
      "twenty":"20",
    "thirty":"30", "forty":"40", "fifty":"50",
 "hundred":"100"
    }
problem_sets=[{ "sixty":"60", "sixteen":"16", "six":"6"},
    {"seven":"7", "seventeen":"17", "seventy":"70"},
    {"eight":"8",  "eighty":"80",  "eighteen":"18"}, 
    {"nine":"9", "ninety":"90","nineteen":"19"}]

p_items = [sort_by_strlen(ps) for ps in problem_sets]

def problem_set_check(l):
    num_and_index=[]
    for pi in range(len(p_items)):
        p = p_items[pi]
        for numstr in p:
            find_index = l.find(numstr)
            if find_index <0:
                continue
            num_and_index.append((problem_sets[pi][numstr],find_index))
            break
    if len(num_and_index)>0:
        print("****",num_and_index)
    return num_and_index

def dorepl(data):
    data = data.replace("one", "o1e")
    data = data.replace("two", "t2o")
    data = data.replace("three", "t3e")
    data = data.replace("four", "f4r")
    data = data.replace("five", "f5e")
    data = data.replace("six", "6")
    data = data.replace("seven", "7n")
    data = data.replace("eight", "e8t")
    data = data.replace("nine", "n9e")
    return data
def puzzle(lines):

    passlist = sort_by_strlen(nummap)

    sum=0
    orderednums = []
    for l in lines:
        l=l.strip()
        l=dorepl(l)
        num_and_index=[]
        # for k in passlist:
        #     find_index = l.find(k)
        #     if find_index <0:
        #         continue
        #     num_and_index.append((nummap[k],find_index))
        for c in range(len(l)):
            if l[c].isdigit():
                num_and_index.append((l[c], c ))
        # do the problem set
        # ps_result = problem_set_check(l) 
        # num_and_index.extend(ps_result)
        ordered_nums = sorted(num_and_index, key = lambda x: x[1])
        ordered_final = [x[0] for x in ordered_nums]
        # print(f"{l}={ordered_final}")
        orderednums.append("".join(ordered_final))
        first = int(ordered_final[0])
        last = int(ordered_final[-1])
        num = int(f"{first}{last}")
        print(f"{l}={num}")
        sum+=num
    print (sum)
    return orderednums,lines


if __name__ == "__main__":
    sample(puzzle)
    # sample(part2)
    # mainpuzzle(part2)
    mainpuzzle(puzzle)
