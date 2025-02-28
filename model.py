class TicTacToeModel:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.playerX = "X"
        self.playerO = "O"
        self.curr_player = self.playerX
        self.turns = 0
        self.game_over = False

    def reset_game(self):
        """Reset game state."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.curr_player = self.playerX
        self.turns = 0
        self.game_over = False

    def make_move(self, row, column):
        """Set a move on the board."""
        if self.game_over or self.board[row][column] != "":
            return False

        self.board[row][column] = self.curr_player
        self.turns += 1
        self.check_winner()
        self.switch_player()
        return True

    def switch_player(self):
        """Switch to the next player."""
        self.curr_player = self.playerO if self.curr_player == self.playerX else self.playerX

    def check_winner(self):
        """Kiểm tra nếu có người thắng và trả về danh sách ô thắng."""
        board = self.board

        # Kiểm tra hàng ngang
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
                self.game_over = True
                return board[i][0], [(i, 0), (i, 1), (i, 2)]

        # Kiểm tra hàng dọc
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
                self.game_over = True
                return board[0][i], [(0, i), (1, i), (2, i)]

        # Kiểm tra đường chéo chính
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
            self.game_over = True
            return board[0][0], [(0, 0), (1, 1), (2, 2)]

        # Kiểm tra đường chéo phụ
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
            self.game_over = True
            return board[0][2], [(0, 2), (1, 1), (2, 0)]

        # Kiểm tra hòa
        if self.turns == 9:
            self.game_over = True
            return "Tie", []

        return None, []
