

board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j != 2:
                print(str(board[i][j]) + " | ", end="")
            else:
                print(board[i][j], end="")
        if i != 2:
            print("")
            print("---------")
    print("")
