from game import Game
from tkinter import Tk, Frame, Label, CENTER
from time import sleep

SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {
    0: BACKGROUND_COLOR_CELL_EMPTY, 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
    16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
    256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
}
CELL_COLOR_DICT = {
    0: BACKGROUND_COLOR_CELL_EMPTY, 2: "#776e65", 4: "#776e65", 8: "#f9f6f2",
    16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
    256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"
}
FONT = ("Verdana", 40, "bold")

KEY_RESET = "r"
KEY_UP = "w"
KEY_DOWN = "s"
KEY_LEFT = "a"
KEY_RIGHT = "d"
KEY_QUIT = "q"


class App(Frame):
    def __init__(self, master=None):
        super().__init__()
        self.grid()
        self.master = master
        self.lift_window()
        self.add_listen_key_event()
        self.init_score_label()
        self.grid_cells = []
        self.init_grid()
        self.game = Game()
        self.commands = {
            KEY_RESET: self.game.reset,
            KEY_QUIT: self.quit,
            KEY_UP: self.game.move_up,
            KEY_DOWN: self.game.move_down,
            KEY_LEFT: self.game.move_left,
            KEY_RIGHT: self.game.move_right,
        }

        self.game_start()

    def lift_window(self):
        self.master.title('2048')
        self.master.lift()
        self.master.attributes("-topmost", True)

    def game_start(self):
        self.game.newTile()
        self.update_cells_values()

    def add_listen_key_event(self):
        self.master.bind("<Key>", self.listen_key)

    def listen_key(self, e):
        key = e.char
        if self.game.over:
            self.score_label.configure(
                text='Game over, your final score is {}'.format(
                    self.game.score)
            )
        if key in self.commands:
            self.commands[e.char]()
            self.game.newTile()
            self.update_cells_values()

    def update_cells_values(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                cell_value = self.game.board[j][i]
                self.grid_cells[j][i].configure(
                    text='{context}'.format(
                        context='' if cell_value == 0 else cell_value,
                    ),
                    bg=BACKGROUND_COLOR_DICT[cell_value],
                    fg=CELL_COLOR_DICT[cell_value]
                )
        self.score_label.configure(text='Score: {}'.format(self.game.score))

    def init_score_label(self):
        self.score_label = Label(self.master, text='Hello world')
        self.score_label.grid()

    def init_grid(self):
        background = Frame(
            self,
            bg=BACKGROUND_COLOR_GAME,
            width=SIZE,
            height=SIZE,
        )
        background.grid()
        for row in range(GRID_LEN):
            grid_row = []
            for column in range(GRID_LEN):
                cell = Label(
                    background,
                    bg=BACKGROUND_COLOR_CELL_EMPTY,
                    width=SIZE//GRID_LEN, height=SIZE//GRID_LEN
                )
                cell.grid(
                    row=row,
                    column=column,
                    padx=GRID_PADDING,
                    pady=GRID_PADDING
                )
                t = Label(
                    master=cell,
                    text="",
                    bg=BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=FONT,
                    width=4,
                    height=2
                )
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)


root = Tk()
app = App(root)
root.mainloop()
