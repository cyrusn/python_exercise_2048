#!/usr/bin/env python3

from game import Game
from tkinter import Tk, Frame, Label, CENTER

# we have class variables

GRID_LEN = 4
GRID_PADDING = 8
FONT_SIZE = 40
LABEL_WIDTH = 4
LABEL_HEIGHT = 2

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {
    0: BACKGROUND_COLOR_CELL_EMPTY,
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}
CELL_COLOR_DICT = {
    0: BACKGROUND_COLOR_CELL_EMPTY,
    2: "#776e65",
    4: "#776e65",
    8: "#f9f6f2",
    16: "#f9f6f2",
    32: "#f9f6f2",
    64: "#f9f6f2",
    128: "#f9f6f2",
    256: "#f9f6f2",
    512: "#f9f6f2",
    1024: "#f9f6f2",
    2048: "#f9f6f2",
}

FONT = ("Verdana", FONT_SIZE, "bold")

KEY_QUIT = "q"
KEY_RESET = "r"
KEY_UP = "Up"
KEY_DOWN = "Down"
KEY_RIGHT = "Right"
KEY_LEFT = "Left"


class App:
    def __init__(self, font=FONT):
        super().__init__()
        self.font = font
        self.Tk = Tk()
        self.lift_window()
        self.register_key_listeners()
        self.grid_cells = []
        self.init_grid()
        self.init_score_label()
        self.game = Game()
        self.commands = {
            KEY_RESET: self.game.reset,
            KEY_QUIT: self.Tk.quit,
            KEY_UP: self.game.tilt_up,
            KEY_DOWN: self.game.tilt_down,
            KEY_LEFT: self.game.tilt_left,
            KEY_RIGHT: self.game.tilt_right,
        }

    def run(self):
        self.game_start()
        self.Tk.mainloop()

    def lift_window(self):
        self.Tk.title("2048")
        self.Tk.lift()
        self.Tk.attributes("-topmost", True)

    def game_start(self):
        self.game.start()
        self.update_cells()

    def register_key_listeners(self):
        self.Tk.bind("<Key>", self.handle_key)

    def handle_key(self, e):
        if e.char in self.commands:
            self.commands[e.char]()

        if e.keysym in self.commands:
            self.commands[e.keysym]()
            self.update_cells()

        if self.game.over:
            self.score_label.configure(
                text="Game over, your final score is {}".format(self.game.score)
            )

    def update_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                cell_value = self.game.board[j][i]
                self.grid_cells[j][i].configure(
                    text="{context}".format(
                        context="" if cell_value == 0 else cell_value
                    ),
                    bg=BACKGROUND_COLOR_DICT[cell_value],
                    fg=CELL_COLOR_DICT[cell_value],
                )
        self.score_label.configure(text="Score: {}".format(self.game.score))

    def init_score_label(self):
        self.score_label = Label(self.Tk, text="")
        self.score_label.grid()

    def init_grid(self):
        background = Frame(self.Tk, bg=BACKGROUND_COLOR_GAME)
        background.grid()
        for row in range(GRID_LEN):
            grid_row = []
            for column in range(GRID_LEN):
                cell = Label(
                    background,
                    bg=BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=self.font,
                    width=LABEL_WIDTH,
                    height=LABEL_HEIGHT,
                )
                cell.grid(row=row, column=column, padx=GRID_PADDING, pady=GRID_PADDING)
                grid_row.append(cell)
            self.grid_cells.append(grid_row)


if __name__ == "__main__":
    App().run()
