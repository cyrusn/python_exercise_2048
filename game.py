from random import choice


class Game:
    """
        Class `Game` stores all methods require for the game.
    """

    @staticmethod
    def _new_board():
        return [[0 for i in range(4)] for j in range(4)]

    @staticmethod
    def _merge_tiles(row):
        """
            merge the first 2 neighboring tiles in a row with the same value
            into a tile of their sum.
            note: row is muted in place

            >>> [2, 2, 4], False => [4, 4]
            >>> [2, 2], False => [4]
            >>> [4, 2], False => [4, 2]
        """
        score = 0
        result = row[:]

        # do nothing if the length of row has only zero or 1 element.
        if len(result) < 2:
            return score, result

        for i in range(len(result) - 1):
            if row[i] == row[i + 1]:
                result[i] = row[i] + row[i + 1]
                score += result[i]
                result.pop(i + 1)
                break
        return score, result

    @staticmethod
    def _free_fall(board):
        scores = 0
        for row in board:
            filteredList = [x for x in row if x != 0]
            score, newRow = Game._merge_tiles(filteredList)

            while len(newRow) < 4:
                newRow.append(0)

            scores += score

            for i in range(4):
                row[i] = newRow[i]
        return (scores, board)

    @staticmethod
    def _transpose(board, rotation=90):
        transposed = Game._new_board()

        for i in range(4):
            for j in range(4):
                if rotation == 0:
                    transposed[j][i] = board[j][i]
                elif rotation == 90:
                    transposed[j][i] = board[i][j]
                elif rotation == 180:
                    transposed[j][i] = board[j][3 - i]
                elif rotation == 270:
                    transposed[j][i] = board[3 - i][3 - j]

        return transposed

    @staticmethod
    def new_tile(board):
        zero_tiles = []
        value = choice([2, 2, 2, 4])

        for j, row in enumerate(board):
            for i, col in enumerate(row):
                if col == 0:
                    zero_tiles.append((i, j))

        tile = choice(zero_tiles)
        return (tile, value)

    def __init__(self):
        self.reset()

    def reset(self):
        self.board = Game._new_board()
        self.over = False
        self.score = 0

    def start(self):
        try:
            tile, value = Game.new_tile(self.board)
            self.board[tile[1]][tile[0]] = value
        except Exception:
            self.over = True

    def _tilt(self, rotation):
        transposedBoard = Game._transpose(self.board, rotation=rotation)
        score, updatedBoard = Game._free_fall(transposedBoard)
        self.score += score
        self.board = Game._transpose(updatedBoard, rotation=rotation)
        self.start()

    def tilt_left(self):
        self._tilt(rotation=0)

    def tilt_right(self):
        self._tilt(rotation=180)

    def tilt_up(self):
        self._tilt(rotation=90)

    def tilt_down(self):
        self._tilt(rotation=270)


if __name__ == "__main__":
    board = [[i + 4 * j for i in range(4)] for j in range(4)]

    def printBoard(board):
        for i in board:
            for j in i:
                print("{:2}".format(j), end=" ")
            print()
        print()

    game = Game()

    commands = {
        "a": game.tilt_left,
        "d": game.tilt_right,
        "w": game.tilt_up,
        "s": game.tilt_down,
    }

    while not game.over:
        command = input("Please choose direction up: w, down: s, left: a, right: f\n")
        if command in commands:
            commands[command]()
        printBoard(game.board)
