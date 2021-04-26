
from random import randint

pageAddressing = []
frameNum = input("Input frame: ")
frame = []
pivot = 0
processList = []
pageFault = 0

for i in range(10):
    rand = randint(0, 7)
    processList.insert(i,rand)

print(processList)

for process in processList:
    # rand = randint(0,7)
    x = frame.count(process)
    print(process)
    #print(pivot)
    #print(pivot == int(frameNum))
    if(len(frame) == int(frameNum)):
        #print(x == 0)
        if(x == 0):
            frame.pop(0)
            pageFault += 1
        pivot = int(frameNum) - 6
    if(len(frame) < int(frameNum)):
        if(x == 0):
            frame.insert(pivot,process)
            pivot = pivot + 1
    print(frame)

    print("page fault = {}".format(pageFault))


