from tkinter import *

import time

win = Tk()                                                                      #Creates Game window
win.title("Tic-Tac-Toe")
win.geometry("450x400")                                                         
canvas = Canvas(win,height=300,width=300, bg="grey")                            #Canvas for creating shapes



def equals(a, b, c):                                                            #Check for a win
        if a==b and b==c:
            return True                                                         
        return False

class TicTacToe:

    def __init__(self):                                                         #List to store the State of the Board
        self.board = [
                ['0','1','2'],
                ['3','4','5'],
                ['6','7','8']
            ]
        self.turns = 0

    def checkWinner(self):
        for i in range(3):
            if equals(self.board[i][0], self.board[i][1], self.board[i][2]):        #Row Check
                return self.board[i][0]

        for i in range(3):
            if equals(self.board[0][i], self.board[1][i], self.board[2][i]):        #Column Check
                return self.board[0][i]

        if equals(self.board[0][0], self.board[1][1], self.board[2][2]):
            return self.board[0][0]
        elif equals(self.board[2][0], self.board[1][1], self.board[0][2]):           #Diagonal Check
            return self.board[2][0]
        
        return ''
    
    def draw_X(self, button):                                                       #Drawing 'X' using create_line()
        if button == 5:
            l1 = canvas.create_line(0,0,100,100)
            l2 = canvas.create_line(100,0,0,100)
            self.board[0][0] = 'X'
        if button == 6:
            l1 = canvas.create_line(100,0,200,100)
            l2 = canvas.create_line(200,0,100,100)
            self.board[0][1] = 'X'
        if button == 7:
            l1 = canvas.create_line(200,0,300,100)
            l2 = canvas.create_line(300,0,200,100)
            self.board[0][2] = 'X'
        if button == 8:
            l1 = canvas.create_line(0,100,100,200)
            l2 = canvas.create_line(100,100,0,200)
            self.board[1][0] = 'X'
        if button == 9:
            l1 = canvas.create_line(100,100,200,200)
            l2 = canvas.create_line(200,100,100,200)
            self.board[1][1] = 'X'
        if button == 10:
            l1 = canvas.create_line(200,100,300,200)
            l2 = canvas.create_line(300,100,200,200)
            self.board[1][2] = 'X'
        if button == 11:
            l1 = canvas.create_line(0,200,100,300)
            l2 = canvas.create_line(100,200,0,300)
            self.board[2][0] = 'X'
        if button == 12:
            l1 = canvas.create_line(100,200,200,300)
            l2 = canvas.create_line(200,200,100,300)
            self.board[2][1] = 'X'
        if button == 13:
            l1 = canvas.create_line(200,200,300,300)
            l2 = canvas.create_line(300,200,200,300)
            self.board[2][2] = 'X'


    def draw_O(self, button):                                                           #Drawing 'O' using create_oval()
        if button == 5:
            l1 = canvas.create_oval(0,0,100,100)
            self.board[0][0] = 'O'
        if button == 6:
            l1 = canvas.create_oval(100,0,200,100)
            self.board[0][1] = 'O'
        if button == 7:
            l1 = canvas.create_oval(200,0,300,100)
            self.board[0][2] = 'O'
        if button == 8:
            l1 = canvas.create_oval(0,100,100,200)
            self.board[1][0] = 'O'
        if button == 9:
            l1 = canvas.create_oval(100,100,200,200)
            self.board[1][1] = 'O'
        if button == 10:
            l1 = canvas.create_oval(200,100,300,200)
            self.board[1][2] = 'O'
        if button == 11:
            l1 = canvas.create_oval(0,200,100,300)
            self.board[2][0] = 'O'
        if button == 12:
            l1 = canvas.create_oval(100,200,200,300)
            self.board[2][1] = 'O'
        if button == 13:
            l1 = canvas.create_oval(200,200,300,300)
            self.board[2][2] = 'O'
    
    
    def Play(self, button):                                                         #switch X and O turns
        if self.turns<9:
            if self.turns%2 == 0:
                self.draw_X(button)
            else:
                self.draw_O(button)
            self.turns+=1
        canvas.tag_unbind(button, "<Button-1>")                                     #Unbinding the button/cell which is Clicked already
        winner = self.checkWinner()
        
        if winner == 'X':
            win_label_x = Label(win, text="Winner : X", font="sans-serif 20 bold", bg="yellow", width=13, height=3).place(x=120, y=320)
            time.sleep(0.5)
            game_done = True
                
        elif winner == 'O':
            win_label_o = Label(win, text="Winner : O", font="sans-serif 20 bold", bg="green", width=13, height=3).place(x=120, y=320)
            time.sleep(0.5)
            game_done = True

        elif winner == '' and self.turns>8:
            win_label_tie = Label(win, text="Its a TIE", font="sans-serif 20 bold", bg="brown", width=13, height=3).place(x=120, y=320)
            time.sleep(0.5)
            game_done = True

        else:
            game_done = False
        
        if game_done:
            Game1 = TicTacToe()
    def Board(self):                                                                #Board SetUp
        l1 = canvas.create_line(0, 100, 300, 100)
        l2 = canvas.create_line(0, 200, 300, 200)
                                                                                    #Grids
        l3 = canvas.create_line(100, 0, 100, 300)
        l3 = canvas.create_line(200, 0, 200, 300)

        canvas.pack()

        button1 = canvas.create_rectangle(0, 0, 100, 100, fill="grey40", outline="grey60")   
        button2 = canvas.create_rectangle(100, 0, 200, 100, fill="grey40", outline="grey60") 
        button3 = canvas.create_rectangle(200, 0, 300, 100, fill="grey40", outline="grey60")
        
        button4 = canvas.create_rectangle(0, 100, 100, 200, fill="grey40", outline="grey60")
        button5 = canvas.create_rectangle(100, 100, 200, 200, fill="grey40", outline="grey60")              #each button acts as a cell
        button6 = canvas.create_rectangle(200, 100, 300, 200, fill="grey40", outline="grey60")
        
        button7 = canvas.create_rectangle(0, 200, 100, 300, fill="grey40", outline="grey60")
        button8 = canvas.create_rectangle(100, 200, 200, 300, fill="grey40", outline="grey60")
        button9 = canvas.create_rectangle(200, 200, 300, 300, fill="grey40", outline="grey60")

        canvas.tag_bind(button1, "<Button-1>", lambda state: self.Play(button1))
        canvas.tag_bind(button2, "<Button-1>", lambda state: self.Play(button2))
        canvas.tag_bind(button3, "<Button-1>", lambda state: self.Play(button3))
        canvas.tag_bind(button4, "<Button-1>", lambda state: self.Play(button4))                           
        canvas.tag_bind(button5, "<Button-1>", lambda state: self.Play(button5))
        canvas.tag_bind(button6, "<Button-1>", lambda state: self.Play(button6))
        canvas.tag_bind(button7, "<Button-1>", lambda state: self.Play(button7))
        canvas.tag_bind(button8, "<Button-1>", lambda state: self.Play(button8))
        canvas.tag_bind(button9, "<Button-1>", lambda state: self.Play(button9))

Game = TicTacToe()                                                                                     #Class Object
button_start = Button(win, text = "Play", command = Game.Board, width=13, height=3, bg="yellow").place(x=175, y=320)  #Onclick calls Board() of class

win.mainloop()