# Алгоритм перемещения половин массивов
a = [87, 1, 90, 4, 30, 7]
b = []
if len(a)%2 == 0:
    f = int(len(a)/2)
    for i in range(0, len(a)):
        if (i >= 0) and (i < 3):
            b.append(a[i+f])
        else:
            b.append(a[i-f])
    print(b)
else:
    print("Error")