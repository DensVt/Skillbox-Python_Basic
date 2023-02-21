def display_instruction():
    print("""
    Привет! Это игра 'Крестики-нолики'.
    Чтобы сделать ход, введите номер клетки,
    куда хотите поставить свой символ:
    """)


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    board = list(range(1, 10))

    def display_board(self):
        print("-" * 13)
        for cell in range(3):
            print("|", self.board[0 + cell * 3],
                  "|", self.board[1 + cell * 3],
                  "|", self.board[2 + cell * 3], "|")
            print("-" * 13)


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    def __init__(self, symbol):
        self.symbol = symbol

    def take_input(self):
        flag = False
        while not flag:
            player_answer = input("Куда поставим " + self.symbol + " ? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if 1 <= player_answer <= 9:
                if str(Board.board[player_answer - 1]) not in "ХО":
                    Board.board[player_answer - 1] = self.symbol
                    flag = True
                else:
                    print("Эта клеточка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9 чтоб сделать ход.")


class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    def __init__(self):
        self.win_coord = (
            (0, 1, 2), (3, 4, 5),
            (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        )

    def check_win(self):
        for each in self.win_coord:
            if Board.board[each[0]] == Board.board[each[1]] == Board.board[each[2]]:
                return Board.board[each[0]]
        return False


def game():
    display_instruction()
    board = Board()
    result = Cell()
    counter = 0
    win = False
    while not win:
        board.display_board()
        if counter % 2 == 0:
            Player("Х").take_input()
        else:
            Player("О").take_input()
        counter += 1
        if counter > 4:
            tmp = result.check_win()
            if tmp:
                print(tmp, "Победил!")
                win = True
                break
        if counter == 9:
            print("Ничья")
            break
    board.display_board()


game()
input("Нажмите Enter для выхода")
