import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Start Page").pack()
        tk.Button(self, text="Go to Page One", command=lambda: parent.show_frame(PageOne)).pack()


class PageOne(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Page One").pack()
        tk.Button(self, text="Back to Start", command=lambda: parent.show_frame(StartPage)).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
