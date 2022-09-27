'''
Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).
'''
q = int(input('Input quarter \n'))

if q == 1:
    print('x = from 0 to plus infinity, y = from 0 to plus infinity')
elif q == 2:
    print('x = from minus infinity to 0, y = from 0 to plus infinity')
elif q == 3:
    print('x = from 0 to minus infinity, y = from 0 to minus infinity')
elif q == 4:
    print('x = from 0 to plus infinity,y = from 0 to minus infinity')
else:
    print('Wrong number of quarter')