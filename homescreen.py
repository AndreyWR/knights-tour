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

        # Defining the canvas that will store the squares on the boards
        self.canvas = Canvas(toplevel, width=300, height=10)
        self.canvas.pack()
        self.tab = None

        # Creating a frame with tk and placing it on toplevel
        self.frame1 = Frame(toplevel)
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

        self.frame7 = Frame(toplevel) # Creating a frame with tk and placing it on toplevel
        self.frame7.pack()

        vlist = ["Depth", "A*"]
        self.horse = PhotoImage(file='horse2.png')

        Label(self.frame1, text='Nº Lines:', width=10).pack(side=LEFT)
        self.line = Entry(self.frame1, width=6)
        self.line.pack(side=LEFT)

        Label(self.frame2, text='Nº Columns:', width=10).pack(side=LEFT)
        self.column = Entry(self.frame2, width=6)
        self.column.pack(side=LEFT)

        Label(self.frame3, text='Pos X:', width=10).pack(side=LEFT)
        self.posx = Entry(self.frame3, width=6)
        self.posx.pack(side=LEFT)

        Label(self.frame4, text='Pos Y:', width=10).pack(side=LEFT)
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

    def createboard(self, k):
        if self.tab is not None:
            self.tab.cleanboard()

        self.tab = bd.Board(self.toplevel, lines = int(self.line.get()), columns = int(self.column.get()), size = 32)
        self.tab.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        #horse = PhotoImage(file='horse2.png')
        self.toplevel.horse = self.horse
        self.tab.addpiece("horse", self.horse, int(k[0]), int(k[1]))

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
        output = ''

        if self.combo.get() == "Depth":
            start = time.time()
            g = searchdepth.find_solution_for()
            end = time.time()
            output = 'Time: ' + str((end - start)) + '\nNumber of vertices in the graph: ' + str(len(g))
            Label(self.frame7, text=output, width=100).pack(side=LEFT, expand=True)

        elif self.combo.get() == "A*":
            start = time.time()
            g = searchastar.find_solution_for(searchastar.warnsdorffs_heuristic)
            end = time.time()
            output = 'Time: ' + str((end - start)) + '\nNumber of vertices in the graph: ' + str(len(g))
            Label(self.frame7, text=output, width=10).pack(side=LEFT, expand=True)

        else:
            messagebox.showerror("Error", "Select one of the valid methods")

        k=[]
        c=0
        for L in g:
            for i in L:
                k.append(i)
            if c == 0:
                self.createboard(k)
            else:
                # self.tab.addpiece("horse", self.horse, int(k[0]), int(k[1]))
                self.tab.putpiece("horse", int(k[0]), int(k[1]))
            c += 1
            time.sleep(2)
            k=[]

    def Close(self): self.toplevel.destroy()
