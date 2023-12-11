from util import *

def search_for_parts(x,y,grid):
    parts=[]
    for j in [-1,0,1]: #yaxis
        for i in [-1,0,1]: #xaxis
            if y+j <0:
                continue
            if x+i <0:
                continue
            if y+j > len(grid):
                continue
            if x+i > len(grid[0]):
                continue
            
            c=grid[y+j][x+i]
            if c.isdigit():
                part =get_part(grid, y+j, x+i)
                parts.append(part)
    return parts
def get_part(grid, y, x):
    numstring=grid[y][x]
    char = numstring
    #search backwards
    i=0
    while True: 
        i=i-1
        if x+i <0:
            break
        char = grid[y][x+i]
        if char.isdigit():
            numstring = char + numstring
            grid[y][x+i]="."
        else:
            break
    #search forwards
    i=0
    while True: 
        i=i+1
        if x+i >= len(grid[0]):
            break
        char = grid[y][x+i]
        if char.isdigit():
            numstring = numstring+char
            grid[y][x+i]="."
        else:
            break
    return int(numstring)


def puzzle(lines):
    lines = strip_lines(lines)
    grid=[]
    for l in lines:
        grid.append(list(l))

    all_parts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c = grid[y][x]
            # print(c)
            if not c.isdigit() and c != ".":
                #symbol
                parts=search_for_parts(x,y,grid)
                all_parts.extend(parts)

    print(all_parts)
    print(sum(all_parts))

def puzzleb(lines):
    lines = strip_lines(lines)
    grid=[]
    for l in lines:
        grid.append(list(l))

    all_parts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c = grid[y][x]
            # print(c)
            if not c.isdigit() and c != ".":
                #symbol
                parts=search_for_parts(x,y,grid)
                if len(parts)==2:
                    all_parts.append(parts[0]*parts[1])

    print(all_parts)
    print(sum(all_parts))


if __name__ == "__main__":
    # sample(puzzle)
    # mainpuzzle(puzzle)
    sample(puzzleb)
    mainpuzzle(puzzleb)