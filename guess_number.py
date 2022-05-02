import random

num = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку\nВведите число от 1 до 100:')


def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100


def is_valid_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def compare_digits():
    count = 0
    while True:
        n = is_valid_num()
        if n < num:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            count += 1
            print('Вы угадали, поздравляем!')
            break
    print('Ваше число попыток:', count)
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    print('Вы бы хотели сыграть еще?\nВведите Y/N')
    answer = input()
    if answer == 'Y':
        print('Тогда нужно бы ввести новое число, бро!')
        return compare_digits()


compare_digits()

'''
Как бы можно было улучшить игру?
1. Вынести в функцию некоторые принты и условия из compare_digits()
2. Осмысленное название переменных!!! Иначе гг вп через месяц
'''