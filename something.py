import sys
import os

board = list("♖♘♗♔♕♗♘♖" + "♙"*8 + " "*32 + "♟"*8 + "♜♞♝♚♛♝♞♜")

def draw_board():
    print("  a b c d e f g h")
    print(" ---------------")
    for i in range(8):
        print(8-i, "|", end="")
        for j in range(8):
            print(board[i*8 + j], end="|")
        print("", 8-i)
        print(" ---------------")
    print("  a b c d e f g h")

def move_piece(start, end):
    start_index = (8 - int(start[1])) * 8 + ord(start[0]) - 97
    end_index = (8 - int(end[1])) * 8 + ord(end[0]) - 97
    board[end_index] = board[start_index]
    board[start_index] = " "

while True:
    os.system("clear")
    draw_board()
    start, end = input("Enter move (eg. 'e2 e4'): ").split()
    move_piece(start, end)