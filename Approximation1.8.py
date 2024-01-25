import time
import numpy as np
import matplotlib.pyplot as plt

from scipy import interpolate

cycles = np.array([0.0, 0.05, 0.1, 0.15000000000000002, 0.2, 0.25, 0.30000000000000004, 0.35000000000000003, 0.4, 0.45,
                   0.5, 0.55, 0.6000000000000001, 0.65, 0.7000000000000001,
                   0.75, 0.8, 0.8500000000000001, 0.9, 0.9500000000000001, 1.0, 1.05, 1.1, 1.1500000000000001,
                   1.2000000000000002, 1.25, 1.3, 1.35, 1.4000000000000001, 1.4500000000000002,
                   1.5, 1.55, 1.6, 1.6500000000000001, 1.7000000000000002, 1.75, 1.8, 1.85, 1.9000000000000001,
                   1.9500000000000002, 2.0, 2.0500000000000003, 2.1, 2.15, 2.2, 2.25,
                   2.3000000000000003, 2.35, 2.4000000000000004, 2.45, 2.5, 2.5500000000000003, 2.6, 2.6500000000000004,
                   2.7, 2.75, 2.8000000000000003, 2.85, 2.9000000000000004,
                   2.95, 3.0, 3.0500000000000003, 3.1, 3.1500000000000004, 3.2, 3.25, 3.3000000000000003, 3.35,
                   3.4000000000000004, 3.45, 3.5, 3.5500000000000003, 3.6, 3.6500000000000004,
                   3.7, 3.75, 3.8000000000000003, 3.85, 3.9000000000000004, 3.95, 4.0, 4.05, 4.1000000000000005,
                   4.15, 4.2, 4.25, 4.3, 4.3500000000000005, 4.4, 4.45, 4.5, 4.55,
                   4.6000000000000005, 4.65, 4.7, 4.75, 4.800000000000001, 4.8500000000000005, 4.9, 4.95, 5.0,
                   5.050000000000001, 5.1000000000000005, 5.15, 5.2, 5.25, 5.300000000000001,
                   5.3500000000000005, 5.4, 5.45, 5.5, 5.550000000000001, 5.6000000000000005, 5.65, 5.7, 5.75,
                   5.800000000000001, 5.8500000000000005, 5.9, 5.95, 6.0, 6.050000000000001,
                   6.1000000000000005, 6.15, 6.2, 6.25, 6.300000000000001, 6.3500000000000005, 6.4, 6.45, 6.5,
                   6.550000000000001, 6.6000000000000005, 6.65, 6.7, 6.75, 6.800000000000001,
                   6.8500000000000005, 6.9, 6.95, 7.0, 7.050000000000001, 7.1000000000000005, 7.15, 7.2, 7.25,
                   7.300000000000001, 7.3500000000000005, 7.4, 7.45, 7.5, 7.550000000000001,
                   7.6000000000000005, 7.65, 7.7, 7.75, 7.800000000000001, 7.8500000000000005, 7.9, 7.95, 8.0,
                   8.05, 8.1, 8.15, 8.200000000000001, 8.25, 8.3, 8.35, 8.4, 8.450000000000001,
                   8.5, 8.55, 8.6, 8.65, 8.700000000000001, 8.75, 8.8, 8.85, 8.9, 8.950000000000001, 9.0])
strain = np.array([0.0, 0.0015931005515946695, 0.002626969420715431, 0.003392996590373509, 0.0037496421269588042,
                   0.004142609527270465, 0.0044546743109727975, 0.004575687987183389,
                   0.00441076389030662, 0.003926659950151647, 0.00300593631937947, 0.002222457216953004,
                   0.0017172354932690995, 0.001693675468581628, 0.0016602378519065732, 0.0017684242817978019,
                   0.0019222027085808175, 0.0021367965801760663, 0.0027088195363837693, 0.003599821120436521,
                   0.0046649346675697615, 0.00584382865767251, 0.006636816669969723, 0.007001092593119728,
                   0.007182458505185726, 0.00728487299129515, 0.007388217193554526, 0.007519394638041228,
                   0.007268119261236377, 0.006581232852214352, 0.005569487252408645, 0.0048118710329964785,
                   0.004312099943753125, 0.004173419715196733, 0.004282020003840125, 0.004431761304214034,
                   0.004629577270589714, 0.0048676454425443305, 0.005524241056388413, 0.006516737266718518,
                   0.00784294262815438, 0.008991866483531879, 0.009836179994536879, 0.010382672746197533,
                   0.010758108526127099, 0.010896792759245188, 0.011092022282764534, 0.01119461906849438,
                   0.010927014314355936, 0.010424076082124624, 0.009533432993634154, 0.008686699215708615,
                   0.008140264934374255, 0.00796647293429489, 0.008151908443661529, 0.008393668006257465,
                   0.008572496854705094, 0.00899467467550131, 0.009625244645593832, 0.010593906196435061,
                   0.011963911062539929, 0.013147172159847008, 0.014038310627844016, 0.01457422876246449,
                   0.014785557863819025, 0.015065430183828873, 0.01526438004584017, 0.015321889037238258,
                   0.015055250512777492, 0.01440644273473551, 0.013347521855506025, 0.012471833074867942,
                   0.011987974496790574, 0.011859309700505178, 0.011875099797170953, 0.012055928405862427,
                   0.012123874421731799, 0.012480822605948294, 0.012978930288643019, 0.01394986940237342,
                   0.01515503933344818, 0.016384416732674816, 0.017244663331191824, 0.01772509373595795,
                   0.017881980193494938, 0.0180991256094641, 0.018130345853915594, 0.018212424168978628,
                   0.017936184022854615, 0.01724234058630718, 0.01626143479830862, 0.01528351576832962,
                   0.014759773364209151, 0.01473850964235932, 0.014829623665668631, 0.014914503378904466,
                   0.015183346741320995, 0.015539856641898988, 0.016157954476058563, 0.01711893433207532,
                   0.01837838136451389, 0.01959342620106492, 0.02046934014640669, 0.0209975739132312,
                   0.0213647890110144, 0.02154656339710722, 0.02163958861649217, 0.021540361081742853,
                   0.021252963254688412, 0.02060870508772356, 0.01968512856574165, 0.018674256811274183,
                   0.018156922735509937, 0.01793557042724038, 0.018033401336852314, 0.018137109621919476,
                   0.018262769119208155, 0.01862794364507426, 0.019107364358662296, 0.020182102677863738,
                   0.021406072205626896, 0.022649236926627406, 0.023463916601932047, 0.023954824550666297,
                   0.024126996462173485, 0.024285736310883793, 0.024473140415192413, 0.02452084540514677,
                   0.024222009717739423, 0.023466218147609963, 0.02240376488194954, 0.021516156230548224,
                   0.020964716029353205, 0.02074750460382797, 0.020754592455041767, 0.020954981401062885,
                   0.021131495215883644, 0.02133925161844872, 0.02191516457224103, 0.022879238440760667,
                   0.02420104930417754, 0.02528936672156929, 0.026137406153677566, 0.026669636466778,
                   0.02684288099823083, 0.026933927944623407, 0.027115899418099637, 0.02710447953277464,
                   0.02684256158445943, 0.026096363018378685, 0.024975796821137302, 0.024072101068730048,
                   0.023537795483214333, 0.023321402289031182, 0.023399069027554256, 0.023489081194942692,
                   0.023644540541802563, 0.024021074315761975, 0.02458044816485063, 0.025617453386939437,
                   0.026892940800409746, 0.028176436866647094, 0.029030767260062533, 0.02944685451941927,
                   0.02968532668486119, 0.029804230188804383, 0.02992480472044324, 0.03, 0.02978570590127,
                   0.029093102787865595, 0.028070587710540645, 0.027171168407073797, 0.026607814178127954,
                   0.02636028710353022, 0.0263618442451501, 0.02647758686954176, 0.026664338518962747,
                   0.02687292152983245, 0.02736166092799099, 0.028333467897468063, 0.02951031223280901])

def timer(func):
    def wrapper(*args, **kwargs):
        # start the timer
        start_time = time.time()
        # call the decorated function
        result = func(*args, **kwargs)
        # remeasure the time
        end_time = time.time()
        # compute the elapsed time and print it
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        # return the result of the decorated function execution
        return result
    # return reference to the wrapper function
    return wrapper


@timer
def cyclic_strain_analyzer(x: np.array, y: np.array):
    '''
    .....................
    Функция для  последовательного нахождения максимумов и минимумов,
    интерполировании их линий, нахождения средней линии, нахождения растояния
    от вершин до средней линии и построение графика зависимости расстояния от количества циклов
    :param x:
    :param y:
    :return: np.array(x_max_array_new), np.array(y_max_array_new), np.array(x_min_array_new), np.array(y_min_array_new),
            np.array(x_middle_line_array), np.array(y_middle_line_array), np.array(distance_min),
            np.array(distance_max), maximums,x_points,y_points
    '''

    x = x.tolist()
    y = y.tolist()
    y_max_array = [0]
    x_min_array = [0]
    y_min_array = [0]
    x_max_array = [0]

    #Цикл для нахождения точек минимума и максимума сравнивая текущую точку и четыре предыдущих
    i = 4
    while i < (len(y)):
        if y[i - 3] < y[i - 2] and y[i - 2] > y[i-1]:
            if y[i - 4] < y[i - 3] or y[i - 1] > y[i]:
                y_max_array.append(y[i - 2])
                x_max_array.append(x[i - 2])
        elif y[i - 3] > y[i - 2] and y[i - 2] < y[i-1]:
            if y[i - 4] > y[i - 3] and y[i - 1] < y[i]:
                y_min_array.append(y[i - 2])
                x_min_array.append(x[i - 2])
        elif y[i - 1] == y[i]:
            if y[i - 2] > y[i - 1]:
                y_min_array.append(y[i])
                x_min_array.append(x[i])
            else:
                y_max_array.append(y[i])
                x_max_array.append(x[i])
        i += 1

    # Цикл для удаления точек максимума, если расстояние между ними менее 5 точек.
    # Сравнивается текущее значение с предыдущим
    i = 1
    while i < len(y_max_array):
        if (y.index(y_max_array[i])-y.index(y_max_array[i-1])) < 5:
            if y_max_array[i] > y_max_array[i-1]:
                y_max_array.remove(y_max_array[i-1])
                x_max_array.remove(x_max_array[i-1])
            elif y_max_array[i] < y_max_array[i-1]:
                y_max_array.remove(y_max_array[i])
                x_max_array.remove(x_max_array[i])
        i += 1

    # Цикл для удаления точек минимума, если расстояние между ними менее 5 точек.
    # Сравнивается текущее значение с предыдущим
    i = 1
    while i < len(y_min_array):
        if (y.index(y_min_array[i])-y.index(y_min_array[i-1])) < 5:
            if y_min_array[i] < y_min_array[i-1]:
                y_min_array.remove(y_min_array[i-1])
                x_min_array.remove(x_min_array[i-1])
            elif y_min_array[i] > y_min_array[i-1]:
                y_min_array.remove(y_min_array[i])
                x_min_array.remove(x_min_array[i])
        i+=1

    #Добавление последнего значения исходного массива к линиям максимумов и минимумов
    y_min_array.append(y[- 1])
    x_min_array.append(x[- 1])
    y_max_array.append(y[- 1])
    x_max_array.append(x[- 1])

    #Сортировка по иксу для расстояний от точек минимумов и максимумов до средней линии
    points_minimum = dict(zip(x_min_array, y_min_array))
    points_maximum = dict(zip(x_max_array, y_max_array))
    points_minimum.update(points_maximum)
    points_min_max = dict(sorted(points_minimum.items()))
    x_points = points_min_max.keys()
    y_points = points_min_max.values()

    #Интерполяция линии минимумов
    temp = interpolate.interp1d(x_min_array, y_min_array)
    x_min_array_new = x
    y_min_array_new = temp(x_min_array_new)

    #Интерполяция линии максимумов
    temp = interpolate.interp1d(x_max_array, y_max_array)
    x_max_array_new = x
    y_max_array_new = temp(x_max_array_new)

    @timer
    def surch_middle_line(x_max_array: np.array, y_max_array: np.array, y_min_array: np.array):
        '''
        Функция для нахождения средней линии по середине интерполированных линий максимумов и минимумов
        :param x_max_array:
        :param y_max_array:
        :param y_min_array:
        :return: x_middle_line_array, y_middle_line_array
        '''

        x_middle_line_array = []
        y_middle_line_array = []

        #Нахождение средней линии как половины разницы значений линий минимумов и максимумов по прямой иксов с 0-й позиции
        i = 0
        while i < (len(x_min_array_new)):
            x_middle_line_array.append(x_max_array[i] )
            y_middle_line_array.append((y_max_array[i] + y_min_array[i]) / 2)
            i += 1
        return x_middle_line_array, y_middle_line_array

    x_middle_line_array, y_middle_line_array = surch_middle_line(x_max_array_new,
                                                                 y_max_array_new, y_min_array_new)

    @timer
    def surch_distance_min_max(x_middle_line_array: np.array, y_middle_line_array: np.array, x_min_array: np.array,
                               y_min_array: np.array, y_max_array, x_max_array):
        '''
        Функция для нахождения расстояния от вершин до средней линии
        :param x_middle_line_array:
        :param y_middle_line_array:
        :param x_min_array:
        :param y_min_array:
        :param y_max_array:
        :param x_max_array:
        :return: distance_min, distance_max
        '''
        distance_min = []
        distance_max = []
        distance_comparison_min = []
        distance_comparison_max = []

        #Нахождение расстояния между средней линией и точек минимума по формуле для перпендикуляра от точки до прямой
        #Перебираются для каждой точки значения всей средней линии.Не учитываются добавленные точки начала и конца
        i, k = 1, 0
        while i < (len(y_min_array)-1):
            while k < len(x_middle_line_array):
                distance_comparison_min.append(np.sqrt(
                    (x_min_array[i] - x_middle_line_array[k]) ** 2 + (y_min_array[i] - y_middle_line_array[k]) ** 2))
                k += 1
            k = 0
            i += 1
            distance_min.append(min(distance_comparison_min))
            distance_comparison_min = []

        #Нахождение расстояния между средней линией и точек максимума.Перебираются для каждой точки значения
        #всей средней линии.Не учитываются добавленные точки начала и конца
        i, k = 1, 0
        while i < (len(y_max_array)-1):
            while k < len(x_middle_line_array):
                distance_comparison_max.append(np.sqrt(
                    (x_max_array[i] - x_middle_line_array[k]) ** 2 + (y_max_array[i] - y_middle_line_array[k]) ** 2))
                k += 1
            k = 0
            i += 1
            distance_max.append(min(distance_comparison_max))
            distance_comparison_max = []
        return distance_min, distance_max

    distance_min, distance_max = surch_distance_min_max(x_middle_line_array, y_middle_line_array, x_min_array,
                                                        y_min_array, y_max_array, x_max_array)

    maxX = np.max(x)
    minX = np.min(x)
    maxY = np.max(y)
    minY = np.min(y)

    maximums = {'maxX': maxX, 'minX': minX, 'maxY': maxY, 'minY': minY}
    return (np.array(x_max_array_new), np.array(y_max_array_new), np.array(x_min_array_new), np.array(y_min_array_new),
            np.array(x_middle_line_array), np.array(y_middle_line_array), np.array(distance_min),
            np.array(distance_max), maximums,x_points,y_points)


if __name__ == "__main__":
    plt.style.use('bmh')
    (x_max_array, y_max_array, x_min_array, y_min_array, x_middle_line_array, y_middle_line_array, distance_min,
     distance_max, maximums,x_points,y_points) = cyclic_strain_analyzer(cycles, strain)

    plt.plot(x_points,y_points,color='orange')
    plt.ylabel('ε')
    plt.xlabel('τ')
    plt.title('График отклонений')
    plt.legend()
    plt.show()

    plt.plot(x_middle_line_array, y_middle_line_array, label='средняя линия')
    plt.ylabel('ε')
    plt.xlabel('τ')
    plt.plot(x_min_array, y_min_array, linewidth=1, linestyle='dashed', label='линия минимумов')
    plt.plot(x_max_array, y_max_array, linewidth=1, linestyle='dashed', label='линия максимумов')
    plt.plot(cycles, strain)
    plt.legend()
    plt.show()
