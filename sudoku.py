import os
import math

def start():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    filled_board_cell = generate_pre_defined_cell_array(board)

    while True:
        draw_board(board)

        # get the user input
        user_input = (input("(Row, Column, Value): ")).split(",")

        # check if the user provided a 3 input
        if (len(user_input) < 3):
            print("Too few arguments. Please try again.")

        try:
            #  convert the input to integer
            row = int(user_input[0].strip())
            col = int(user_input[1].strip())
            value = int(user_input[2].strip())
        except:
            print("Non integer value entered.")

        input_is_valid = validate_user_input(row, col, value, board)
        if not input_is_valid:
            print("Invalid")
        else:
            # alter the value in board if the cell is not included in pre-defined
            if not filled_board_cell[row - 1][col - 1]:
                board[row - 1][col - 1] = value
            else:
                print("The cell is pre-defined. choose another cell")


def validate_user_input(row, col, value, board):
    row_is_valid = number_is_between_1_to_9(row)
    col_is_valid = number_is_between_1_to_9(col)
    value_is_valid = number_is_between_1_to_9(value) and value_can_be_inserted_to_board(row, col, value, board)

    if (row_is_valid and col_is_valid and value_is_valid):
        return True

    return False


def number_is_between_1_to_9(num):
    # if num is not a number, emit error

    # if num is not a number between 1 and 9 return false
    if not (num > 0 and num < 10):
        return False

    return True

def value_can_be_inserted_to_board(row, col, value, board):
    # subtract 1 to the value of row and col
    row_idx = row - 1
    col_idx = col -1 

    # check if the cell is not a pre-defined cell

    # check the row
    # check the every column of the row if equal to the value
    for col_value in board[row_idx]:
        if col_value == value:
            return False

    # check the column
    # check every row of the column if equal to the value
    for row in board:
        if row[col_idx] == value:
            return False

    # check the sub-grid
    # get the sub-grid to check
    row_start = row_idx // 3 * 3
    row_end = row_start + 3

    col_start = col_idx // 3 * 3
    col_end = col_start + 3

    for sub_row_idx in range(row_start, row_end + 1):
        for sub_col_idx in range(col_start, col_end + 1):
            if board[sub_row_idx][sub_col_idx] == value:
                return False
    
    # return true if value is not found to any of the checks
    return True


def draw_board(board):

    print("-"*34)
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-"*34)
        
        print("|", end=" ")

        for j, col in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            value = col
            if col == 0:
                value = "."

            print(f"{value}  ", end="")
        
        print("|")
    print("-"*34)

def generate_pre_defined_cell_array(board):
    cell_array = [[False] * 9] * 9
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            cell_is_filled = board[row_idx][col_idx] > 0
            cell_array[row_idx][col_idx] == True
    print(cell_array)
    return cell_array

if __name__ == "__main__":
    # start the game
    start()


# Region