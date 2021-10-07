import tkinter as tk
import telainicial as ti

def main():
    # Definicao do widget de maior prioridade, instanciando a tela e executando o programa
    toplevel = tk.Tk()
    tela = ti.TelaInicial(toplevel)
    toplevel.mainloop()


if __name__ == "__main__":
    main()
