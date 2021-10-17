board=[

    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]

]

def print_board(board1):
    for i in range(len(board1)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - ")

        for j in range(len(board1)):
            if j % 3 == 0 and j !=0:
                print("| ",end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ",end='')


def find_empty(board1):
    #search for unfilled box
    for i in range(len(board1)):
        for j in range(len(board1)):
            if board1[i][j] == 0:
                return (i,j)

    return None

def valid(board1,number,position):
    #checks row
    for i in range(len(board1)):
        if board1[position[0]][i] == number and position[1] != i:
            return False

    #checks column
    for j in range(len(board1)):
        if board1[j][position[1]] == number and position[0] != j:
            return False

    #checks box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_x*3,box_y*3+3):
        for j in range(box_y * 3, box_x * 3 + 3):
            if board1[i][j] == number and (i,j) != position:
                 return False

    return True

def solve(board1):
    find = find_empty(board1)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(board1,i,(row,col)):
            board1[row][col]=i

            if solve(board1):
                return True


            board1[row][col]=0
    return False

print_board(board)

solve(board)

print("=====================")

print_board(board)