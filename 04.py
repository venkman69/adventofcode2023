from util import *

def puzzle(lines):
    total=0
    for l in lines:
        leftside,rightside=l.split("|")
        winning_numbers = set(leftside.split()[2:])
        card = l.split(":")[0]
        card_numbers = set(rightside.split())
        # print (winning_numbers)
        # print (card_numbers)
        wins=winning_numbers.intersection(card_numbers)
        count=len(wins)
        if count>0:
            total+=2**(count-1)
            print(total)

            print (wins)
        else:
            print(f"Nothing in {card}")

def puzzleb(lines):
    total=0
    cardcount={i:1 for i in range(1,len(lines)+1) }
    for l in lines:
        leftside,rightside=l.split("|")
        winning_numbers = set(leftside.split()[2:])
        cardid = int(l.split(":")[0].split()[1])
        card_numbers = set(rightside.split())
        # print (winning_numbers)
        # print (card_numbers)
        wins=winning_numbers.intersection(card_numbers)
        count=len(wins)
        for i in range(1,count+1):
            for j in range(cardcount[cardid]):
                cardcount[i+cardid]+=1

    print(cardcount)
    print(sum(cardcount.values()))

if __name__ == "__main__":
    sample(puzzleb)
    mainpuzzle(puzzleb)

    # 0
    # 1 1
    # 1 1

    # 0
    # 1 1
    # 1 1 1 1