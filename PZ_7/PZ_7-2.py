ara = ['(',')','[',']','{','}']
z = []
for i in ara:
    a = ord(i)
    z.append(a)
print(z)
def alala(a,b):
    if a and b in z:
        None
    elif a and b not in z:
        print("скобок нет")
    elif a and not b in z:
        print("не хвататет )")
    elif b and not a in z:
        print("не хвататет (")
alala(40,41)
alala(91,93)
alala(123,125)