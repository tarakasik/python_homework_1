'''Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''
print('Input x');
x = int(input())
print('Input y');
y = int(input())

if x == 0 or y == 0:
    print('On the plane')

elif x > 0 and y > 0:
    print(f'[{x},{y}] -> First quarter')

elif x < 0 and y > 0:
    print(f'[{x},{y}] -> Second quarter')

elif x < 0 and y < 0:
    print(f'[{x},{y}] -> Third quarter')

else:
    print(f'[{x},{y}] -> Forth quarter')