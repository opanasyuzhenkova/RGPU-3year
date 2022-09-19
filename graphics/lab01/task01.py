import numpy as np
import pprint as pprn

x_coord_lst = list()
print('Введите координаты двухмерного вектора: ')
x_coord_lst = [float(input(f"Координата номер {i + 1} : ")) for i in range(2)]
# print(x_coord_lst)

x = np.array(x_coord_lst)
print('Массив координат точки Х: ', x)

t = np.array([[1, 3], [4, 1]])
print('Матрица преобразования T = ', end = '')
pprn.pprint(t)

x_new = x@t
print('Новые координаты точки X: ', end = '')
pprn.pprint(x_new)