import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe Nâng Cao")
        self.window.resizable(False, False)

        self.color_blue = "#4584b6"
        self.color_yellow = "#ffde57"
        self.color_gray = "#343434"
        self.color_light_gray = "#646464"
        self.color_green = "#00cc00"
        self.color_red = "#ff4444"

        self.frame = tk.Frame(self.window)

        # Label trạng thái
        self.label = tk.Label(self.frame, text="X's turn", font=("Consolas", 20),
                              background=self.color_gray, foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        # Label cảnh báo (chỉ hiển thị khi chơi với bot)
        self.warning_label = tk.Label(self.frame, text="", font=("Consolas", 12),
                                     background=self.color_gray, foreground=self.color_red)
        self.warning_label.grid(row=5, column=0, columnspan=3, sticky="we")

        # Label dự đoán (chỉ hiển thị khi chơi với bot)
        self.prediction_label = tk.Label(self.frame, text="", font=("Consolas", 12),
                                        background=self.color_gray, foreground=self.color_green)
        self.prediction_label.grid(row=6, column=0, columnspan=3, sticky="we")

        # Nút chọn chế độ chơi
        self.mode_frame = tk.Frame(self.window)
        # Nút chọn Bot Dễ
        self.bot_easy_button = tk.Button(self.mode_frame, text="Chơi với Bot Dễ",
                                    font=("Consolas", 14), command=lambda: self.controller.set_game_mode("bot_easy"))
        self.bot_easy_button.pack(side="left", padx=5)
        # Nút chọn Bot Khó
        self.bot_hard_button = tk.Button(self.mode_frame, text="Chơi với Bot Khó",
                                           font=("Consolas", 14), command=lambda: self.controller.set_game_mode("bot_hard"))
        self.bot_hard_button.pack(side="left", padx=5)
        # Nút chơi 2 người
        self.two_player_button = tk.Button(self.mode_frame, text="Chơi 2 Người",
                                           font=("Consolas", 14), command=lambda: self.controller.set_game_mode("2p"))
        self.two_player_button.pack(side="left", padx=5)
        self.mode_frame.pack(pady=10)

        # Bảng cờ
        self.board_buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for column in range(3):
                self.board_buttons[row][column] = tk.Button(
                    self.frame, text="", font=("Consolas", 50, "bold"),
                    background=self.color_gray, foreground=self.color_blue, width=4, height=1,
                    command=lambda r=row, c=column: self.controller.handle_move(r, c)
                )
                self.board_buttons[row][column].grid(row=row + 1, column=column)

        # Nút chức năng
        self.button_frame = tk.Frame(self.frame, background=self.color_gray)
        self.button_frame.grid(row=4, column=0, columnspan=3, sticky="we")

        self.restart_button = tk.Button(self.button_frame, text="Restart", font=("Consolas", 16),
                                        background=self.color_gray, foreground="white",
                                        command=self.controller.restart_game)
        self.restart_button.pack(side="left", expand=True, fill="both")

        # Nút gợi ý chỉ hiển thị khi chơi với bot
        self.predict_button = tk.Button(self.button_frame, text="Gợi ý", font=("Consolas", 16),
                                       background=self.color_gray, foreground=self.color_green,
                                       command=self.controller.predict_move)
        self.predict_button.pack(side="left", expand=True, fill="both")
        
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

    def highlight_prediction(self, row, col):
        """Làm nổi bật nước đi được dự đoán."""
        if self.controller.model.board[row][col] != "":
            return
        self.update_board(self.controller.model.board)
        self.board_buttons[row][col].config(background=self.color_green)

    def show_warning(self, message):
        self.warning_label.config(text=message)

    def show_prediction(self, message):
        self.prediction_label.config(text=message)

    def clear_warnings(self):
        self.warning_label.config(text="")
        self.prediction_label.config(text="")

    def run(self):
        self.window.mainloop()