# поле
field = [["-" for _ in range(3)] for _ in range(3)]

# вывод в терминал
def print_field():
    print("  0 1 2")
    for i in range(3):
        row = f"{i} " + " ".join(field[i])
        print(row)

# проверка вин-вин
def check_win(player):
    # строки и столбики
    for i in range(3):
        if all(field[i][j] == player for j in range(3)) or all(field[j][i] == player for j in range(3)):
            return True
    # диагональ
    if all(field[i][i] == player for i in range(3)) or all(field[i][2-i] == player for i in range(3)):
        return True
    return False

# всё поле заполнено?
def is_draw():
    return all(field[i][j] != "-" for i in range(3) for j in range(3))

# сама игра
def play():
    current_player = "x"
    while True:
        print_field()
        print(f"ХОД {current_player}")
        try:
            row = int(input("Строка?"))
            col = int(input("Столбик?"))
        except ValueError:
            print("ЧИСЛО(0-2)")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if field[row][col] == "-":
                field[row][col] = current_player
                if check_win(current_player):
                    print_field()
                    print(f"ПОБЕДА {current_player}!")
                    break
                elif is_draw():
                    print_field()
                    print("дружба?")
                    break
                current_player = "o" if current_player == "x" else "x"
            else:
                print("ЗАНЯТО")
        else:
            print("НЕВЕРНО!")

play()
input("нажми на кнопку и получишь смс (ENTER)")
