n = int(input())
a = list()
b = list()
sum = list()
x = input().split()
y = input().split()
for i in range(len(x)):
    a.append(int(x[i]))
 
for i in range(len(y)):
    b.append(int(y[i]))
 
for i in range(len(a)):
    sum.append(a[i] + b[i])
 
for i in sum:
    print(i, end = ' ')
