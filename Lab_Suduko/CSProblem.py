# SUDOKU
import math
import copy

# import CSPSolver
# board - The variables' value are in a list of the (N*N)*(N*N) board cells
#            (a vector representing a mat.).
# an empty cell contains 0.
#
# d - The domains are a list of lists - the domain of every var.
#
# The state is a list of 2 lists: the vars. and the domains.
N = 0


def create(fpath="sudoku.txt"):
    global N
    board = read_board_from_file(fpath)
    N = int(len(board) ** 0.25)

    # TODO- you need to add to each parameter the domain which it can get
    # second space should have a list of all of the domains which it can have
    # note- 0 is a list of lists(with every values domain)
    domains = []

    for i in range(len(board)):
        # check that place is empty
        if board[i] == 0:
            # will go over the row and remove form the list all the numbers which are not in the domin
            # Create a list with all the numbers in the domain
            domain = [i for i in range(1, 10)]

            # Go over the rows and check the domain
            domain = check_row(board, domain, i)
            # Go over the column and check the domain
            domain = check_column(board, domain, i)

            # Go over the box and check the domain
            domain = check_box(board, domain, i)
            # change the domain
            domains.append(copy.deepcopy(domain))
        else:
            # set the domain to an empty list
            domain = []
            domains.append(copy.deepcopy(domain))

    for row in range(N * N):
        print(domains[row+27])
    # puts the domains in the second slot
    problem = [board, domains]
    return problem


def check_row(board, list, place):
    rowSize = N * N
    # which row is it in times 9
    startOfRow = int(place / rowSize) * rowSize
    for i in range(rowSize):
        # if it is not zero will remove it from the list
        number = board[startOfRow + i]
        if number != 0 and number in list:
            list.remove(number)
    return list


# will go over the colum and remove form the list all the numbers which are not in the domain


def check_column(board, list, place):
    columnSize = N * N
    # which column are we checking
    columnNumber = place % columnSize
    for i in range(columnSize):
        # if it is not zero will remove it from the list
        number = board[columnNumber + columnSize * i]
        if number != 0 and number in list:
            list.remove(number)
    return list


# will check the box and remove numbers from it domain if it can't be in its domain


def check_box(board, list, place):
    boxSize = N * N
    # we will go over the box with two for
    # row = int(place / boxSize)
    # column= place % boxSize

    # gets the first row in the box
    # firstRowInBox= row - row%N

    # gets the first column in the box
    # firstColumnInBox= column - column%N

    # firstSpot=  firstColumnInBox + firstRowInBox*boxSize
    firstSpot = first_spot_in_box(place)

    # will go over etch row
    for i in range(N):
        # will go over etch spot in the row
        for j in range(N):
            location = firstSpot + boxSize * i + j
            number = board[location]
            if number != 0 and number in list:
                list.remove(number)

    return list


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
    # gets to parameters v1, v2, and ask if we added them would there be a problem
    # returns a BOOLEAN
    # meaning can you put those two values their
    # will check if the two locations are in the same line or row or box
    # check if they are the same value
    if v1 == v2 or x1 != x2:
        return True
    # then the numbers are the same
    # will check if the two locations are in the same line or row or box
    if v1 % 9 == v2 % 9 or v1 // 9 == v2 // 9 or first_spot_in_box(v1) == first_spot_in_box(v2):
        return False

    return True


def is_consistent(pr, v1,v2, x1, x2):
    if x1 != x2:
        return True
    if v1 % 9 == v2 % 9 or \
            v1 // 9 == v2 // 9 or \
            check_box(v1, v2):
        return False

    return True


def check_box(v1, v2):
    box1 = v1 - v1 % 9 % 3 - v1//9
    box2 = v2 - v2 % 9 % 3 - v2//9

    return box1 == box2


# Gets - a location on the board
# Returns - the first location in the box(top,left)
def first_spot_in_box(place):
    boxSize = N * N
    # find the row and column of the location
    row = int(place / boxSize)
    column = place % boxSize

    # gets the first row in the box
    firstRowInBox = row - row % N

    # gets the first column in the box
    firstColumnInBox = column - column % N

    return firstColumnInBox + firstRowInBox * boxSize


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
