import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Union
from scipy import interpolate
from scipy.interpolate import CubicSpline

cycles = np.array([0.0, 0.05, 0.1, 0.15000000000000002, 0.2, 0.25, 0.30000000000000004, 0.35000000000000003, 0.4, 0.45, 0.5, 0.55, 0.6000000000000001, 0.65, 0.7000000000000001, 0.75, 0.8, 0.8500000000000001, 0.9, 0.9500000000000001, 1.0, 1.05, 1.1, 1.1500000000000001, 1.2000000000000002, 1.25, 1.3, 1.35, 1.4000000000000001, 1.4500000000000002, 1.5, 1.55, 1.6, 1.6500000000000001, 1.7000000000000002, 1.75, 1.8, 1.85, 1.9000000000000001, 1.9500000000000002, 2.0, 2.0500000000000003, 2.1, 2.15, 2.2, 2.25, 2.3000000000000003, 2.35, 2.4000000000000004, 2.45, 2.5, 2.5500000000000003, 2.6, 2.6500000000000004, 2.7, 2.75, 2.8000000000000003, 2.85, 2.9000000000000004, 2.95, 3.0, 3.0500000000000003, 3.1, 3.1500000000000004, 3.2, 3.25, 3.3000000000000003, 3.35, 3.4000000000000004, 3.45, 3.5, 3.5500000000000003, 3.6, 3.6500000000000004, 3.7, 3.75, 3.8000000000000003, 3.85, 3.9000000000000004, 3.95, 4.0, 4.05, 4.1000000000000005, 4.15, 4.2, 4.25, 4.3, 4.3500000000000005, 4.4, 4.45, 4.5, 4.55, 4.6000000000000005, 4.65, 4.7, 4.75, 4.800000000000001, 4.8500000000000005, 4.9, 4.95, 5.0, 5.050000000000001, 5.1000000000000005, 5.15, 5.2, 5.25, 5.300000000000001, 5.3500000000000005, 5.4, 5.45, 5.5, 5.550000000000001, 5.6000000000000005, 5.65, 5.7, 5.75, 5.800000000000001, 5.8500000000000005, 5.9, 5.95, 6.0, 6.050000000000001, 6.1000000000000005, 6.15, 6.2, 6.25, 6.300000000000001, 6.3500000000000005, 6.4, 6.45, 6.5, 6.550000000000001, 6.6000000000000005, 6.65, 6.7, 6.75, 6.800000000000001, 6.8500000000000005, 6.9, 6.95, 7.0, 7.050000000000001, 7.1000000000000005, 7.15, 7.2, 7.25, 7.300000000000001, 7.3500000000000005, 7.4, 7.45, 7.5, 7.550000000000001, 7.6000000000000005, 7.65, 7.7, 7.75, 7.800000000000001, 7.8500000000000005, 7.9, 7.95, 8.0, 8.05, 8.1, 8.15, 8.200000000000001, 8.25, 8.3, 8.35, 8.4, 8.450000000000001, 8.5, 8.55, 8.6, 8.65, 8.700000000000001, 8.75, 8.8, 8.85, 8.9, 8.950000000000001, 9.0])
strain = np.array([0.0, 0.002704122622613223, 0.004734273950460789, 0.00622620278775675, 0.0076184477710014116, 0.008643263380171011, 0.009639544651561126, 0.010467619284694864, 0.010955336576356955, 0.011058967095125884, 0.010864495326967477, 0.010561798531001108, 0.010727148636544052, 0.011036309406619224, 0.011434208647091314, 0.012007184133876104, 0.012659760801444498, 0.013269973105117861, 0.014180250994300975, 0.01544839391495469, 0.016862874851992317, 0.018292722676501432, 0.019234686775335214, 0.019971687091059148, 0.02052007144003864, 0.02094274992387366, 0.021367617400868996, 0.021594004672883513, 0.021607603565702713, 0.021272318543976203, 0.02072422895133621, 0.020142386719152063, 0.019915074931114846, 0.019858361538279433, 0.02015801832847817, 0.020509173794649498, 0.02090114263266841, 0.021331375250265943, 0.021963216861956774, 0.023111559042122642, 0.024307675759812273, 0.02556382877593762, 0.026571783950044024, 0.027098045315881152, 0.02747267271895797, 0.027756472071979486, 0.027955956887925414, 0.02791502583664775, 0.027743429427405326, 0.027262736709690812, 0.02634421199765562, 0.025520796324368652, 0.02506026951778535, 0.024848904448737153, 0.024928872631187697, 0.024962157703566627, 0.025142744130579448, 0.025333795609878838, 0.025821297320015382, 0.02660886258990591, 0.027786646671293158, 0.02892109141402685, 0.029628707044876936, 0.0299715173310774, 0.030129617665850743, 0.030295443320214336, 0.0304697848474464, 0.030428013430772366, 0.030241999293334116, 0.02953840418678355, 0.02869226707165212, 0.027918070115178877, 0.027590627717063096, 0.027500441513746886, 0.027610673257192676, 0.027914916150470002, 0.028290287625280183, 0.028695161273199064, 0.029417684972393082, 0.030454414040791713, 0.03174393866605677, 0.03306476317524391, 0.03397276268826185, 0.03448288610037643, 0.034840701275316355, 0.03521995753059717, 0.03539512868669923, 0.03543590058029312, 0.035135023579571, 0.034620851738086246, 0.033712161811249114, 0.032808702981413494, 0.03233001428811974, 0.03218698243203419, 0.03216248241466634, 0.032199841144536674, 0.032279284887997015, 0.032504610611197755, 0.03303005320741395, 0.03376196443070642, 0.03493866217804204, 0.035904490252353816, 0.036573614212116835, 0.03679946679349178, 0.03684579643820628, 0.03682577663592072, 0.036838878157854846, 0.036656474755420373, 0.0362337882154723, 0.035528129717760655, 0.034474628627178656, 0.03342232785170879, 0.032702577213590614, 0.032277508073497274, 0.03217037579379166, 0.0321790569827157, 0.03234681637757348, 0.032654183167254026, 0.03333160853391649, 0.034404478658212126, 0.03591733244632587, 0.03725787371141187, 0.03802619554276893, 0.03858660061710526, 0.038801983840053136, 0.03899641111314876, 0.03915162439696928, 0.03917805524016007, 0.038839333497681455, 0.038091723497983725, 0.03677106599502913, 0.03537922429150447, 0.03444948822231235, 0.03394578481780496, 0.03372631888461875, 0.0336495326650896, 0.033766007766253735, 0.034208736698422525, 0.03511182245396142, 0.03665867516887857, 0.03853144758650144, 0.040051587832002786, 0.04104016325059531, 0.04145162949798616, 0.04165721896829568, 0.04182796628397439, 0.0418347391148033, 0.04187834298139835, 0.04154575073628246, 0.04037056868887528, 0.03863125036581041, 0.036506235499492494, 0.03485719951735901, 0.03386951654646701, 0.03337944011239035, 0.03322326890030695, 0.03337032246938981, 0.03395134238612487, 0.035169153238588234, 0.03736690689892474, 0.039946189337542085, 0.04211740746225751, 0.04325429881012174, 0.04371750960549295, 0.04382443408605796, 0.04380721492492266, 0.044, 0.043978306519364664, 0.04353547924142668, 0.04213151539083622, 0.03959909690853221, 0.036747573140625024, 0.03446885095745565, 0.0331749739026295, 0.032590702105408924, 0.03235205524754297, 0.032658317394594176, 0.0334726743141317, 0.03533803578380648, 0.038232109169101254, 0.04120883376183204])

@dataclass
class Line:
    x: Union[np.array, list] = None
    y: Union[np.array, list] = None

@dataclass
class MinMaxProcessing:
    max_points: Line = None     # точки максимумов
    min_points: Line = None     # точки минимумов
    max_line: Line = None       # линия максимумов
    min_line: Line = None       # линия минимумов
    middle_line: Line = None    # средняя линяя
    distance_line: Line = None  # линия удаления максимумов и минимумов от средней линии
    distance_min: list = None,
    distance_max: list = None,
    maximums: dict = None

def min_max_analyzer(x: np.array, y: np.array) -> MinMaxProcessing:
    """
    .....................
    Функция для  последовательного нахождения максимумов и минимумов,
    интерполировании их линий, нахождения средней линии, нахождения растояния
    от вершин до средней линии и построение графика зависимости расстояния от количества циклов
    :param x:
    :param y:
    :return: np.array(x_max_array_new), np.array(y_max_array_new), np.array(x_min_array_new), np.array(y_min_array_new),
            np.array(x_middle_line_array), np.array(y_middle_line_array), np.array(distance_min),
            np.array(distance_max), maximums,x_points,y_points
    """
    #применяем кубически сплайн для  последующего нахождения знаков производной
    cs = CubicSpline(x, y)
    y = y.tolist()
    x = x.tolist()
    m = cs(x, 1)
    k = m.tolist()

    y_max_array = [0]
    x_min_array = [0]
    y_min_array = [0]
    x_max_array = [0]
    # Находим точку изменения знака производной, сравнивая текущее значение с предыдущим
    i = 1
    while i < len(k):
        if k[i - 1] > 0 and k[i] < 0:
            if y[i - 1] > y[i]:
                y_max_array.append(y[i - 1])
                x_max_array.append(x[i - 1])
            elif y[i - 1] < y[i]:
                y_max_array.append(y[i])
                x_max_array.append(x[i])
        elif k[i - 1] < 0 and k[i] > 0:
            if y[i - 1] < y[i]:
                y_min_array.append(y[i - 1])
                x_min_array.append(x[i - 1])
            elif y[i - 1] > y[i]:
                y_min_array.append(y[i])
                x_min_array.append(x[i])
        i += 1
    # Цикл для удаления точек максимума, если расстояние между ними менее 5 точек.
    # Сравнивается текущее значение с предыдущим
    i = 2
    while i < len(y_max_array):
        if (y.index(y_max_array[i]) - y.index(y_max_array[i - 1])) < 5:
            if y_max_array[i] > y_max_array[i - 1]:
                y_max_array.remove(y_max_array[i - 1])
                x_max_array.remove(x_max_array[i - 1])
            elif y_max_array[i] < y_max_array[i - 1]:
                y_max_array.remove(y_max_array[i])
                x_max_array.remove(x_max_array[i])
        i += 1
    # Цикл для удаления точек минимума, если расстояние между ними менее 5 точек.
    # Сравнивается текущее значение с предыдущим
    i = 2
    while i < len(y_min_array):
       if (y.index(y_min_array[i]) - y.index(y_min_array[i - 1])) < 5:
            if y_min_array[i] < y_min_array[i - 1]:
                y_min_array.remove(y_min_array[i])
                x_min_array.remove(x_min_array[i])
            elif y_min_array[i] > y_min_array[i - 1]:
                y_min_array.remove(y_min_array[i - 1])
                x_min_array.remove(x_min_array[i - 1])
       i += 1
    # Цикл для удаления точек минимума и минимума, если расстояние между ними менее 3 точек.
    # Сравнивается текущее значение с предыдущим
    i = 2
    while i < len(y_min_array):
        if (y.index(y_min_array[i]) - y.index(y_max_array[i])) < 3:
            if y_max_array[i] < y_max_array[i - 1]:
                y_max_array.remove(y_max_array[i])
                x_max_array.remove(x_max_array[i])
            elif y_max_array[i] > y_min_array[i - 1]:
                y_min_array.remove(y_min_array[i])
                x_min_array.remove(x_min_array[i])
        elif (y.index(y_min_array[i]) - y.index(y_max_array[i - 1])) < 3:
            if y_min_array[i] < y_min_array[i - 1]:
                y_min_array.remove(y_min_array[i - 1])
                x_min_array.remove(x_min_array[i - 1])
            elif y_min_array[i] > y_min_array[i - 1]:
                y_min_array.remove(y_min_array[i])
                x_min_array.remove(x_min_array[i])

        i += 1
    # Добавление последнего значения исходного массива к линиям максимумов и минимумов
    y_min_array.append(y[- 1])
    x_min_array.append(x[- 1])
    y_max_array.append(y[- 1])
    x_max_array.append(x[- 1])
    print(len(x_min_array))
    print(len(x_max_array))

    # Интерполяция линии минимумов
    temp = interpolate.interp1d(x_min_array, y_min_array)
    x_min_array_line = x
    y_min_array_line = temp(x_min_array_line)

    # Интерполяция линии максимумов
    temp = interpolate.interp1d(x_max_array, y_max_array)
    x_max_array_line = x
    y_max_array_line = temp(x_max_array_line)

    x_middle_line_array = []
    y_middle_line_array = []

    # Нахождение средней линии как половины разницы значений линий минимумов и максимумов по прямой иксов с
    # 0-й позиции
    i = 0
    while i < (len(x_min_array_line)):
        x_middle_line_array.append(x_max_array_line[i])
        y_middle_line_array.append((y_max_array_line[i] + y_min_array_line[i]) / 2)
        i += 1

    def surch_distance_min_max(x_middle_line_array: list, y_middle_line_array: list, x_min_array: list,
                               y_min_array: list, y_max_array, x_max_array: list):
        """
        Функция для нахождения расстояния от вершин до средней линии и его сортировка по иксу
        :param x_middle_line_array: значения по иксу для средней линии
        :param y_middle_line_array: значения по иреку для средней линии
        :param x_min_array: значения по иксу для линии минимумов
        :param y_min_array: значения по игреку для линии минимумов
        :param y_max_array:  значения по игреку для линии максимумов
        :param x_max_array: значения по игреку для линии максимумов
        :return: distance_min, distance_max
        """
        distance_min = []
        distance_max = []
        distance_comparison_min = []
        distance_comparison_max = []

        # Нахождение расстояния между средней линией и точек минимума по формуле для перпендикуляра от точки до прямой
        # Перебираются для каждой точки значения всей средней линии.Не учитываются добавленные точки начала и конца
        i, k = 1, 0
        while i < (len(y_min_array) - 1):
            while k < len(x_middle_line_array):
                distance_comparison_min.append(np.sqrt(
                    (x_min_array[i] - x_middle_line_array[k]) ** 2 + (y_min_array[i] - y_middle_line_array[k]) ** 2))
                k += 1
            k = 0
            i += 1
            distance_min.append(min(distance_comparison_min))
            distance_comparison_min = []

        # Нахождение расстояния между средней линией и точек максимума.Перебираются для каждой точки значения
        # всей средней линии.Не учитываются добавленные точки начала и конца
        i, k = 1, 0
        while i < (len(y_max_array) - 1):
            while k < len(x_middle_line_array):
                distance_comparison_max.append(np.sqrt(
                    (x_max_array[i] - x_middle_line_array[k]) ** 2 + (y_max_array[i] - y_middle_line_array[k]) ** 2))
                k += 1
            k = 0
            i += 1
            distance_max.append(min(distance_comparison_max))
            distance_comparison_max = []

        # Сортировка по иксу для расстояний от точек минимумов и максимумов до средней линии
        points_minimum = dict(zip(x_min_array, distance_max))
        points_maximum = dict(zip(x_max_array, distance_min))
        points_minimum.update(points_maximum)
        points_min_max = dict(sorted(points_minimum.items()))
        x_points = points_min_max.keys()
        y_points = points_min_max.values()

        return distance_min, distance_max, x_points, y_points

    distance_min, distance_max, x_points, y_points = surch_distance_min_max(x_middle_line_array, y_middle_line_array,
                                                                            x_min_array,
                                                                            y_min_array, y_max_array, x_max_array)
    max_x = np.max(x)
    min_x = np.min(x)
    max_y = np.max(y)
    min_y = np.min(y)

    maximums = {'maxX': max_x, 'minX': min_x, 'maxY': max_y, 'minY': min_y}

    return MinMaxProcessing(
        max_points=Line(
            x=x_max_array,
            y=y_max_array
        ),
        min_points=Line(
            x=x_min_array,
            y=y_min_array
        ),
        max_line=Line(
            x=x_max_array_line,
            y=y_max_array_line
        ),
        min_line=Line(
            x=x_min_array_line,
            y=y_min_array_line
        ),
        middle_line=Line(
                x=x_middle_line_array,
                y=y_middle_line_array
            ),
        distance_line=Line(
                x=list(x_points),
                y=list(y_points)
            ),
        distance_min=distance_min,
        distance_max=distance_max,
        maximums=maximums

    )



if __name__ == "__main__":
    plt.style.use('bmh')
    MinMaxProcessing = min_max_analyzer(cycles, strain)

    plt.plot(MinMaxProcessing.middle_line.x, MinMaxProcessing.middle_line.y, label='средняя линия')
    plt.ylabel('ε')
    plt.xlabel('τ')
    plt.plot(MinMaxProcessing.min_points.x, MinMaxProcessing.min_points.y, 'o')
    plt.plot(MinMaxProcessing.max_points.x, MinMaxProcessing.max_points.y, 'o')
    plt.plot(MinMaxProcessing.min_line.x, MinMaxProcessing.min_line.y, linewidth=1, linestyle='dashed', label='линия минимумов')
    plt.plot(MinMaxProcessing.max_line.x, MinMaxProcessing.max_line.y, linewidth=1, linestyle='dashed', label='линия максимумов')
    plt.plot(cycles, strain)

    plt.legend()
    plt.show()

    plt.plot(MinMaxProcessing.distance_line.x, MinMaxProcessing.distance_line.y, color='orange')
    plt.ylabel('ε')
    plt.xlabel('τ')
    plt.title('График отклонений')
    plt.show()
