import math
from util import *

def quadratic_solve(a,b,c):

    # ax^2 + bx + c = 0
    # -b - sqrt(b^2 - 4ac)/2a 
    # -b + sqrt(b^2 - 4ac)/2a 
    b2_4ac = (b**2) - (4 * a * c)
    b2_4ac_sqrt = math.sqrt(b2_4ac)
    sola = (-b - b2_4ac_sqrt)/(2*a)
    solb = (-b + b2_4ac_sqrt)/(2*a)
    print(sola,solb)
    return sola, solb

def combos(total_time, min_distance):
    # 0 1 2 3 4 5 <odd sequence
    #   1 2 3 4   range that should be tested
    #   1 2       range that is half of the above 
    #---
    # 0 1 2 3 4 5 6 <even sequence
    #   1 2 3 4 5  range that should be tested
    #   1 2 3     range that is half of the above 
    #---
    half_time = int(total_time/2)
    adjust=0
    if half_time * 2 == total_time:
        # this is an even sequence
        # so times 2 minus 1
        adjust=-1

    success_count=0
    for charge_time in range(half_time,1,-1):
        distance = (total_time - charge_time) * charge_time
        if distance <= min_distance:
            break
        print(charge_time, distance)
        success_count+=1

    print (success_count*2+adjust)
    return (success_count*2+adjust)

def puzzle(lines):
    timestring = lines[0].split(":")[1]
    diststring = lines[1].split(":")[1]
    times = [ int(x) for x in timestring.split()]
    distances = [ int(x) for x in diststring.split()]
    winlist=[]
    for t,d in zip(times, distances):
        win=combos(t,d)
        winlist.append(win)
    prod=1    
    for win in winlist:
        prod = prod * win

    print(prod)
    # print(distances)
def puzzleb(lines):
    timestring = lines[0].split(":")[1]
    timestring = timestring.replace(" ","")
    diststring = lines[1].split(":")[1]
    diststring = diststring.replace(" ","")

    time = int(timestring)
    dist = int(diststring)
    # win=combos(time,dist)
    #  distance = (total_time - charge_time) * charge_time
    # distance = total_time * charge_time - charge_time ^2
    # total_time * charge_time - charge_time ^2 - distance = 0
    # -1 * charge_time ^2 + total_time * charge_time + (- distance) = 0
    # a    x^2             + b           x           + c
    # ctime*x - x*x - min_distance = 0
    # -1 * x^2 + time *x + (-min_distance) = 0
    # a          b            c

    # combos(time, dist)
    sola, solb= quadratic_solve(-1, time,-dist)
    adjust=0
    if time % 2 == 0:
        adjust = -1
        print("adjust")
    print(int(sola) - int(solb)+adjust)
    # sola, solb= quadratic_solve(-1, 7,-9)
    # print(int(sola) - int(solb))
    # sola, solb= quadratic_solve(-1, 15,-40)
    # print(int(sola) - int(solb))
    # sola, solb= quadratic_solve(-1, 30,-200)
    
    # print(int(sola) - int(solb) -1)
    

    # print(win)
    # print(distances)

if __name__ == "__main__":
    # sample(puzzleb)
    mainpuzzle(puzzleb)