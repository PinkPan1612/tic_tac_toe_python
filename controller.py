from model import TicTacToeModel
from view import TicTacToeView

class TicTacToeController:
    def __init__(self):
        self.model = TicTacToeModel()
        self.view = TicTacToeView(self)

    def handle_move(self, row, column):
        if self.model.make_move(row, column):
            self.view.update_board(self.model.board)
            winner, winning_cells = self.model.check_winner()
            if winner:
                if winner == "Tie":
                    self.view.update_status("It's a tie!", self.view.color_yellow)
                else:
                    self.view.update_status(f"{winner} is the winner!", self.view.color_yellow)
                    self.view.highlight_winner(winning_cells)
            else:
                self.view.update_status(f"{self.model.curr_player}'s turn")


    def restart_game(self):
        self.model.reset_game()
        self.view.update_board(self.model.board)  # Cập nhật lại toàn bộ ô, bao gồm cả style
        self.view.update_status(f"{self.model.curr_player}'s turn")

    def run(self):
        self.view.run()

if __name__ == "__main__":
    game = TicTacToeController()
    game.run()
