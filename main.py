import tkinter as tk
import homescreen as hs


def main():
    # Definition of the highest priority widget, instantiating the screen and running the program
    toplevel = tk.Tk()
    screen = hs.HomeScreen(toplevel)
    toplevel.mainloop()


if __name__ == "__main__":
    main()
