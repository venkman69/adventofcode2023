from util import *

max_color={
"green":13,
"red":12,
"blue":14
}
subsetnumber = lambda subset, color: int(subset.replace(color,"").strip())

def puzzle(lines):
    goodgames=[]
    for l in lines:
        badline=False
        lsplitcolon=l.split(":")
        game=int(lsplitcolon[0].replace("Game","").strip())
        print(game)
        print(lsplitcolon[1])
        splitsemicolon=lsplitcolon[1].split(";")
        # ; split
        for setitem in splitsemicolon:
            commasplit = setitem.split(",")
            colcount={}
            # , split
            for subset in commasplit:
                count, color = subset.split()
                count = int(count)
                color = color.strip()
                if color in colcount:
                    colcount[color]+=count
                else:
                    colcount[color] = count
                print(f"{color}:{count}:{subset}")
            # print(colcount)
            for col,count in colcount.items():
                if max_color[col] < count:
                    print(f"**NO GOOD {game} {l}")
                    badline=True
                    break
            if badline:
                break
        if badline == False:
            goodgames.append(game)
    print(f"{sum(goodgames)}: {goodgames}")

def puzzleb(lines):
    prodlist=[]
    for l in lines:
        color_max={}
        badline=False
        lsplitcolon=l.split(":")
        game=int(lsplitcolon[0].replace("Game","").strip())
        print(game)
        # print(lsplitcolon[1])
        list_of_draws=lsplitcolon[1].split(";")
        # ; split
        for single_draw in list_of_draws:
            commasplit = single_draw.split(",")
            # , split
            for subset in commasplit:
                count, color = subset.split()
                count = int(count)
                color = color.strip()
                if color in color_max:
                    if color_max[color]<count:
                        color_max[color]=count
                else:
                    color_max[color] = count
                # print(f"{color}:{count}:{subset}")
            # print(colcount)
        prod=1
        for x in color_max.values():
            prod = prod * x
            

        print(color_max, prod)
        prodlist.append(prod)
    print(sum(prodlist))



if __name__ == "__main__":
    sample(puzzleb)
    mainpuzzle(puzzleb)