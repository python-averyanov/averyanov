import random
N = int(input("введите число:  "))
a = []
b = []
for o in range(1,N):
    a.append(random.randint(1,N))

for i in a:
    if a[i] > a[i+ 1]:
        b.append(a)

print(a)
print(b)