# Напишите программу, которая принимает на вход координаты точки (X,Y), причем X!=0 и Y!=0,
# и выдает номер четверти плоскости, в которой находится эта точка
#  (или на какой оси она находится)

x = int (input ('Введите координату x - '))
print (x)
y = int (input ('Введите координату y - '))
print (y)
if x > 0 and y > 0:
    print ('Точка находится в 1-й четверти')
elif x < 0 and y > 0:
    print ('Точка находится во 2-й четверти')
elif x < 0 and y < 0:
    print ('Точка находится в 3-й четверти')
elif x > 0 and y < 0:
    print ('Точка находится в 4-й четверти')
elif x == 0:
    print ('Точка лежит на оси Y')
elif y == 0:
    print ('Точка лежит на оси X')