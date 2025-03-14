import tkinter

class TicTacToeView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tkinter.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)

        self.color_blue = "#4584b6"
        self.color_yellow = "#ffde57"
        self.color_gray = "#343434"
        self.color_light_gray = "#646464"

        self.frame = tkinter.Frame(self.window)

        # Label trạng thái
        self.label = tkinter.Label(self.frame, text="X's turn", font=("Consolas", 20),
                                   background=self.color_gray, foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        # Nút chọn chế độ chơi
        self.mode_frame = tkinter.Frame(self.window)
        self.bot_button = tkinter.Button(self.mode_frame, text="Chơi với Bot",
                                         font=("Consolas", 14), command=lambda: self.controller.set_game_mode("bot"))
        self.bot_button.pack(side="left", padx=5)

        self.two_player_button = tkinter.Button(self.mode_frame, text="Chơi 2 Người",
                                                font=("Consolas", 14), command=lambda: self.controller.set_game_mode("2p"))
        self.two_player_button.pack(side="left", padx=5)
        self.mode_frame.pack(pady=10)

        # Bảng cờ
        self.board_buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for column in range(3):
                self.board_buttons[row][column] = tkinter.Button(
                    self.frame, text="", font=("Consolas", 50, "bold"),
                    background=self.color_gray, foreground=self.color_blue, width=4, height=1,
                    command=lambda r=row, c=column: self.controller.handle_move(r, c)
                )
                self.board_buttons[row][column].grid(row=row + 1, column=column)

        # Nút restart
        self.restart_button = tkinter.Button(self.frame, text="Restart", font=("Consolas", 20),
                                             background=self.color_gray, foreground="white",
                                             command=self.controller.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

        self.frame.pack()

    def update_board(self, board):
        for row in range(3):
            for column in range(3):
                self.board_buttons[row][column].config(text=board[row][column], foreground=self.color_blue,
                                                       background=self.color_gray)

    def update_status(self, message, color="white"):
        self.label.config(text=message, foreground=color)

    def highlight_winner(self, winning_cells):
        for row, col in winning_cells:
            self.board_buttons[row][col].config(foreground=self.color_yellow, background=self.color_light_gray)

    def run(self):
        self.window.mainloop()
