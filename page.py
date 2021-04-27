import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)
H = 500
W = 800


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,width=W,height=H)


        greet = tk.Label(
            text="Virtual Memory Simulation"
        )
        greet.place(x=150,y=0)
        greet.config(font=("Open Sans", 30))
        inputFrameText = tk.Label(
            text="Input Frame Size",
        )
        inputFrameText.place(x=100,y=200)
        inputFrameText.config(font=("Open Sans", 20))

        inputFrame = tk.Entry()
        inputFrame.place(x=400,y=200)
        inputFrame.config(font=("Open Sans", 20))



        def testButton():
            if(inputFrame.get() == ""):
                print("WTF")
            else:
                newLabel = tk.Label(
                    text=inputFrame.get()
                )
                inputFrame.pack_forget()
                inputFrameText.pack_forget()
                print(inputFrame.get())

        runButton = tk.Button(
            text="RUN",
            height=2,
            width=10,
            command=lambda: controller.show_frame(Page1)
        )
        runButton.place(x=350, y=270)
        runButton.config(font=("Open Sans", 10))

        # # label of frame Layout 2
        # label = ttk.Label(self, text="Startpage", font=LARGEFONT)
        #
        # # putting the grid in its place by using
        # # grid
        # label.grid(row=0, column=4, padx=10, pady=10)
        #
        # button1 = ttk.Button(self, text="Page 1",
        #                      command=lambda: controller.show_frame(Page1))
        #
        # # putting the button in its place by
        # # using grid
        # button1.grid(row=1, column=1, padx=10, pady=10)
        #
        # ## button to show frame 2 with text layout2
        # button2 = ttk.Button(self, text="Page 2",
        #                      command=lambda: controller.show_frame(Page2))
        #
        # # putting the button in its place by
        # # using grid
        # button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,width=W,height=H)
        for widgets in tk.Frame.winfo_children(self):
            widgets.destroy()
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
