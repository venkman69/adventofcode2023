import sys
import os
import time


currenttimemillis=lambda: int(round(time.time() * 1000))
fn=sys.argv[0]

fnbase=os.path.basename(fn)
fnname,fnext = os.path.splitext(fnbase)
samplefn=fnname+".sample"
puzinpfn=fnname+".input"

def strip_lines(lines):
    return [x.strip() for x in lines]

def sample(puzzle_func):
    with open(samplefn) as f:
        lines = f.readlines()
    return puzzle_func(lines)

def mainpuzzle(puzzle_func):
    global puzzle, puzzleb
    with open(puzinpfn) as f:
        lines = f.readlines()
    return puzzle_func(lines)


