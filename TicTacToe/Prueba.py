from tkinter import *
from TicTacToe import Board, GUI

raiz = Tk()

frame = Frame(raiz, width="500", height="300")
frame.pack()

lblplayer1=Label(frame, text="player1:")
lblplayer1.grid(row=0, column=0, sticky="e", pady="10", padx="10")

lblplayer2=Label(frame, text="player2:")
lblplayer2.grid(row=1, column=0, pady="10", padx="10")

txtplayer1=Entry(frame)
txtplayer1.grid(row=0, column=1)

txtplayer2=Entry(frame)
txtplayer2.grid(row=1, column=1)

raiz.mainloop()