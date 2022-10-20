# Алгоритм вставки символов в массив
a = [1, 54, 8, 490]
b = [3, 95, 902, 11]
c = []
k = 3
for i in range(0, len(a)):
    if i == k:
        for j in range(0, len(b)):
            c.append(b[j])
    c.append(a[i])
print(c)