'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''
a = int(input('Input day of week \n'))

if a <= 7 and a >= 6:
    print(f'{a} -> This weekend')
elif a > 0 and a <= 5:
    print(f'{a} -> This a workday')
else:
    print(f'{a} -> Wrong day week')