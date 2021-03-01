import random as rd

a_0 = rd.randint(1, 10)
a_1 = rd.randint(1, 10)
a_2 = rd.randint(1, 10)
a_3 = rd.randint(1, 10)
x_1 = rd.sample(range(1, 20), 8)
x_2 = rd.sample(range(1, 20), 8)
x_3 = rd.sample(range(1, 20), 8)
X0_x1 = (min(x_1) + max(x_1)) / 2
X0_x2 = (min(x_2) + max(x_2)) / 2
X0_x3 = (min(x_3) + max(x_3)) / 2
dx_x1 = X0_x1 - min(x_1)
dx_x2 = X0_x3 - min(x_2)
dx_x3 = X0_x2 - min(x_3)
Xn1 = []
Xn2 = []
Xn3 = []
for i in range(len(x_1)):
    rn = round((x_1[i] - X0_x1) / dx_x1, 4)
    Xn1.append(rn)
for i in range(len(x_2)):
    rn = round((x_2[i] - X0_x2) / dx_x2, 4)
    Xn2.append(rn)
for i in range(len(x_3)):
    rn = round((x_3[i] - X0_x3) / dx_x3, 4)
    Xn3.append(rn)

Y = []
for i in range(len(x_1)):
    y = a_0 + (a_1 * x_1[i]) + (a_2 * x_2[i]) + (a_3 * x_3[i])
    Y.append(y)

out = []
for i in range(8):
    out.append([])
    out[i].append(i + 1)
    out[i].append(x_1[i])
    out[i].append(x_2[i])
    out[i].append(x_3[i])
    out[i].append(Y[i])
    out[i].append(Xn1[i])
    out[i].append(Xn2[i])
    out[i].append(Xn3[i])

out.insert(0, ["№", "X_1", 'X_2', "X_3", 'Y', "Xn1", "Xn2", "Xn3"])
out.append([])
out.append([])
out[-1].append("X0")
out[-1].append(X0_x1)
out[-1].append(X0_x2)
out[-1].append(X0_x3)
out.append([])
out[-1].append("dx")
out[-1].append(dx_x1)
out[-1].append(dx_x2)
out[-1].append(dx_x3)

for row in out:
    print('  :  '.join([str(i) for i in row]))
middle = sum(Y) / len(Y)
M = [] # Масив, у якому зберігаються усі Y, що відповідають варіанту завдання(->середнє Y : менше за середнє Y в даному випадку)
for i in Y:
    if middle - i > 0:
        M.append(middle - i)
a = min(M)
_Y = middle - min(M)
print("->Y = ", _Y)
print('a0 = {}, a1 = {}, a2 = {}, a3 = {}'.format(a_0, a_1, a_2, a_3))
