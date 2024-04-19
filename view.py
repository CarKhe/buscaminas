import tkinter as tk
from celda_new import Celda
import time

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

        value = [[0,6,5,4,5,6,7,4],[0,6,5,4,5,6,7,4],[0,6,5,4,5,6,7,4],[0,6,5,4,5,6,7,4],[0,6,5,4,5,6,7,4]]
        x_pos = 10
        y_pos = 70 
        start_time = time.time()
        for x in range(5):
            for y in range(6):
                Celda(self.root,(x_pos+(50*x)),(y_pos+(50*y)),value[x][y])    
        print("--- %s seconds ---" % (time.time() - start_time)) 

        self.root.mainloop()


Game()
