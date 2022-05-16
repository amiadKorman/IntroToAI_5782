import copy
import random

'''
Authors: Binyamin Rosner & Amiad Korman
'''

VIC = 10 ** 20  # The value of a winning board (for max)
LOSS = -VIC  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 5  # The length of a winning sequence
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human cells on the board
VALUE = 10
EMPTY = "Empty"
'''
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. Empty cells = "Empty".
1. Who's turn is it: HUMAN or COMPUTER
2. HUMAN score.
3. Computer score.
4. In which row/column we are now(rows for Human, columns for COMPUTER).
'''


def create():
    # Returns an empty board. The human plays first.
    human_score = computer_score = 0
    board = []
    for i in range(SIZE):
        row_of = []
        for j in range(SIZE):
            row_of.append(random.randint(-VALUE, VALUE))
        board.append(row_of)
    return [board, HUMAN, human_score, computer_score, int(SIZE / 2)]


def value(s):
    # Returns the heuristic value of s
    # And that actually computer_score - human_score
    return s[3] - s[2]


def printState(s):
    # Prints the board. The empty cells are printed blanked
    # If the game ended prints who won.
    # print the columns
    for r in range(len(s[0])):
        print("\n" + "\033[1;33m --------" * SIZE + "\n|\033[1;0m", end="")
        # print the rows
        for c in range(len(s[0][0])):
            temp = s[0][r][c]
            # if we are in empty cell, we will print nothing
            if temp == EMPTY:
                print("        \033[1;33m|\033[1;0m", end="")
            # if we are in the row or column that was last played then we will add numbers to it
            elif s[1] == HUMAN and r == s[4]:
                print(f"{temp:>3} \033[1;32m({c})\033[1;33m |\033[1;0m", end="")
            else:
                print(f"{temp:^8}\033[1;33m|\033[1;0m", end="")
    print("\n" + "\033[1;33m --------\033[1;0m" * SIZE + "\n", end="")
    # print the current score of both comp. and huma.
    print(f"The Human score is: {s[2]}")
    print(f"The Computer score is: {s[3]}")
    # if the game is over, checks the score
    if isFinished(s):
        print("\nThe game is over!")
        if value(s) > 0:
            print("\33[1;31mHa ha ha I won!\033[1;0m")
        elif value(s) < 0:
            print("\033[1;32mHuman beat machine!")
        elif value(s) == TIE:
            print("It's a TIE")


def isFinished(s):
    # if it is the humans turn will check if the
    if isHumTurn(s):
        for c in range(SIZE):
            if s[0][s[4]][c] != EMPTY:
                return False
    # if it's the computers turn will go over his column
    else:
        for r in range(SIZE):
            if s[0][r][s[4]] != EMPTY:
                return False
    # Returns True iff the game ended
    return True


def isHumTurn(s):
    # Returns True iff it the human's turn to play
    return s[1] == HUMAN


def whoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1- computer / anything else- you. : ")) == 1:
        s[1] = COMPUTER
    else:
        s[1] = HUMAN


def makeMove(s, r, c):
    # change the score, and updates the Matrix, changes the row or column
    if isHumTurn(s):
        s[2] = s[2] + s[0][r][c]
        s[0][r][c] = EMPTY
        s[4] = c
    else:
        s[3] = s[3] + s[0][r][c]
        s[0][r][c] = EMPTY
        s[4] = r
    # Switch turns
    s[1] = COMPUTER + HUMAN - s[1]


def inputMove(s):
    # Reads, enforces legality and executes the user's move.
    printState(s)
    flag = True
    while flag:
        row = input("Enter your next move: ")
        # check that the input is valid
        if row.isdecimal() and 0 <= int(row) < SIZE and s[0][s[4]][int(row)] != EMPTY:
            flag = False
            makeMove(s, s[4], int(row))
        else:
            print("Illegal move.")


def getNext(s):
    # returns a list of the next states of s
    ns = []
    if isHumTurn(s):
        # if it is the human turn, do all the possibles moves for the human
        for c in range(SIZE):
            if s[0][s[4]][c] != EMPTY:
                tmp = copy.deepcopy(s)
                makeMove(tmp, s[4], c)
                ns += [tmp]
        # sort the moves from best to worst(for the computer), using the heuristic value
        ns.sort(key=value)
    else:
        # if it is the computer turn, do all the possibles moves for the computer
        for r in range(SIZE):
            if s[0][r][s[4]] != EMPTY:
                tmp = copy.deepcopy(s)
                makeMove(tmp, r, s[4])
                ns += [tmp]
        # sort the moves from best to worst(for the computer), using the heuristic value
        ns.sort(key=value, reverse=True)
    return ns
