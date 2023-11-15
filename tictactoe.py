board = [["-"] * 3 for i in range(3)]  # создаем игровое поле


def greatings():  # функция для приветствия
    print("********************\n"
          "* Добро пожаловать *\n"
          "*      в игру      *\n"
          "* крестики--нолики *\n"
          "********************\n")


def draw_board():  # рисуем игровое поле

    print("********************\n"
          "*   | 0 | 1 | 2 |  *\n"
          "* ---------------  *")
    for i in range(3):
        row = " | ".join(board[i])
        print(f"* {i} | {row} |  *\n"
              "* ---------------  *")
    print("********************")


def make_move():  # запрос хода, координат / проверка на ошибки при вводе
    while True:
        move = input("  x - номер строки\n"
                     "  y - номер столбца\n"
                     " Введите координаты:\n"
                     "        ").split()
        if len(move) != 2:
            print(f"Введите две координаты!\n   Попробуйте снова...\n")
            continue
        x, y = move
        if not (x.isdigit()) or not (y.isdigit()):
            print("Координаты не являются числами!\n   Попробуйте снова...\n")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Вы ввели несуществующие координаты!\n   Попробуйте снова...\n")
            continue
        if board[x][y] != "-":
            print("Клетка занята!\nПопробуйте снова...\n")
            continue
        return x, y


def win_lines():  # проверка выигрышных комбинаций
    win_coords = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                  ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                  ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for coord in win_coords:
        win_line = []
        for i in coord:
            win_line.append(board[i[0]][i[1]])
        if win_line == ["X", "X", "X"]:
            print("  Выйграл игрок - 'X'")
            return True
        if win_line == ["O", "O", "O"]:
            print("  Выйграл игрок - 'O'")
            return True
    return False


move_count = 0
while True:  # запуск самой игры, очередность и количество ходов, вывод победителя
    move_count += 1
    greatings()
    draw_board()
    if move_count % 2 == 1:
        print("  Ход игрока - 'X'")
    else:
        print("  Ход игрока - 'O'")

    x, y = make_move()

    if move_count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "O"

    if win_lines():
        draw_board()
        break

    if move_count == 9:
        draw_board()
        print("    Ничья!")
        break
