from model import TicTacToeModel
from view import TicTacToeView

class TicTacToeController:
    def __init__(self):
        self.model = TicTacToeModel()
        self.view = TicTacToeView(self)

    def handle_move(self, row, column):
        if self.model.make_move(row, column):
            self.view.update_board(self.model.board)
            
            # Chỉ hiển thị cảnh báo khi chơi với bot
            if self.model.playing_with_bot and self.model.warning_message:
                self.view.show_warning(self.model.warning_message)
            else:
                self.view.show_warning("")

            winner, winning_cells = self.model.check_winner()
            if winner:
                if winner == "Tie":
                    self.view.update_status("Hòa!", self.view.color_yellow)
                else:
                    self.view.update_status(f"{winner} là người thắng!", self.view.color_yellow)
                    self.view.highlight_winner(winning_cells)
                return
            self.view.update_status(f"Lượt của {self.model.curr_player}")

    def predict_move(self):
        # Chỉ thực hiện dự đoán khi chơi với bot
        if not self.model.playing_with_bot:
            return
        move, reason = self.model.predict_best_move()
        if move:
            row, col = move
            self.view.highlight_prediction(row, col)
            self.view.show_prediction(f"Nước đi tốt nhất: ({row+1},{col+1}) - {reason}")

    def restart_game(self):
        self.model.reset_game()
        self.view.update_board(self.model.board)
        self.view.update_status(f"Lượt của {self.model.curr_player}")
        self.view.clear_warnings()

    def set_game_mode(self, mode):
        """Đặt chế độ chơi: bot_easy, bot_hard hoặc 2p."""
        self.model.set_game_mode(mode)
        self.view.update_board(self.model.board)
        self.view.update_status(f"Lượt của {self.model.curr_player}")
        self.view.clear_warnings()

    def run(self):
        self.view.run()

if __name__ == "__main__":
    game = TicTacToeController()
    game.run()