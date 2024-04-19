import tkinter as tk
from celda import Celda

MINES = 3
class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper")
        self.root.iconbitmap("assets/Minesweeper_1992.ico")
        self.root.geometry("280x380+1100+200")

        self.planted_mines = tk.Frame(self.root,bg="#AFA8A8")
        self.planted_mines.place(x=10,y=10,width=90,height=50)

        self.mines_remain = tk.Label(self.planted_mines,font=('digital-7',30,'bold'),
            background='black',foreground='red',text=MINES)
        self.mines_remain.pack()

        self.restart_button = tk.Button(self.root,text="(ツ)")
        self.restart_button.place(x=110,y=10,height=50,width=50)

        self.time = tk.Frame(self.root,bg="#AFA8A8")
        self.time.place(x=170,y=10,width=90,height=50)

        self.lbl_time = tk.Label(self.time,font=('digital-7',30,'bold'),
            background='black',foreground='red')
        self.lbl_time.pack()

        self.board = tk.Frame(self.root,bg="#AFA8A8")
        self.board.place(x=10,y=70,height=300,width=250)

        Celda(self.root,10,70,6)
        Celda(self.root,10,120,2)
        Celda(self.root,10,170,0)
        Celda(self.root,10,220,9)
        Celda(self.root,10,270,0)
        Celda(self.root,10,320,9)
        Celda(self.root,60,70,9)
        Celda(self.root,60,120,1)
        Celda(self.root,60,170,0)
        Celda(self.root,60,220,3)
        Celda(self.root,60,270,0)
        Celda(self.root,60,320,9)

        
        

        self.root.mainloop()

    
        


Game()