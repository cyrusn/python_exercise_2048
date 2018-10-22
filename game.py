from random import choice


class Game():
    """
        Class Game is stored all methods require for the game.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [[0 for i in range(4)] for j in range(4)]
        self.over = False
        self.score = 0

    def _add(self, row, reverse=False):
        """
            add method is a method for adding first 2 neighbors with same values
            (except 0) in a row, and append 0 to the end of row.
            e.g. [0, 2, 2, 4] => [0, 4, 4, 0]
        """
        if reverse:
            row.reverse()

        result = row[:]
        for i in range(3):
            if row[i] == row[i+1] and row[i] != 0:
                result[i] = row[i] + row[i+1]
                self.score += result[i]
                result.pop(i+1)
                result.append(0)
                break
        if reverse:
            result.reverse()
        for i in range(4):
            row[i] = result[i]

    def _transpose(self):
        transposedBoard = [[0 for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                transposedBoard[i][j] = self.board[j][i]
        return transposedBoard

    def _sortBoard(self, board, reverse=False):
        for row in board:
            row.sort(key=lambda x: x == 0, reverse=reverse)
            self._add(row, reverse=reverse)
        return board

    def _move_vertical(self, up=True):
        transposedBoard = self._transpose()
        sortedTransposedBoard = self._sortBoard(
            transposedBoard, reverse=not up)
        for i in range(4):
            for j in range(4):
                self.board[j][i] = sortedTransposedBoard[i][j]

    def _move_horizontal(self, left=True):
        self._sortBoard(self.board, reverse=not left)

    def _checkZeroTiles(self):
        zeroTiles = []
        for j, row in enumerate(self.board):
            for i, col in enumerate(row):
                if col == 0:
                    zeroTiles.append((i, j))
        return zeroTiles

    def newTile(self):
        zeroTiles = self._checkZeroTiles()
        if len(zeroTiles) == 0:
            self.gameOver = True
            return
        selectTile = choice(zeroTiles)
        self.board[selectTile[1]][selectTile[0]] = choice([2, 2, 2, 4])

    def move_left(self):
        self._move_horizontal(left=True)

    def move_right(self):
        self._move_horizontal(left=False)

    def move_up(self):
        self._move_vertical(up=True)

    def move_down(self):
        self._move_vertical(up=False)
