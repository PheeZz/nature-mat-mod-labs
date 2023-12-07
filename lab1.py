import matplotlib


def dir(T, h):
    n = len(h)
    pr_l = []
    for i in range(n - 1):
        if (float(h[i + 1]) - float(h[i])) == 0:  # если зонд по ошибке измерил 0
            dh = 0.0000000001  # присваиваем число, приближенное к 0
            pr_l.append((float(T[i + 1]) - float(T[i])) / dh)
        else:
            pr_l.append((float(T[i + 1]) - float(T[i])) / (float(h[i + 1]) - float(h[i])))
    return pr_l


f = open("CTD.csv", "r")
f.readline()

current_station = ""
depth = []  # пустые строки
temp = []

for line in f:
    str = line.split(";")
    if current_station == "":  # проверка первой строки
        current_station = str[0]
    while str[0] != current_station:  # обработка новой станции
        print(
            dir(
                temp,
                depth,
            )
        )
        current_station = str[0]
        depth = []
        temp = []
