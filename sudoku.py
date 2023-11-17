import sys

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

    pre_filled_cell = generate_pre_filled_cell_array(board)
            
    while True:
        print("\n\n")
        print("Pre-filled cells board")
        draw_board(pre_filled_cell)

        print("Current Board")
        draw_board(board)

        # get the user input
        user_inputs = (input("(Row,Column,Value): ")).split(",")
        # check if the user provided atleast 3 input
        if (len(user_inputs) < 3):
            print("Too few arguments. Please try again.")
            continue
        inputs = {}
        try:
            #  convert the input to integer
            inputs["row"] = int(user_inputs[0].strip())
            inputs["col"] = int(user_inputs[1].strip())
            inputs["value"] = int(user_inputs[2].strip())
        except:
            print("Non integer value entered.")
            continue

        # Check the inputs if between 0 and 9
        if not inputs_are_between_0_and_9(inputs):
            print("A value/s are out of range.")
            continue

        # skip if the cell is pre-filled
        if pre_filled_cell[inputs["row"] - 1][inputs["col"] - 1]:
            print("The cell selected is pre-filled. Choose another cell")
            continue

        if inputs["value"] != 0:
            if not can_insert_value_to_cell(inputs, board):
                print("Value have conflicts. Select a different value to insert.")
                continue

        # insert the value to cell if all checks passed
        board[inputs["row"] - 1][inputs["col"] -1] = inputs["value"]

        # checks if all cells are filled
        if board_is_filled(board):
            print("Game Over! Thank you for playing.")
            sys.exit()


def board_is_filled(board):
    # checks all the cells if all is not equal to 0
    for row in board:
        for col in row:
            if col == 0:
                return False
            
    return True

# returns true if value doesn't have conflicts
def can_insert_value_to_cell(inputs, board):
# subtract 1 to the value of row and col
    row_idx = inputs["row"] - 1
    col_idx = inputs["col"] - 1 
    
    value = inputs["value"]

    # check every column of the row if equal to the value
    for idx, col_value in enumerate(board[row_idx]):
        if col_value == value and idx != col_idx:
            return False
        
    # check every row of the column if equal to the value
    for idx, row in enumerate(board):
        if row[col_idx] == value and idx != row_idx:
            return False

    # check the sub-grid
    # get the sub-grid to check
    row_start = row_idx // 3 * 3
    row_end = row_start + 3

    col_start = col_idx // 3 * 3
    col_end = col_start + 3

    for sub_row_idx in range(row_start, row_end):
        for sub_col_idx in range(col_start, col_end):
            if board[sub_row_idx][sub_col_idx] == value and (sub_col_idx != col_idx and sub_row_idx != row_idx):
                return False
    
    # return true if value does not have conflicts
    return True


def inputs_are_between_0_and_9(inputs):
    for key, value in inputs.items():
        if value < 0 or value > 9:
            return False
        
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

def generate_pre_filled_cell_array(board):
    filled_cell_array = [[0 for _ in range(9)] for _ in range(9)]

    print(len(board))
    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            if board[row_idx][col_idx] > 0:
                filled_cell_array[row_idx][col_idx] = 1

    return filled_cell_array

if __name__ == "__main__":
    # start the game
    start()


# Region