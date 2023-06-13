import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Хрестики-нулики")

        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text=' ', width=10, height=5,
                               command=lambda pos=i: self.make_move(pos))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            self.buttons[position].config(state='disabled')

            if self.check_winner():
                self.display_message("Гравець " + self.current_player + " переміг!")
                self.disable_buttons()
            elif self.check_tie():
                self.display_message("Гра закінчилась у нічию!")
                self.disable_buttons()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [self.board[0], self.board[1], self.board[2]],  # перша горизонтальна лінія
            [self.board[3], self.board[4], self.board[5]],  # друга горизонтальна лінія
            [self.board[6], self.board[7], self.board[8]],  # третя горизонтальна лінія
            [self.board[0], self.board[3], self.board[6]],  # перша вертикальна лінія
            [self.board[1], self.board[4], self.board[7]],  # друга вертикальна лінія
            [self.board[2], self.board[5], self.board[8]],  # третя вертикальна лінія
            [self.board[0], self.board[4], self.board[8]],  # перша діагональна лінія
            [self.board[2], self.board[4], self.board[6]]   # друга діагональна лінія
        ]

        return any(combination == [self.current_player, self.current_player, self.current_player]
                   for combination in winning_combinations)

    def check_tie(self):
        return ' ' not in self.board

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state='disabled')

    def display_message(self, message):
        messagebox.showinfo("Хрестики-нулики", message)

    def start(self):
        self.root.mainloop()


# Запуск гри
game = TicTacToeGUI()
game.start()
