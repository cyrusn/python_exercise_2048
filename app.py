from random import choice

board = [[0 for i in range(4)] for j in range(4)]
gameOver = False


def add(row, reverse=False):
    if reverse:
        row.reverse()

    result = row[:]
    for i in range(3):
        if row[i] == row[i+1] and row[i] != 0:
            sum = row[i] + row[i+1]
            result.pop(i+1)
            result[i] = sum
            result.append(0)
            break
    if reverse:
        result.reverse()
    for i in range(4):
        row[i] = result[i]


def transpose(board):
    column_tiles = [[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            column_tiles[i][j] = board[j][i]

    return column_tiles


def sortBoard(board, reverse=False):
    for row in board:
        row.sort(key=lambda x: x == 0, reverse=reverse)
        add(row, reverse=reverse)
    return board


def move_vertical(up=True):
    transposedBoard = transpose(board)
    sortedTransposedBoard = sortBoard(transposedBoard, reverse=not up)
    for i in range(4):
        for j in range(4):
            board[j][i] = sortedTransposedBoard[i][j]


def move_horizontal(left=True):
    sortBoard(board, reverse=not left)


def printBoard(board):
    for row in board:
        for i in row:
            print("{:4}".format(i), end=' ')
        print()


def checkZeroTiles(board):
    zeroTiles = []
    for j, row in enumerate(board):
        for i, col in enumerate(row):
            if col == 0:
                zeroTiles.append((i, j))
    return zeroTiles


def generate2Tile(board):
    zeroTiles = checkZeroTiles(board)
    if len(zeroTiles) == 0:
        global gameOver
        gameOver = True
        return
    selectTile = choice(zeroTiles)
    board[selectTile[1]][selectTile[0]] = choice([2, 4])


while not gameOver:
    generate2Tile(board)
    printBoard(board)
    v = input()
    if v == 'h':
        move_horizontal(left=True)
    elif v == 'l':
        move_horizontal(left=False)
    elif v == 'k':
        move_vertical(up=True)
    elif v == 'j':
        move_vertical(up=False)

print("Game Over")
