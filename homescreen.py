from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import profundidade as pf
from astar import *
import time

class TelaInicial:
    def __init__(self,toplevel):
        self.toplevel = toplevel
        self.toplevel.title('Informações do tabuleiro')

        self.canvas = Canvas(toplevel, width=300, height=10) # Definindo o canvas que vai guardar os quadrados dos tabuleiros
        self.canvas.pack()
        self.tab = None

        self.frame1 = Frame(toplevel) # Criando um frame com tk e colocando no toplevel
        self.frame1.pack()

        self.frame2 = Frame(toplevel) # Criando um frame com tk e colocando no toplevel
        self.frame2.pack()

        self.frame3 = Frame(toplevel) # Criando um frame com tk e colocando no toplevel
        self.frame3.pack()

        self.frame4 = Frame(toplevel)
        self.frame4.pack()

        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        self.frame6 = Frame(toplevel)
        self.frame6.pack()

        vlist = ["Depth", "A*"]

        Label(self.frame1, text='Nº Lines:', width=8).pack(side=LEFT)
        self.linha = Entry(self.frame1, width=6)
        self.linha.pack(side=LEFT)

        Label(self.frame2, text='Nº Columns:', width=8).pack(side=LEFT)
        self.coluna = Entry(self.frame2, width=6)
        self.coluna.pack(side=LEFT)

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

        # Botão Executar
        self.bexec = Button(self.frame6, text='Run', command=self.retornavalor)
        self.bexec['padx'],self.bexec['pady'] = 10, 5
        self.bexec.pack(side=LEFT)

        # Botão Fechar
        self.bfechar = Button(self.frame6, text='Close', command=self.fechar)
        self.bfechar['padx'],self.bfechar['pady'] = 10, 5
        self.bfechar.pack(side=LEFT)

    def retornavalor(self):

        try:
            val = int(self.linha.get())
        except ValueError:
            messagebox.showerror("Error", "Enter an integer value")
            return

        try:
            val = int(self.coluna.get())
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

        buscaprof = pf.profundidade(int(self.posx.get()), int(self.posy.get()), int(self.linha.get()))
        buscaastar = aestrela(int(self.posx.get()), int(self.posy.get()), int(self.linha.get()))

        if self.combo.get() == "Depth":
            start = time.time()
            g = buscaprof.find_solution_for()
            end = time.time()
            print('Time: {}'.format(end - start))
            print('Graph: {}'.format(g))
            print('Number of vertices in the graph: {}'.format(len(g)))


        elif self.combo.get() == "A*":
            start = time.time()
            g = buscaastar.find_solution_for(buscaastar.warnsdorffs_heuristic)
            end = time.time()
            print('Time: {}'.format(end - start))
            print('Graph: {}'.format(g))
            print('Number of vertices in the graph: {}'.format(len(g)))

        else:
            messagebox.showerror("Error", "Select one of the valid methods")

    def fechar(self): self.toplevel.destroy()
