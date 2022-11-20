"""
Задача 9. Крестики-нолики
Что нужно сделать
Напишите программу, которая реализует игру «Крестики-нолики». Да, это всё условие задачи.
Ваши классы в этой задаче могут выглядеть так:

class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки

class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки

class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
"""

class Cell:
    pass

class Board:
    board_list = range(1, 10)
    pass

class Player:
    def __init__(self, name, simbol):
        self.name = name
        self.simbol = simbol

def main():
    user_1 = Player('Игорь', 'X')
    user_2 = Player('Олеся', 'O')
    valid = False
    while not valid:


main()


# def graw_board(board):
#     print('-' * 13)
#     for i in range(3):
#         print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
#         print('-' * 13)
#
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = int(input('Куда поставить {}?'.format(player_token)))
#         try:
#             player_answer = int(player_token)
#         except:
#             print('Не корректный ввод. Вы уверены что ввели число?')
#         if 1 <= int(player_answer) <= 9:
#             if str(board[player_answer - 1]) not in "XO":
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print('Эта клетка занята.')
#         else:
#             print('Ошибка вы вышли за диапазон от 1 до 9')
#
#
# def chek_win(board):
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 5, 6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         graw_board(board)
#         if counter % 2 == 0:
#             take_input('X')
#         else:
#             take_input('O')
#         counter += 1
#         if counter > 4:
#             tm = chek_win(board)
#             if tm:
#                 print('{} Победил!!!'.format(tm))
#                 win = True
#                 break
#         if counter == 9:
#             print('Ничья.')
#             break
#     graw_board(board)
#
#
#
# board = range(1, 10)
# main(board)