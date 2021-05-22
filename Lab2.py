import random as rand
import math

var = 15
m = 5

yMax = (30 - var) * 10
yMin = (20 - var) * 10
xMin_1, xMax_1, xMin_2, xMax_2 = 10, 50, 25, 65
x_n = [[-1, -1], [1, -1], [-1, 1]]


def averageY(lst):
    average_Y = []
    for i in range(len(lst)):
        s = 0
        for j in lst[i]:
            s += j
        average_Y.append(s / len(lst[i]))
    return average_Y


def find_dispersion(lst):
    dispersion = []
    for i in range(len(lst)):
        s = 0
        for j in lst[i]:
            s += (j - averageY(lst)[i]) * (j - averageY(lst)[i])
        dispersion.append(s / len(lst[i]))
    return dispersion


def func_uv(u, v):
    if u >= v:
        return u / v
    else:
        return v / u


def discriminant(x11, x12, x13, x21, x22, x23, x31, x32, x33):
    return x11 * x22 * x33 + x12 * x23 * x31 + x32 * x21 * x13 - x13 * x22 * x31 - x32 * x23 * x11 - x12 * x21 * x33


y = [[rand.randint(yMin, yMax) for j in range(6)] for i in range(3)]
avY = averageY(y)

sigmaTheta = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))

Fuv = []
theta = []
Ruv = []

Fuv.append(func_uv(find_dispersion(y)[0], find_dispersion(y)[1]))
Fuv.append(func_uv(find_dispersion(y)[2], find_dispersion(y)[0]))
Fuv.append(func_uv(find_dispersion(y)[2], find_dispersion(y)[1]))

theta.append(((m - 2) / m) * Fuv[0])
theta.append(((m - 2) / m) * Fuv[1])
theta.append(((m - 2) / m) * Fuv[2])

Ruv.append(abs(theta[0] - 1) / sigmaTheta)
Ruv.append(abs(theta[1] - 1) / sigmaTheta)
Ruv.append(abs(theta[2] - 1) / sigmaTheta)

Rkr = 2

for i in range(len(Ruv)):
    if Ruv[i] > Rkr:
        print('Помилка, повторіть експеримент')

mx1 = (x_n[0][0] + x_n[1][0] + x_n[2][0]) / 3
mx2 = (x_n[0][1] + x_n[1][1] + x_n[2][1]) / 3
my = (avY[0] + avY[1] + avY[2]) / 3

a1 = (x_n[0][0] ** 2 + x_n[1][0] ** 2 + x_n[2][0] ** 2) / 3
a2 = (x_n[0][0] * x_n[0][1] + x_n[1][0] * x_n[1][1] + x_n[2][0] * x_n[2][1]) / 3
a3 = (x_n[0][1] ** 2 + x_n[1][1] ** 2 + x_n[2][1] ** 2) / 3

a11 = (x_n[0][0] * avY[0] + x_n[1][0] * avY[1] + x_n[2][0] * avY[2]) / 3
a22 = (x_n[0][1] * avY[0] + x_n[1][1] * avY[1] + x_n[2][1] * avY[2]) / 3

b0 = discriminant(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b1 = discriminant(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b2 = discriminant(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)

y_pr1 = b0 + b1 * x_n[0][0] + b2 * x_n[0][1]
y_pr2 = b0 + b1 * x_n[1][0] + b2 * x_n[1][1]
y_pr3 = b0 + b1 * x_n[2][0] + b2 * x_n[2][1]

dx1 = abs(xMax_1 - xMin_1) / 2
dx2 = abs(xMax_2 - xMin_2) / 2
x10 = (xMax_1 + xMin_1) / 2
x20 = (xMax_2 + xMin_2) / 2

koef_0 = b0 - (b1 * x10 / dx1) - (b2 * x20 / dx2)
koef_1 = b1 / dx1
koef_2 = b2 / dx2

yP1 = koef_0 + koef_1 * xMin_1 + koef_2 * xMin_2
yP2 = koef_0 + koef_1 * xMax_1 + koef_2 * xMin_2
yP3 = koef_0 + koef_1 * xMin_1 + koef_2 * xMax_2

print('Матриця планування для m =', m)
for i in range(3):
    print(y[i])
print('Експериментальні значення критерію Романовського:')
for i in range(3):
    print(Ruv[i])

print('Натуралізовані коефіцієнти: \n'
      'a0 =', round(koef_0, 4), 'a1 =', round(koef_1, 4), 'a2 =', round(koef_2, 4))
print('У практичний ', round(y_pr1, 4), round(y_pr2, 4), round(y_pr3, 4),
      '\nУ середній', round(avY[0], 4), round(avY[1], 4), round(avY[2], 4))
print('У практичний норм.', round(yP1, 4), round(yP2, 4), round(yP3, 4))
