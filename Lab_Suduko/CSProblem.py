# SUDOKU
import math

# import CSPSolver
# board - The variables' value are in a list of the (N*N)*(N*N) board cells
#            (a vector representing a mat.).
# an empty cell contains 0.
#
# d - The domains are a list of lists - the domain of every var.
#
# The state is a list of 2 lists: the vars, and the domains.
N = 0


def create(fpath="sudoku.txt"):
    global N
    board = read_board_from_file(fpath)
    N = int(len(board) ** 0.25)
    # your code here
    domains = []

    problem = [board, 0]
    return problem


def read_board_from_file(fpath):
    f = open(fpath, "r")
    board = []
    s = f.readline()
    while s != "":
        for i in s.split():
            board += [int(i)]
        s = f.readline()
    f.close()
    return board


def domain(problem, v):
    # Returns the domain of v
    return problem[1][v][:]


def domain_size(problem, v):
    # Returns the domain size of v
    return len(problem[1][v])


def assign_val(problem, v, x):
    # Assigns x in var. v
    problem[0][v] = x


def get_val(problem, v):
    # Returns the val. of v
    return problem[0][v]


def erase_from_domain(problem, v, x):
    # Erases x from the domain of v
    problem[1][v].remove(x)


def get_list_of_free_vars(problem):
    # Returns a list of vars. that were not assigned a val.
    l = []
    for i in range(len(problem[0])):
        if problem[0][i] == 0:
            l += [i]
    return l


def is_solved(problem):
    # Returns True iff the problem is solved
    for i in range(len(problem[0])):
        if problem[0][i] == 0:
            return False
    return True


def is_consistent(problem, v1, v2, x1, x2):
    # Returns True if v1=x1 and v2=x2 is consistent with all constraints
    # your code here
    # מקבל שני מקומות, ובודק האם ההצבה תקינה ביחס לשני המספרים האלו בלבד

    return 0


def list_of_influenced_vars(problem, v):
    # Returns a list of free vars. whose domain will be
    # influenced by assigning a val. to v
    r = list(range(N ** 4))
    r.remove(v)
    l = []
    for i in r:
        if problem[0][i] == 0 and not is_consistent(problem, v, i, 1, 1):
            l += [i]
    return l


def present(problem):
    for i in range(len(problem[0])):
        if i % (N * N) == 0:
            print()
        x = str(problem[0][i])
        pad = (math.ceil(math.log(N * N, 10)) - len(x))
        print(pad * " ", x, end="")
    print()
