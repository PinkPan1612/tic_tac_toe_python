import random

class TicTacToeModel:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.playerX = "X"
        self.playerO = "O"
        self.curr_player = self.playerX
        self.turns = 0
        self.game_over = False
        self.playing_with_bot = False  # Mặc định chơi với người

    def set_game_mode(self, play_with_bot):
        """Thiết lập chế độ chơi với bot hoặc người."""
        self.playing_with_bot = play_with_bot
        self.reset_game()

    def reset_game(self):
        """Reset game state."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.curr_player = self.playerX
        self.turns = 0
        self.game_over = False

    def make_move(self, row, column):
        """Đặt một nước đi trên bàn cờ."""
        if self.game_over or self.board[row][column] != "":
            return False

        self.board[row][column] = self.curr_player
        self.turns += 1
        winner, _ = self.check_winner()
        
        if winner:
            self.game_over = True
            return True

        self.switch_player()

        # Nếu chơi với bot và là lượt của bot, bot sẽ tự động đánh
        if self.playing_with_bot and self.curr_player == self.playerO:
            self.bot_move()

        return True

    def bot_move(self):
        """Chọn một nước đi ngẫu nhiên cho bot."""
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        if available_moves:
            row, column = random.choice(available_moves)
            self.make_move(row, column)

    def switch_player(self):
        """Chuyển lượt chơi."""
        self.curr_player = self.playerO if self.curr_player == self.playerX else self.playerX

    def check_winner(self):
        """Kiểm tra nếu có người thắng và trả về danh sách ô thắng."""
        board = self.board

        # Kiểm tra hàng ngang
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
                return board[i][0], [(i, 0), (i, 1), (i, 2)]

        # Kiểm tra hàng dọc
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
                return board[0][i], [(0, i), (1, i), (2, i)]

        # Kiểm tra đường chéo chính
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
            return board[0][0], [(0, 0), (1, 1), (2, 2)]

        # Kiểm tra đường chéo phụ
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
            return board[0][2], [(0, 2), (1, 1), (2, 0)]

        # Kiểm tra hòa
        if self.turns == 9:
            return "Tie", []

        return None, []
