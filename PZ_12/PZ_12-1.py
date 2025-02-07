# Организовать и вывести последовательность А из n чисел. Из
# последовательности А получить две последовательности В и С: в последовательности В –
# четные элементы А, в С – нечетные элементы А.  Произвести суммирование
# соответствующих элементов последовательностей В и С. Найти минимальный элемент
# полученной последовательности.
import random
A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
B = []
C = []
Fin = []

def aga(N):
    for i in range(len(N)):
        Fin.append(B[i] + C[i])
        i += 1
    print("сумма чисел: ",Fin)
    print("минимальное значение: ",min(Fin))


for i in range(len(A)):
    a = random.randint(1, 50)
    A[i] = a * A[i]
print("список А: ",A)
list(map(lambda x: B.append(x) if not x % 2 else None, A))
list(map(lambda x: C.append(x) if x % 2 else None, A))
print("список B: ",B)
print("список C: ",C)
if len(B) > len(C):
    aga(C)
elif len(B) < len(C):
    aga(B)



