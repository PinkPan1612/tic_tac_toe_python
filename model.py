import random

class TicTacToeModel:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.playerX = "X"
        self.playerO = "O"
        self.curr_player = self.playerX
        self.turns = 0
        self.game_over = False
        self.playing_with_bot = False  # Mặc định chơi 2 người
        self.bot_difficulty = "hard"   # Mặc định bot khó khi chơi với bot
        self.history = []
        self.warning_message = ""
        self.suggestion = ""

    def set_game_mode(self, mode):
        if mode == "2p":
            self.playing_with_bot = False
        elif mode == "bot_easy":
            self.playing_with_bot = True
            self.bot_difficulty = "easy"
        elif mode == "bot_hard":
            self.playing_with_bot = True
            self.bot_difficulty = "hard"
        self.reset_game()

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.curr_player = self.playerX
        self.turns = 0
        self.game_over = False
        self.history = []
        self.warning_message = ""
        self.suggestion = ""

    def make_move(self, row, column):
        if self.game_over or self.board[row][column] != "":
            return False

        self.history.append((row, column, self.curr_player))
        self.board[row][column] = self.curr_player
        self.turns += 1
        winner, winning_cells = self.check_winner()

        if winner:
            self.game_over = True
            return True

        self.switch_player()

        # Cập nhật cảnh báo và gợi ý chỉ khi chơi với bot và ở chế độ Bot Khó
        if self.playing_with_bot and self.bot_difficulty == "hard":
            self.check_and_warn()
            self.generate_suggestion()
        else:
            self.warning_message = ""
            self.suggestion = ""

        if self.playing_with_bot and self.curr_player == self.playerO:
            self.bot_move()

        return True

    def check_and_warn(self):
        opponent = self.playerX if self.curr_player == self.playerO else self.playerO
        winning_move = self.find_winning_move(opponent)
        if winning_move:
            row, col = winning_move
            self.warning_message = f"Cảnh báo! {opponent} sắp thắng ở vị trí ({row+1}, {col+1})!"
        else:
            self.warning_message = ""

    def generate_suggestion(self):
        move, reason = self.predict_best_move()
        if move:
            row, col = move
            self.suggestion = f"Gợi ý: Đi ({row+1}, {col+1}) - {reason}."
        else:
            self.suggestion = "Không có gợi ý nước đi."

    def predict_best_move(self):
        player = self.curr_player

        move = self.find_winning_move(player)
        if move:
            return move, "nước thắng"

        opponent = self.playerX if player == self.playerO else self.playerO
        move = self.find_winning_move(opponent)
        if move:
            return move, "nước phòng thủ"

        if self.board[1][1] == "":
            return (1, 1), "vị trí trung tâm"

        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        available_corners = [corner for corner in corners if self.board[corner[0]][corner[1]] == ""]
        if available_corners:
            return random.choice(available_corners), "vị trí góc"

        available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        if available_moves:
            return random.choice(available_moves), "nước đi có thể"

        return None, "không có nước đi khả dụng"

    def bot_move(self):
        if self.bot_difficulty == "easy":
            available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
            if available_moves:
                move = random.choice(available_moves)
                row, col = move
                # Bot Dễ chọn nước đi ngẫu nhiên
                self.make_move(row, col)
        else:  # Bot Khó
            move, _ = self.predict_best_move()
            if move:
                row, col = move
                self.make_move(row, col)

    def find_winning_move(self, player):
        for i in range(3):
            row = [self.board[i][j] for j in range(3)]
            move = self.check_line(row, player, lambda col: (i, col))
            if move:
                return move

        for i in range(3):
            col = [self.board[j][i] for j in range(3)]
            move = self.check_line(col, player, lambda row: (row, i))
            if move:
                return move

        diag1 = [self.board[i][i] for i in range(3)]
        move = self.check_line(diag1, player, lambda i: (i, i))
        if move:
            return move

        diag2 = [self.board[i][2-i] for i in range(3)]
        move = self.check_line(diag2, player, lambda i: (i, 2-i))
        if move:
            return move

        return None

    def check_line(self, line, player, position_func):
        if line.count(player) == 2 and line.count("") == 1:
            empty_index = line.index("")
            return position_func(empty_index)
        return None

    def switch_player(self):
        self.curr_player = self.playerO if self.curr_player == self.playerX else self.playerX

    def check_winner(self):
        board = self.board

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
                return board[i][0], [(i, 0), (i, 1), (i, 2)]

        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
                return board[0][i], [(0, i), (1, i), (2, i)]

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
            return board[0][0], [(0, 0), (1, 1), (2, 2)]

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
            return board[0][2], [(0, 2), (1, 1), (2, 0)]

        if self.turns == 9:
            return "Tie", []

        return None, []
