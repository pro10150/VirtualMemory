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

    # newLabel = tk.Label(
    #     text=inputFrame.get()
    # )
    # newLabel.pack()
    # newLabel.pack_forget()
    # processList = []
    # s = []
    #
    pageFaults = 0
    # capacity = int(frameSize.get())
    #
    # for i in range(10):
    #     rand = randint(0, 7)
    #     processList.insert(i, rand)
    #
    # print(processList)
    # print(variable.get())
    # print(frameSize.get())
    # frame = tk.Frame(
    #     bg="grey",
    #     width=800,
    #     height=400
    # )
    # frame.place(y=100)
    # for widgets in frame.winfo_children():
    #     widgets.destroy()
    # y=50
    # x=10
    # for label in range(len(frame.winfo_children())):
    #     frame.winfo_children(label).place_forget()
    # testLabel = tk.Label(frame,
    #                      text="process list = " + str(processList))
    # testLabel.place(x=200, y=10)
    # testLabel.config(font=("Open Sans",15))
    if(variable.get() == "FIFO"):
        FIFO()
    elif(variable.get() == "OPT"):
        OPT()
    else:
        LRU()
    # for i in processList:
    #
    #     # If i is not present in currentPages list
    #     if i not in s:
    #
    #         # Check if the list can hold equal pages
    #         if (len(s) == int(capacity)):
    #             s.remove(s[0])
    #             s.append(i)
    #             print(s)
    #
    #         else:
    #             s.append(i)
    #             print(s)
    #
    #         # Increment Page faults
    #         pageFaults += 1
    #
    #     # If page is already there in
    #     # currentPages i.e in Main
    #     else:
    #
    #         # Remove previous index of current page
    #         s.remove(i)
    #
    #         # Now append it, at last index
    #         s.append(i)
    #         print(s)
    #     for process in range(int(frameSize.get())):
    #         if len(s) < capacity:
    #             if process < len(s):
    #                 testLabel = tk.Label(frame,
    #                                      text="[" + str(s[process]) + "]")
    #                 testLabel.place(x=x, y=y)
    #                 y += 20
    #             else:
    #                 testLabel = tk.Label(frame,
    #                                      text="[  ]")
    #                 testLabel.place(x=x, y=y)
    #                 y += 20
    #         else:
    #             testLabel = tk.Label(frame,
    #                                  text="[" + str(s[process]) + "]")
    #             testLabel.place(x=x, y=y)
    #             y += 20
    #     # time.sleep(0.5)
    #     y = 50
    #     x += 30

def OPT():
    pageAddressing = []
    capacity = int(frameSize.get())
    s = []
    pivot = 0
    processList = []
    pageFaults = 0

    frame = tk.Frame(
        bg="grey",
        width=800,
        height=400
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
            pivot = int(capacity) - 6
        if (len(s) < int(capacity)):
            if (x == 0):
                s.insert(pivot, i)
                pivot = pivot + 1
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
                y = 50
                X += 30
        # print(s)
        testLabel = tk.Label(frame,
                             text="Page Fault = " + str(pageFaults))
        testLabel.place(x=300, y=200)
        testLabel.config(font=("Open Sans", 15))

def FIFO():
    pageAddressing = []
    processList = []
    capacity = int(frameSize.get())
    s = []
    pivot = 0
    pageFaults = 0

    for i in range(10):
        rand = randint(0, 7)
        processList.insert(i, rand)

    frame = tk.Frame(
        bg="grey",
        width=800,
        height=400
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
        if len(s) < int(capacity):
            if (x == 0):
                s.insert(pivot, i)
                pivot = pivot + 1
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
        width=800,
        height=400
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
                print(s)

            else:
                s.append(i)
                print(s)

            # Increment Page faults
            pageFaults += 1

        # If page is already there in
        # currentPages i.e in Main
        else:

            # Remove previous index of current page
            s.remove(i)

            # Now append it, at last index
            s.append(i)
            print(s)
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
        y = 50
        x += 30
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

root.mainloop()
