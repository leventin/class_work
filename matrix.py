from random import * 
a = []
for i in range(0,10):
    a.append([])
    for j in range(0,10):
        a[i].append(randint(-9,9))

for i in range(0,10):
    for j in range(0,10):
         print(a[i][j], end = " ")
    print()
