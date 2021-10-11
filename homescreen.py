from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import depthfirstsearch as dpth
from astar import *
import board as bd
import time

class HomeScreen:
    def __init__(self,toplevel):
        self.toplevel = toplevel
        self.toplevel.title('Board information')

        self.canvas = Canvas(toplevel, width=300, height=10) # Defining the canvas that will store the squares on the boards
        self.canvas.pack()
        self.tab = None

        self.frame1 = Frame(toplevel) # Creating a frame with tk and placing it on toplevel
        self.frame1.pack()

        self.frame2 = Frame(toplevel) # Creating a frame with tk and placing it on toplevel
        self.frame2.pack()

        self.frame3 = Frame(toplevel) # Creating a frame with tk and placing it on toplevel
        self.frame3.pack()

        self.frame4 = Frame(toplevel) # Creating a frame with tk and placing it on toplevel
        self.frame4.pack()

        self.frame5 = Frame(toplevel) # Creating a frame with tk and placing it on toplevel
        self.frame5.pack()

        self.frame6 = Frame(toplevel) # Creating a frame with tk and placing it on toplevel
        self.frame6.pack()

        vlist = ["Depth", "A*"]

        Label(self.frame1, text='Nº Lines:', width=8).pack(side=LEFT)
        self.line = Entry(self.frame1, width=6)
        self.line.pack(side=LEFT)

        Label(self.frame2, text='Nº Columns:', width=8).pack(side=LEFT)
        self.column = Entry(self.frame2, width=6)
        self.column.pack(side=LEFT)

        Label(self.frame3, text='Pos X:', width=8).pack(side=LEFT)
        self.posx = Entry(self.frame3, width=6)
        self.posx.pack(side=LEFT)

        Label(self.frame4, text='Pos Y:', width=8).pack(side=LEFT)
        self.posy = Entry(self.frame4, width=6)
        self.posy.pack(side=LEFT)

        # COMBO BOX
        self.combo = ttk.Combobox(self.frame5, values=vlist)
        self.combo.set("Choose an option")
        self.combo.pack(padx=5, pady=5)

        # Run Button
        self.brun = Button(self.frame6, text='Run', command=self.ReturnValue)
        self.brun['padx'],self.brun['pady'] = 10, 5
        self.brun.pack(side=LEFT)

        # Close Button
        self.bclose = Button(self.frame6, text='Close', command=self.Close)
        self.bclose['padx'],self.bclose['pady'] = 10, 5
        self.bclose.pack(side=LEFT)

        # Create Board
        self.bboard = Button(self.frame6, text='Board', command=self.createboard)
        self.bboard['padx'],self.bboard['pady'] = 10, 5
        self.bboard.pack(side=LEFT)


    def createboard(self):
        print('self.tab: {}'.format(self.tab))

        if self.tab is not None:
            self.tab.cleanboard()

        self.board = bd.Board(self.toplevel, lines = int(self.line.get()), columns = int(self.column.get()), size = 32)
        self.board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        horse = PhotoImage(file='horse2.png')
        self.toplevel.horse = horse
        self.tab.addpiece("horse", horse, int(self.posx.get()), int(self.posy.get()))


    def ReturnValue(self):

        try:
            val = int(self.line.get())
        except ValueError:
            messagebox.showerror("Error", "Enter an integer value")
            return

        try:
            val = int(self.column.get())
        except ValueError:
            messagebox.showerror("Error", "Enter an integer value")
            return

        try:
            val = int(self.posx.get())
        except ValueError:
            messagebox.showerror("Error", "Enter an integer value")
            return

        try:
            val = int(self.posy.get())
        except ValueError:
            messagebox.showerror("Error", "Enter an integer value")
            return

        searchdepth = dpth.Depth(int(self.posx.get()), int(self.posy.get()), int(self.line.get()))
        searchastar = AStar(int(self.posx.get()), int(self.posy.get()), int(self.line.get()))

        if self.combo.get() == "Depth":
            start = time.time()
            g = searchdepth.find_solution_for()
            end = time.time()
            print('Time: {}'.format(end - start))
            print('Graph: {}'.format(g))
            print('Number of vertices in the graph: {}'.format(len(g)))


        elif self.combo.get() == "A*":
            start = time.time()
            g = searchastar.find_solution_for(searchastar.warnsdorffs_heuristic)
            end = time.time()
            print('Time: {}'.format(end - start))
            print('Graph: {}'.format(g))
            print('Number of vertices in the graph: {}'.format(len(g)))

        else:
            messagebox.showerror("Error", "Select one of the valid methods")

    def Close(self): self.toplevel.destroy()
