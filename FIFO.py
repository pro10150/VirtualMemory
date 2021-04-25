from random import randint

pageAddressing = []
frameNum = input("Input frame: ")
frame = []
pivot = 0

for i in range(20):
    rand = randint(0,7)
    x = frame.count(rand)
    print(rand)
    #print(pivot)
    #print(pivot == int(frameNum))
    if(len(frame) == int(frameNum)):
        #print(x == 0)
        if(x == 0):
            frame.pop(0)
        pivot = int(frameNum) - 1
    pageAddressing.insert(i,rand)
    if(len(frame) < int(frameNum)):
        if(x == 0):
            frame.insert(pivot,rand)
            pivot = pivot + 1
    print(frame)

print(pageAddressing)