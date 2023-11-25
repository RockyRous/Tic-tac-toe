# map = [' ' for a in range(1,10)] # Создаем карту для игры (9 ячеек)
win_map = [  # Победные комбинации
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]


def print_map(map) -> None:
    """ Функция печати карты игры """
    print(
        f'\nНомера ячеек указаны справа\n'
        f' {map[0]} | {map[1]} | {map[2]}  ==   1 | 2 | 3\n'
        f' {map[3]} | {map[4]} | {map[5]}  ==   4 | 5 | 6\n'
        f' {map[6]} | {map[7]} | {map[8]}  ==   7 | 8 | 9\n'
          )


def step(num_map: int, symbol: str, map: list[str]) -> None:
    """ Функция хода игрока """
    map[num_map] = symbol


def new_game_or_exit():
    """ Начать новую игру или выйти """
    a = input(f'Начать новую игру? (Y/N): ')
    a.lower()
    if a == 'y':
        main()


def win_or_not(map: list[str], symbol: str) -> bool:
    """ Проверяем наличие выигрышных комбинаций на поле """
    for i in win_map:
        if any([
            all([map[i[0]] == "X",
                 map[i[1]] == "X",
                 map[i[2]] == "X"]),
            all([map[i[0]] == "O",
                 map[i[1]] == "O",
                 map[i[2]] == "O"])
        ]):
            map[i[0]] = f'={symbol}'  # Стильное выделение победителя
            map[i[1]] = f'={symbol}'
            map[i[2]] = f'={symbol}'

            print_map(map)
            print(f'Победил игрок с символом {symbol}. Поздравляем!')
            return True

    return False


def main():
    # Тут будет сообщение о начале новой игры
    map = [' ' for a in range(1, 10)]  # Создаем новую карту для игры (9 ячеек)
    iter_game = 0
    symbol = "X"  # Символ первого игрока

    while True:  # Цикл игры
        print_map(map)  # Показываем поле (пустое)
        iter_game += 1
        if iter_game == 10:
            print(f'Ходы кончились, Ничья!')
            new_game_or_exit()
            break  # Выход

        input_ = True

        while input_:  # Ввод хода
            try:
                num_map = int(input(f'Игрок с символом {symbol}, введите номер ячейки для вашего хода: '))
                num_map -= 1  # Сразу конвентируем в id
            except:
                num_map = -1

            # Проверка на валидность введенных данных
            if -1 < num_map < 9:
                if all([
                    map[num_map] != 'X',
                    map[num_map] != 'O'
                ]):
                    step(num_map, symbol, map)
                    input_ = False
                else:
                    print(f'Эта ячейка уже занята... Попробуйте еще раз.')
            else:
                print(f'Вы ввели цифру вне диапазона ячеек... Попробуйте еще раз.')

        if win_or_not(map, symbol):
            break

        if symbol == "X":  # Меняем символ игрока
            symbol = "O"
        else:
            symbol = "X"


if __name__ == '__main__':
    # Тут будет приветствие в программе
    # Тут будет инструкция к игре
    main()

