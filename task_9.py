a = [1,3,6,2,9,5,8]
b = []
k = 2
m = 2
for i in range(0,len(a)):
    if i < k+1 or i > k+m:
        b.append(a[i])
print(b)