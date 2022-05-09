import state


def solve(size):
    # solves the (size) queens problem
    b = state.rndBoard(size)
    n = state.threats(b)
    i = 1
    sum = 0
    while n > 0:
        x = state.improve(b)
        if x == n:
            print("try again")
            #i = 1
            b = state.rndBoard(size)
            n = state.threats(b)
        else:
            n = x
        print("try:", i)
        i += 1
        sum += 1

    state.printBoard(b)
    print("\nsum tries:", sum)


solve(10)
