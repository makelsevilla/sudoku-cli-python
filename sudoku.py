import os

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

    draw_board(board)


def draw_board(board):
    os.system("clear")

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

if __name__ == "__main__":
    # start the game
    start()