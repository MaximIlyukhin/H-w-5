# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint
n = randint(100,1000)
print(f'Число конфет равно {n}')
num_player_1 = randint(1,2)
print(f'Первым ходит игрок №{num_player_1}')
if num_player_1 == 1:
    num_player_2 = 2
else:
    num_player_2 = 1
c = 0
while n>1:
    while True:
        a = int(input(f'Игрок №{num_player_1} введите число: '))
        if a>28 or a<1:
            print(f'Введите число меньше 29')
            continue
        else:
            break
    n-=a
    print(f'Число конфет равно {n}')
    c+=1
    if n<2:
        print(f'Победил игрок №{num_player_1}')
        break
    else:
        while True:
            b = int(input(f'Игрок №{num_player_2} введите число: '))
            if b>28 or b<1:
                print(f'Введите число меньше 29')
                continue
            else:
                break
        n-=b
        print(f'Число конфет равно {n}')
        c+=1
else:
    print(f'Победил игрок №{num_player_2}')


        