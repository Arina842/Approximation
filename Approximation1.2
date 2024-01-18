import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from random import randint
from scipy import interpolate
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution



cycles = np.arange(0, 45.0, 0.5)
strain = np.array([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 10, 9, 8, 7, 6, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 14,
           13, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23, 22, 21, 20, 19, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 29, 28, 27, 26, 25, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 39, 38, 37, 36, 35],int)
# # strain = [0]
# # for i in range(29):
# #     strain.append(randint(1, 10))
# print(strain)

#




def cyclic_strain_analyzer(cycles: np.array, strain: np.array) -> dict:
    '''
    Функция для обработки кривой деформаций при динамическом нагружении
    :param cycles: массив циклов нагружения
    :param strain: массив деформации
    :return: результаты обработки
    '''
    y_max_array, y_min_array, x_max_array, x_min_array,x_middle_line_new,y_middle_line_new = min_max_search(cycles, strain)
    distance_min, distance_max = finding_distance(x_middle_line_new, y_middle_line_new, y_min_array, x_min_array, y_max_array, x_max_array)
    print(distance_min)
    print(distance_max)
    creating_curves(y_max_array, y_min_array, x_max_array, x_min_array)








def creating_curves(y_max_array, y_min_array, x_max_array, x_min_array):
    plt.style.use('bmh')
    plt.plot(cycles, strain)
    plt.plot(x_min_array, y_min_array, linewidth=1, linestyle='dashed', marker='o',
             label='минимумы')
    plt.plot(x_max_array, y_max_array, linewidth=1, linestyle='dashed', marker='o',
             label='максимумы')

    plt.legend()
    plt.show()
def min_max_search(x: np.array, y: np.array) -> dict:
    '''
    .....................
    :param x: cycles
    :param y: strain
    :return: y_max_array, y_min_array, x_max_array, x_min_array
    '''
    y_max_array = [0]
    x_min_array = [0]
    y_min_array = [0]
    x_max_array = [0]
    # ищем минимумы и максимумы начиная с 3 точки,проверяя две предыдущие и одну текущую
    i = 2
    x_middle_line_first = []
    y_middle_line_first = []
    while i < (len(strain)):
        if strain[i - 2] < strain[i - 1] and strain[i - 1] > strain[i]:
            y_max_array.append(strain[i - 1])
            x_max_array.append(cycles[i - 1])
            x_middle_line_first.append(cycles[i - 1])
            y_middle_line_first.append(strain[i - 1])
        elif strain[i - 2] > strain[i - 1] and strain[i - 1] < strain[i]:
            y_min_array.append(strain[i - 1])
            x_min_array.append(cycles[i - 1])
            x_middle_line_first.append(cycles[i - 1])
            y_middle_line_first.append(strain[i - 1])
        elif strain[i - 1] == strain[i]:  # если значения совпадают, берём первое вхождение
            if strain[i - 2] > strain[i - 1]:
                y_min_array.append(strain[i - 1])
                x_min_array.append(cycles[i - 1])
                x_middle_line_first.append(cycles[i - 1])
                y_middle_line_first.append(strain[i - 1])
            else:
                y_max_array.append(strain[i - 1])
                x_max_array.append(cycles[i - 1])
                x_middle_line_first.append(cycles[i - 1])
                y_middle_line_first.append(strain[i - 1])
        i += 1


    y_min_array.append(strain[i - 1])
    x_min_array.append(cycles[i - 1])

    y_max_array.append(strain[i - 1])
    x_max_array.append(cycles[i - 1])

    x_middle_line = [0]
    y_middle_line = [0]
    i=1

    while i < (len(x_middle_line_first)-2):

        if i >= 2:
            x_middle_line.append((x_middle_line_first[i]))
            y_middle_line.append((y_middle_line_first[i] + y_middle_line_first[i + 1] + y_middle_line_first[i + 2]) / 4)
        elif i == 0:
            x_middle_line.append(x_middle_line_first[i])
            y_middle_line.append((y_middle_line_first[i] + y_middle_line_first[i + 1]))
        elif i == 1:
            x_middle_line.append(x_middle_line_first[i])
            print((y_middle_line_first[i] + y_middle_line_first[i - 1]) / 2)
            y_middle_line.append((y_middle_line_first[i] + y_middle_line_first[i + 1]) / 2)


        i+=1
    y_middle_line.append((strain[- 1]+strain[- 2]) / 2)
    x_middle_line.append((cycles[- 1]))
    print(x_middle_line_first, y_middle_line_first)
    print(x_middle_line, y_middle_line)
    plt.plot(x_middle_line, y_middle_line)

    temp = interpolate.interp1d(x_middle_line, y_middle_line)
    x_middle_line_new = cycles

    y_middle_line_new = temp(x_middle_line_new)

    plt.plot(x_middle_line_new, y_middle_line_new, '--')
    print(len(y_min_array))

    maxX = np.max(x)
    minX = np.min(x)
    maxY = np.max(y)
    minY = np.min(y)
    print('maxX =', maxX, 'maxY =', maxY, 'minX =', minX, 'minY =', minY)
    return y_max_array, y_min_array, x_max_array, x_min_array,x_middle_line_new,y_middle_line_new,y_min_array,x_min_array
def finding_distance(x_middle_line_new,y_middle_line_new,y_min_array,x_min_array,y_max_array,x_max_array):
    distance_min = []
    distance_max = []
    distance_comparison_min = []
    distance_comparison_max = []
    i, k = 0, 0
    while i < len(y_min_array):
        while k < len(x_middle_line_new):
            distance_comparison_min.append(np.sqrt((x_min_array[i]-x_middle_line_new[k])**2+(y_min_array[i]-y_middle_line_new[k])**2))
            k += 1
        k = 0
        i += 1
        distance_min.append(min(distance_comparison_min))
        distance_comparison_min = []

    i, k = 0, 0
    while i < len(y_max_array):
        while k < len(x_middle_line_new):
            distance_comparison_max.append(np.sqrt((x_max_array[i] - x_middle_line_new[k]) ** 2 + (y_max_array[i] - y_middle_line_new[k]) ** 2))
            k += 1
        k = 0
        i += 1
        distance_max.append(min(distance_comparison_max))
        distance_comparison_max = []
    return distance_min, distance_max





if __name__ == "__main__":
    cyclic_strain_analyzer(cycles, strain)




