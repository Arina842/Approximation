import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint

cycles = np.arange(0, 9, 0.1)
strain = np.array([0, 1, 2, 3,4, 5, 6, 7, 8, 9,10, 11,11, 10, 9, 8, 7, 6, 5,5, 6, 7, 8, 9,10, 11,12,13,14,15,15,14,
          13, 12 ,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23, 22,21,20,19,18,19,20,21,22,23,24,25,26,27,28,29,30,29,28,27,26,25,24,25,26,
            27,28,29,30,31,32,33,34,35,36,37,38,39,40,39,38,37,36,35],int)

def cyclic_strain_analyzer(cycles: np.array, strain: np.array) -> dict:
    '''
    Функция для обработки кривой деформаций при динамическом нагружении
    :param cycles: массив циклов нагружения
    :param strain: массив деформации
    :return: результаты обработки
    '''

    y_max_array, y_min_array, x_max_array, x_min_array = min_max_search(cycles, strain)
    creating_curves(y_max_array, y_min_array, x_max_array, x_min_array)
def creating_curves(y_max_array, y_min_array, x_max_array, x_min_array):
    plt.style.use('bmh')
    plt.plot(x_min_array, y_min_array, linewidth=1, linestyle='dashed', marker='o',
             label='минимумы')  # строим графики минимумов
    plt.plot(x_max_array, y_max_array, linewidth=1, linestyle='dashed', marker='o',
             label='максимумы')  # строим графики максимумов
    plt.plot(cycles, strain)
    plt.legend()
    plt.show()
def min_max_search(x: np.array, y: np.array) -> dict:
    '''
    .....................
    :param x:
    :param y:
    :return:
    '''
    print(strain)
    y_max_array = [0]
    x_min_array = [0]
    y_min_array = [0]
    x_max_array = [0]
    # ищем минимумы и максимумы начиная с 3 точки,проверяя две предыдущие и одну текущую
    i = 2
    while i < (len(strain)):
        if strain[i - 2] < strain[i - 1] and strain[i - 1] > strain[i]:
            y_max_array.append(strain[i - 1])
            x_max_array.append(cycles[i - 1])
        elif strain[i - 2] > strain[i - 1] and strain[i - 1] < strain[i]:
            y_min_array.append(strain[i - 1])
            x_min_array.append(cycles[i - 1])
        elif strain[i - 1] == strain[i]:  # если значения совпадают, берём первое вхождение
            if strain[i - 2] > strain[i - 1]:
                y_min_array.append(strain[i - 1])
                x_min_array.append(cycles[i - 1])
            else:
                y_max_array.append(strain[i - 1])
                x_max_array.append(cycles[i - 1])
        i += 1

    y_min_array.append(strain[i - 1])
    x_min_array.append(cycles[i - 1])

    y_max_array.append(strain[i - 1])
    x_max_array.append(cycles[i - 1])


    maxX = np.max(x)
    minX = np.min(x)
    maxY = np.max(y)
    minY = np.min(y)
    print('maxX =', maxX, 'maxY =', maxY, 'minX =', minX, 'minY =', minY)
    return y_max_array, y_min_array, x_max_array, x_min_array

if __name__ == "__main__":
    cyclic_strain_analyzer(cycles,np.array)



