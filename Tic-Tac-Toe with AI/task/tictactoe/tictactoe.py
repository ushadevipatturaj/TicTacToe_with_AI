from string import ascii_letters


def check_row(cells):
    result1 = ""
    result2 = ""
    for i in range(len(cells)):
        if cells[i][0] == "X" and cells[i][1] == "X" and cells[i][2] == "X":
            result1 = "X"
        elif cells[i][0] == "O" and cells[i][1] == "O" and cells[i][2] == "O":
            result2 = "O"
    if result1 == "X" and result2 == "O":
        return "XO"
    elif result1 == "X":
        return "X"
    elif result2 == "O":
        return "O"


def check_column(cells):
    result1 = ""
    result2 = ""
    for i in range(len(cells)):
        if cells[0][i] == "X" and cells[1][i] == "X" and cells[2][i] == "X":
            result1 = "X"
        elif cells[0][i] == "O" and cells[1][i] == "O" and cells[2][i] == "O":
            result2 = "O"
    if result1 == "X" and result2 == "O":
        return "XO"
    elif result1 == "X":
        return "X"
    elif result2 == "O":
        return "O"


def check_diagonal(cells):
    x_count = 0
    o_count = 0
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if i == j:
                if cells[i][j] == "X":
                    x_count += 1
                elif cells[i][j] == "O":
                    o_count += 1
    if x_count == 3 and o_count == 3:
        return "XO"
    elif o_count == 3:
        return "O"
    elif x_count == 3:
        return "X"


def check_anti_diagonal(cells):
    x_count = 0
    o_count = 0
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            x = len(cells[0]) - 1 - i
            if x == j:
                if cells[i][j] == "X":
                    x_count += 1
                elif cells[i][j] == "O":
                    o_count += 1
    if x_count == 3 and o_count == 3:
        return "XO"
    elif o_count == 3:
        return "O"
    elif x_count == 3:
        return "X"


def validate_win_scenarios(tic_tac_toe, input_cells):
    if (check_row(tic_tac_toe) == check_column(tic_tac_toe) == check_diagonal(tic_tac_toe) is None and
            check_anti_diagonal(tic_tac_toe) is None and input_cells.count("X") + input_cells.count("O") == 9):
        print("Draw")
        return True
    elif (check_row(tic_tac_toe) == check_column(tic_tac_toe) == check_diagonal(tic_tac_toe) is None and
          check_anti_diagonal(tic_tac_toe) is None and input_cells.count("X") + input_cells.count("O") != 9
          and (input_cells.count("X") == input_cells.count("O") or input_cells.count("X") == input_cells.count(
                "O") + 1)):
        # print("Game not finished")
        return False
    elif (check_row(tic_tac_toe) == "X" or check_column(tic_tac_toe) == "X" or check_diagonal(tic_tac_toe) == "X"
          or check_anti_diagonal(tic_tac_toe) == "X"):
        print("X wins")
        return True
    elif (check_row(tic_tac_toe) == "O" or check_column(tic_tac_toe) == "O" or
          check_diagonal(tic_tac_toe) == "O" or check_anti_diagonal(tic_tac_toe) == "O"):
        print("O wins")
        return True
    elif (check_row(tic_tac_toe) == check_column(tic_tac_toe) == check_diagonal(tic_tac_toe) is None and
          check_anti_diagonal(tic_tac_toe) is None and input_cells.count("X") + input_cells.count("O") != 9
          and (input_cells.count("X") != input_cells.count("O") or input_cells.count("X") != input_cells.count(
                "O") + 1)):
        print("Impossible")
        return True
    elif (check_row(tic_tac_toe) == "XO" or check_column(tic_tac_toe) == "XO" or check_diagonal(tic_tac_toe) == "XO"
          or check_anti_diagonal(tic_tac_toe) == "XO"):
        print("Impossible")
        return True


def first_move(board, char):
    x, y = 0, 0
    run = True
    while run:
        str_input = input("Enter the coordinates:")
        if str_input[0] in ascii_letters:
            print("You should enter numbers!")
            continue
        else:
            x, y = map(int, str_input.split(" "))
            if x < 0 or x > 3 or y > 3 or y < 0:
                print("Coordinates should be from 1 to 3!")
                continue
            else:
                i = 3 - y
                j = x - 1
                if board[i][j] == "_":
                    # board[i][j] = "X"
                    board[i] = [char if n == j else board[i][n] for n, row in enumerate(board[i]) ]
                    run = False
                    return board
                else:
                    print("This cell is occupied! Choose another one!")
                    continue

def computer_move(board, char, level):
    if char == "X":
        opp_char = "O"
    else:
        opp_char = "X"
    if level == "easy":
        print('Making move level "easy"')
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "_":
                    # board[i][j] = "X"
                    board[i] = [char if n == j else board[i][n] for n, row in enumerate(board[i])]
                    return board
                else:
                    continue
    elif level == "medium":
        x, y = 0, 0
        print('Making move level "medium"')
        for i in range(len(board)):
            if board[i].count(char) == 2 and "_" in board[i] :
                index_space = board[i].index("_")
                board[i][index_space] = char
                return board
            elif board[i].count(opp_char) == 2 and "_" in board[i]:
                index_space = board[i].index("_")
                board[i][index_space] = char
                return board
            else:
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] == "_":
                            # board[i][j] = "X"
                            board[i] = [char if n == j else board[i][n] for n, row in enumerate(board[i])]
                            return board
                        else:
                            continue
    elif level == "hard":
        x, y = 0, 0
        print('Making move level "medium"')
        for i in range(len(board)):
            if board[i].count(char) == 2 and "_" in board[i] :
                index_space = board[i].index("_")
                board[i][index_space] = char
                return board
            elif board[i].count(opp_char) == 2 and "_" in board[i]:
                index_space = board[i].index("_")
                board[i][index_space] = char
                return board
            else:
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] == "_":
                            # board[i][j] = "X"
                            board[i] = [char if n == j else board[i][n] for n, row in enumerate(board[i])]
                            return board
                        else:
                            continue


def print_board(board):
    print("---------")
    for k in range(len(board)):
        print("|", *board[k], "|", sep=" ")
    print("---------")


while True:
    play_choice = input("Input command:")
    if(len(play_choice.split()) < 3):
        print("Bad parameters!")
    elif(len(play_choice.split()) == 3):
        break
tic_tac_toe_board = [["_","_","_"] for n in range(3)]
print_board(tic_tac_toe_board)
choice = play_choice.split()
# validate_win_scenarios(tic_tac_toe, input_cell)
for i in range(9):
    modified_board =[]
    if choice[1] in("easy", "medium", "hard"):
        str = "X"
        modified_board = computer_move(tic_tac_toe_board, str, choice[1])
        print_board(modified_board)
        # input_cells = "".join([' '.join([str(c) for c in lst]) for lst in modified_board])
        input_cells = ''.join([data for ele in modified_board for data in ele])
        run = validate_win_scenarios(tic_tac_toe_board, input_cells)
        if run:
            break
    elif choice[1] == "user":
        str = "X"
        modified_board = first_move(tic_tac_toe_board, str)
        print_board(modified_board)
        # input_cells = "".join([' '.join([str(c) for c in lst]) for lst in modified_board])
        input_cells = ''.join([data for ele in modified_board for data in ele])
        run = validate_win_scenarios(tic_tac_toe_board, input_cells)
        if run:
            break
    if choice[2] in("easy", "medium", "hard"):
        str = "O"
        modified_board = computer_move(tic_tac_toe_board, str, choice[2])
        print_board(modified_board)
        # input_cells = "".join([' '.join([str(c) for c in lst]) for lst in modified_board])
        input_cells = ''.join([data for ele in modified_board for data in ele])
        run = validate_win_scenarios(tic_tac_toe_board, input_cells)
        if run:
            break
    elif choice[2] == "user":
        str = "O"
        modified_board = first_move(tic_tac_toe_board, str)
        print_board(modified_board)
        # input_cells = "".join([' '.join([str(c) for c in lst]) for lst in modified_board])
        input_cells = ''.join([data for ele in modified_board for data in ele])
        run = validate_win_scenarios(tic_tac_toe_board, input_cells)
        if run:
            break

    tic_tac_toe_board = modified_board

