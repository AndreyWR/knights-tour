import tkinter as tk
import telainicial as ti

def main():
    # Definition of the highest priority widget, instantiating the screen and running the program
    toplevel = tk.Tk()
    tela = ti.HomeScreen(toplevel)
    toplevel.mainloop()


if __name__ == "__main__":
    main()
