from math import acos, degrees, sqrt, sin

def side(point_x_1, point_y_1, point_x_2, point_y_2):
    side = sqrt(((point_x_1 - point_x_2) ** 2) + ((point_y_1 - point_y_2) ** 2))
    return side

def perimeter_t(side1, side2, side3):
    return float((side1+side2+side3))

def perimeter_e(side1, side2, side3,side4):
    return float((side1+side2+side3+side4))

def square(side1, side2, side3):
    p = perimeter_t(side1, side2, side3) / 2
    return (sqrt(p * (p - side1) * (p - side2) * (p - side3)))

def lenght_median(side1, side2, side3):  # side3 вычитаем
    lenght_median = sqrt(2 * side1 ** 2 + 2 * side2 ** 2 - side3 ** 2) / 2
    return lenght_median


def angle(side1, side2, side3):  # side3 вычитаем
    angle = (acos((side1 ** 2 + side2 ** 2 - side3 ** 2) / (2.0 * side1 * side2)))
    return angle


def equation_side(point_x_1, point_y_1, point_x_2, point_y_2):
    A = float(point_y_2 - point_y_1)
    B = float(point_x_1 - point_x_2)
    C = float(point_x_2 * point_y_1 - point_x_1 * point_y_2)
    return '(' + str(A) + ')' + 'x + ' + '(' + str(B) + ')' + 'y + ' + '(' + str(C) + ')' + ' = 0'


def line_coefficients(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, -C


def intersection_x(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    if D != 0:
        x = Dx / D
        return x


def intersection_y(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        y = Dy / D
        return y