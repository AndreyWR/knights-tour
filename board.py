import tkinter as tk

class Board(tk.Frame):
    def __init__(self, toplevel, lines, columns, size, color1="white", color2="blue"):

        self.size = size
        self.lines = lines
        self.columns = columns
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        if self.lines == '' and self.columns == '':
            return None

        canvas_width = columns * size
        canvas_height = lines * size

        self.frame = tk.Frame.__init__(self, toplevel)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.canvas.bind("<Configure>", self.refresh)


    def cleanboard(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


    def addpiece(self, name, image, line=0, column=0):
        self.canvas.create_image(0, 0, image=image, tags=(name, "piece"), anchor="c")
        self.putpiece(name, line, column)


    def putpiece(self, name, line, column):
        self.pieces[name] = (line, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (line * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)


    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.lines)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2

        for line in range(self.lines):
            color = self.color1 if color == self.color2 else self.color2

            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (line * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size

                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2

            for name in self.pieces:
                self.putpiece(name, self.pieces[name][0], self.pieces[name][1])

            self.canvas.tag_raise("piece"),
            self.canvas.tag_lower("square")
