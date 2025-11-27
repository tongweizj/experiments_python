from random import randrange
global board

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    # 该函数接受一个参数，其中包含电路板的当前状态
    # 并将其打印到控制台。
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |\n|", end='')
        for col in row:
           print(f"   {col}   |", end='')
        print("\n|       |       |       |")
        print("+-------+-------+-------+")

    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    # 该函数接收棋盘的当前状态，询问用户下一步的走法，
    # 检查输入，并根据用户的决定更新棋盘。
    # 检查是否空位
    empty = make_list_of_free_fields(board)
    check_input = False
    while check_input== False:
        movie_to = int(input("Enter your move: "))

        # 检查输入是否合法 0-8
        if movie_to < 0 or movie_to > 8:
            continue
        # 变换成坐标
        row = int(movie_to // 3)
        col = movie_to % 3

        # print(empty)
        if (row, col) in empty:
            board[row][col] = "o"
            check_input = True
        else:
            continue


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    # 该函数遍历棋盘并构建一个包含所有空闲方格的列表；
    # 该列表由元组组成，每个元组包含行号和列号。
    empty_board = []
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] in [0,1,2,3,4,5,6,7,8]:
                empty_board.append((row,col))
    return empty_board

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # 0 false
    # 1 win
    # 2 draw
    empty = make_list_of_free_fields(board)
    if len(empty) == 0:
            print("We are draw!")
            return 2
    # row
    for row in range(0,3):
        if (board[row][0] == sign) and (board[row][1] == sign) and (board[row][2] == sign):
            print("You Won!")
            return 1
    # col
    for col in range(0,3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            print("You Won!")
            return 1
    # 斜线
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        print("You Won!")
        return 1
    if board[0][2] == sign and board[1][2] == sign and board[2][0] == sign:
        print("You Won!")
        return 1
    return 0

def draw_move(board):
    # The function draws the computer's move and updates the board.
    # 该函数绘制计算机的走法并更新棋盘。
    empty = make_list_of_free_fields(board)
    print(empty)
    if len(empty) == 1:
        board[empty[0][0]][empty[0][1]] = "x"
        return

    for i in range(10):
        movie_to = randrange(8)
        row = int(movie_to // 3)
        col = movie_to % 3

        if (row, col) in empty:
            print(movie_to)
            board[row][col] = "x"
            break
        else:
            continue



def main():
    board = [
        [0,1,2],
        [3,"x",5],
        [6,7,8]
    ]
    display_board(board)
    is_over = False
    while is_over == False:
        # 1. 输入
        enter_move(board)
        # 2. 显示棋盘
        display_board(board)
        # 4. 检查是否赢了
        if victory_for(board, "o") !=0:
            break
        # 5. 计算机走下一步
        draw_move(board)
        display_board(board)
        # 6. 检查是否赢了
        if victory_for(board, "x") == 1:
            print("You Lost!")
            is_over = True
        elif victory_for(board, "x") == 2:
            is_over = True


if __name__ == "__main__":
    main()