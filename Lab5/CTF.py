import hashlib

CTF_hash = "9372187d2de232bb199bbf2be2532a6d"
a_hash = "d9fa8363e7dfa60b4c67ad5c3beb5085"
salt1 = "7993"
salt = "4271"
words = open("american-english-large.txt")

for line in words:
    word = line.strip("\n")
    temp_hash = hashlib.md5(word.encode() + salt1.encode()).hexdigest()
    if temp_hash == a_hash:  # if we find the original word
        print(word)

def printState(s):
    # Prints the board. The empty cells are printed as numbers = the cells name(for input)
    # If the game ended prints who won.
    print(f"The Human score is: {s[2]}")
    print(f"The Computer score is: {s[3]}")
    print("The board is:")
    # print the culoms

    # this is what we try to get
    print("+---------------" * SIZE + "+")
    for row in s[0]:
        s = "|"
        for column in row:
            s += f"{column}" + "|"
        print(s)
        print("+---------------"*SIZE + "+")
    # this is what we already have
    for row in range(len(s[0])):
        print("\n" + " --------" * SIZE + "\n|", end="")
        # print the row
        for c in range(len(s[0][0])):
            temp = s[0][row][c]
            # if we are in the row or coulom that was last palyed then we will add numbers to it
            # note- maybe a problem here if we printed the wrong row
            if s[1] == COMPUTER and c == s[4]:
                print(f"({row}) {temp} | ", end="")
            elif s[1] == HUMAN and row == s[4]:
                print(f"({c}) {temp} | ", end="")
            else:
                print(f"  {temp}   | ", end="")
    print("\n" + " --------" * SIZE + "\n", end="")
    if isFinished(s) == True:
        if value(s) > 0:
            print("Ha ha ha I won!")
        elif value(s) < 0:
            print("Human beat mushine!")
        elif value(s) == TIE:
            print("It's a TIE")

            print("\n" + "\033[1;33m --------" * SIZE + "\n|\033[1;0m", end="")