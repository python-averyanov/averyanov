l = ["-99 9 8 5 4 34 67 -4 6 -7 3 -2 6 -87 -6554 -6 934 654 345 67 -3 4 -886"]
# tap = open('ala.txt','w')
# tap.writelines(l)
# tap.close()
file = open('ala.txt', "r")
aa = file.read()
print("исходные данные: ",aa) #1
aaa = aa.split()
result = list(map(int, aaa))
lis = []
for i in result:
    if i <= 1 and i % 2 == 0:
        lis.append(i)
print(len(lis)) #2
print(sum(lis))#3
finall = sum(lis) / len(lis)
print(finall)#4
