import tkinter as tk


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()  # Создание главного окна приложения
        self.root.title('Крестики-нолики')
        self.current_player = 'X'  # Инициализация текущего игрока
        self.buttons = []  # Список кнопок
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]  # Создание пустого игрового поля
        self.new_game()

    def new_game(self):
        for row in range(3):
            button_row = list()  # Список кнопок для каждой строки
            for col in range(3):
                button = tk.Button(self.root, text='', width=5, height=2,
                                   font=('Helvetica', 20, 'bold'),
                                   command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row + 1, column=col, sticky='nsew')  # Размещаем кнопку на поле
                button_row.append(button)  # Добавляем кнопку в список для текущей строки
            self.buttons.append(button_row)  # Добавляем в список всех кнопок одну из 3 строк кнопок

    def on_button_click(self, row, col):
        if self.board[row][col] is None:  # Если ячейка пустая
            self.board[row][col] = self.current_player  # Заполняем ячейку
            self.buttons[row][col].config(text=self.current_player)  # Обновление текста на кнопке
            if self.check_win():  # Проверка на выигрыш
                self.disable_buttons()  # Отключение всех кнопок
            elif self.check_tie():  # Проверка на ничью
                self.disable_buttons()
            else:
                self.toggle_player()  # Переключение текущего игрока

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] is not None:  # Проверка горизонтальных линий
                self.highlight_winner(i, 0,
                                      i, 1,
                                      i, 2)
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] is not None:  # Проверка вертикальных линий
                self.highlight_winner(0, i,
                                      1, i,
                                      2, i)
                return True
            elif self.board[0][0] == self.board[1][1] == self.board[2][2] is not None:  # Диагональ слева направо
                self.highlight_winner(0, 0,
                                      1, 1,
                                      2, 2)
                return True
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:  # Диагональ справа налево
                self.highlight_winner(0, 2,
                                      1, 1,
                                      2, 0)
                return True
            else:
                return False

    def highlight_winner(self, row1, col1, row2, col2, row3, col3):
        self.buttons[row1][col1].config(bg='green')
        self.buttons[row2][col2].config(bg='green')
        self.buttons[row3][col3].config(bg='green')

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def toggle_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    game = TicTacToe()
    game.run()
