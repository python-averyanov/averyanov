# Известно, что X кг конфет стоит A рублей. Определить, сколько
# стоит 1 кг и Y кг этих же конфет.
try:
    x = int(input('сколько кг?   '))
    a = int(input('сколько стоило?  '))
    y = int(input('сколько кг?  '))

except:
    print("неверно")
ax = a/x
tcena = (y*ax)
itog = tcena + ax
print(itog)
