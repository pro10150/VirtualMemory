from random import randint
import tkinter as tk
import time


H = 500
W = 800



root = tk.Tk()

canvas = tk.Canvas(root, height=H,width=W)
canvas.pack()
greet = tk.Label(
    text="Virtual Memory Simulation"
)
greet.place(x=150,y=0)
greet.config(font=("Open Sans", 30))
inputFrameText = tk.Label(
    text="Input Frame Size",
)
inputFrameText.place(x=100,y=50)
inputFrameText.config(font=("Open Sans", 20))

frameSize = tk.StringVar(root)
frameSize.set(1)

inputFrame = tk.OptionMenu(root, frameSize, 1,2,3,4,5,6,7,8,9,10)
inputFrame.place(x=350,y=50,width=50)
inputFrame.config(font=("Open Sans", 15))


variable = tk.StringVar(root)
variable.set("FIFO") # default value

w = tk.OptionMenu(root, variable, "FIFO", "OPT", "LRU")
w.place(x=410,y=50)
w.config(font=("Opens Sans",15))



def testButton():

    if(variable.get() == "FIFO"):
        FIFO()
    elif(variable.get() == "OPT"):
        OPT()
    else:
        LRU()

def OPT():
    pageAddressing = []
    capacity = int(frameSize.get())
    s = []
    pivot = 0
    processList = []
    pageFaults = 0
    flag = False
    popFlag = False
    previousS = []

    frame = tk.Frame(
        bg="grey",
        width=810,
        height=410
    )
    frame.place(y=100)
    for widgets in frame.winfo_children():
        widgets.destroy()
    y = 50
    X = 10

    for i in range(10):
        rand = randint(0, 7)
        processList.insert(i, rand)

    for label in range(len(frame.winfo_children())):
        frame.winfo_children(label).place_forget()
    testLabel = tk.Label(frame,
                         text="process list = " + str(processList))
    testLabel.place(x=200, y=10)
    testLabel.config(font=("Open Sans", 15))

    for i in processList:
        # rand = randint(0,7)
        x = s.count(i)
        # print(i)
        # print(pivot)
        # print(pivot == int(frameNum))
        if (len(s) == int(capacity)):
            # print(x == 0)
            if (x == 0):
                s.pop(0)
                pageFaults += 1
                flag = True
                popFlag = True
            else:
                flag = False
            pivot = int(capacity) - 6
        if (len(s) < int(capacity)):
            if (x == 0):
                s.insert(pivot, i)
                pivot = pivot + 1
                if popFlag:
                    print("check")
                    flag = True
                else:
                    print("here")
                    print(s)
                    flag = True
                    pageFaults += 1
            else:
                flag = False

        for process in range(int(frameSize.get())):
            if len(s) < capacity:
                if process < len(s):
                    testLabel = tk.Label(frame,
                                            text="[" + str(s[process]) + "]")
                    testLabel.place(x=X, y=y)
                    y += 20
                else:
                    testLabel = tk.Label(frame,
                                            text="[  ]")
                    testLabel.place(x=X, y=y)
                    y += 20
            else:
                testLabel = tk.Label(frame,
                                    text="[" + str(s[process]) + "]")
                testLabel.place(x=X, y=y)
                y += 20
                # time.sleep(0.5)
        if flag:
            testLabel = tk.Label(frame,
                            text="M ")
            testLabel.place(x=X, y=y)
        else:
            testLabel = tk.Label(frame,
                                 text="H  ")
            testLabel.place(x=X, y=y)
        y = 50
        X += 30
        # print(s)
        testLabel = tk.Label(frame,
                             text="Page Fault = " + str(pageFaults))
        testLabel.place(x=300, y=200)
        testLabel.config(font=("Open Sans", 15))
        previousS = s


def FIFO():
    pageAddressing = []
    processList = []
    capacity = int(frameSize.get())
    s = []
    pivot = 0
    pageFaults = 0
    flag = False
    popFlag = False

    for i in range(10):
        rand = randint(0, 7)
        processList.insert(i, rand)

    frame = tk.Frame(
        bg="grey",
        width=810,
        height=410
    )
    frame.place(y=100)
    for widgets in frame.winfo_children():
        widgets.destroy()
    y = 50
    X = 10

    for label in range(len(frame.winfo_children())):
        frame.winfo_children(label).place_forget()
    testLabel = tk.Label(frame,
                         text="process list = " + str(processList))
    testLabel.place(x=200, y=10)
    testLabel.config(font=("Open Sans", 15))

    for i in processList:
        # rand = randint(0,7)
        x = s.count(i)
        # print(i)
        # print(pivot)
        # print(pivot == int(frameNum))
        if len(s) == int(capacity):
            # print(x == 0)
            if x == 0:
                s.pop(0)
                pageFaults += 1
            pivot = int(capacity) - 1
            flag = True
            popFlag = True
        else:
            flag = False
        if len(s) < int(capacity):
            if (x == 0):
                s.insert(pivot, i)
                pivot = pivot + 1
                if popFlag:
                    flag = False
                else:
                    flag = False
                    pageFaults += 1
            else:
                flag = True
        for process in range(int(frameSize.get())):
            if len(s) < capacity:
                if process < len(s):
                    testLabel = tk.Label(frame,
                                            text="[" + str(s[process]) + "]")
                    testLabel.place(x=X, y=y)
                    y += 20
                else:
                    testLabel = tk.Label(frame,
                                        text="[  ]")
                    testLabel.place(x=X, y=y)
                    y += 20
            else:
                testLabel = tk.Label(frame,
                                    text="[" + str(s[process]) + "]")
                testLabel.place(x=X, y=y)
                y += 20
                # time.sleep(0.5)
            if flag:
                testLabel = tk.Label(frame,
                                     text="H  ")
                testLabel.place(x=X, y=y)
            else:
                testLabel = tk.Label(frame,
                                     text="M ")
                testLabel.place(x=X, y=y)
        y = 50
        X += 30
        # print(s)
    testLabel = tk.Label(frame,
                         text="Page Fault = " + str(pageFaults))
    testLabel.place(x=300, y=200)
    testLabel.config(font=("Open Sans", 15))




def LRU():
    processList = []
    s = []
    flag = False
    previousS = []

    pageFaults = 0
    capacity = int(frameSize.get())

    for i in range(10):
        rand = randint(0, 7)
        processList.insert(i, rand)

    # print(processList)
    # print(variable.get())
    # print(frameSize.get())
    frame = tk.Frame(
        bg="grey",
        width=810,
        height=410
    )
    frame.place(y=100)
    for widgets in frame.winfo_children():
        widgets.destroy()
    y = 50
    x = 10
    for label in range(len(frame.winfo_children())):
        frame.winfo_children(label).place_forget()
    testLabel = tk.Label(frame,
                         text="process list = " + str(processList))
    testLabel.place(x=200, y=10)
    testLabel.config(font=("Open Sans", 15))
    # if (variable.get() == "FIFO"):
    #     FIFO()
    # elif (variable.get() == "OPT"):
    #     OPT()
    # else:
    #     LRU()
    for i in processList:

        # If i is not present in currentPages list
        if i not in s:

            # Check if the list can hold equal pages
            if (len(s) == int(capacity)):
                s.remove(s[0])
                s.append(i)

            else:
                s.append(i)

            # Increment Page faults
            flag = True
            pageFaults += 1

        # If page is already there in
        # currentPages i.e in Main
        else:

            # Remove previous index of current page
            s.remove(i)
            flag = False
            # Now append it, at last index
            s.append(i)
        for process in range(int(frameSize.get())):
            if len(s) < capacity:
                if process < len(s):
                    testLabel = tk.Label(frame,
                                         text="[" + str(s[process]) + "]")
                    testLabel.place(x=x, y=y)
                    y += 20
                else:
                    testLabel = tk.Label(frame,
                                         text="[  ]")
                    testLabel.place(x=x, y=y)
                    y += 20
            else:
                testLabel = tk.Label(frame,
                                     text="[" + str(s[process]) + "]")
                testLabel.place(x=x, y=y)
                y += 20
        # time.sleep(0.5)
            if flag:
                testLabel = tk.Label(frame,
                                     text="M ")
                testLabel.place(x=x, y=y)
            else:
                testLabel = tk.Label(frame,
                                     text="H  ")
                testLabel.place(x=x, y=y)

        y = 50
        x += 30
        previousS = s

    testLabel = tk.Label(frame,
                            text="Page Fault = " + str(pageFaults))
    testLabel.place(x=300, y=200)
    testLabel.config(font=("Open Sans", 15))

runButton = tk.Button(
    text="RUN",
    height=1,
    width=10,
    command=testButton
)
runButton.place(x=700, y=50)
runButton.config(font=("Open Sans", 10))

root.resizable(width=False, height=False)
root.mainloop()
