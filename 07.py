from util import *
from functools import cmp_to_key
import string
digs = string.digits + "TJQKA"

fiveofkind=6
fourofkind=5
fullhouse=4
threeofkind=3
twopair = 2
onepair=1
highcard=0
handmap={
    fiveofkind:"fiveofkind",
    fourofkind:"fourofkind",
    fullhouse:"fullhouse",
    threeofkind:"threeofkind",
    twopair:"twopair",
    onepair:"onepair",
    highcard:"highcard",
}

cardvalue={
"A":14,
"K":13,
"Q":12,
"J":1,
"T":10,
"9":9,
"8":8,
"7":7,
"6":6,
"5":5,
"4":4,
"3":3,
"2":2,
}
def handtoint(hand):
    revhand = hand[::-1]
    base = 15
    base10num=0
    ind=0
    for card in revhand:
        base10num = base10num+ cardvalue[card]* (base**ind)
        ind+=1

    return(base10num)

def handtorank(hand):
    fiveofkind=6
    fourofkind=5
    fullhouse=4
    threeofkind=3
    twopair = 2
    onepair=1
    highcard=0
#  Jxxxx = five
#  fourofki
    counts = [hand.count(i) for i in set(hand) if i != "J"]
    jokers = hand.count("J")
    result=0
    if len(counts)>0:
        highest_kind=max(counts)
        counts.remove(highest_kind)
        counts.append(highest_kind+jokers)
    else:
        counts=[jokers]
    
    if 5 in counts:
        print(f"five of a kind {hand}")
        return fiveofkind
    if 4 in counts:
        print(f"four of a kind {hand}")
        return fourofkind
    if 3 in counts:
        if 2 in counts:
            print(f"fullhouse {hand}")
            return  fullhouse
        if 1 in counts:
            print(f"three of a kind {hand}")
            return threeofkind
    if counts.count(2) == 2: 
        print(f"two pair {hand}")
        return  twopair
    if counts.count(2)== 1:
        print(f"one pair {hand}")
        return onepair
    if 1 in counts:
        print (f"highcard {hand}")
        return highcard
    print(f"something wrong {hand}")

def hand_compare(hand1, hand2):
    #check rank first
    if hand1["rank"]> hand2["rank"]:
        return 1
    elif hand1["rank"]<hand2["rank"]:
        return -1
    else:
        if hand1["int"]>hand2["int"]:
            return 1
        elif hand1["int"]<hand2["int"]:
            return -1
        else:
            return 0


def puzzle(lines):
    hands_and_bet = []       
    for l in lines:
        lsplit=l.split()
        hand=lsplit[0]
        handint = handtoint(hand)
        handrank = handtorank(hand)
        bet = int(lsplit[1])
        hands_and_bet.append({"int":handint,"rank":handrank, "hand":hand,  "bet":bet})
        print(hand)
    
    sorted_hands=sorted(hands_and_bet,key=cmp_to_key(hand_compare))
    i=1
    total=0
    for hand in sorted_hands:
        total=total+hand['bet']*i
        i+=1
        print (f"{hand} :**{handmap[hand['rank']]}:  {hand['bet']*i}")
    print(total)

if __name__ == "__main__":
    print("KTJJT",handtorank("KTJJT"))
    # print("A123J",handtorank("A123J"))
    # print("A133J",handtorank("A133J"))
    # print("A333J",handtorank("A333J"))
    # print("A553J",handtorank("A553J"))
    # print("3333J",handtorank("3333J"))
    
    sample(puzzle)
    mainpuzzle(puzzle)
    # print(handvalue("AAA8"))
    # print(handvalue("AKTA"))