#Задача первая
a = input()
print(int(a[0])+int(a[1])+int(a[2]))
#Задача Вторая
s = int(input())
P=C=s//6
K=(P+C)*2
print(K,P,C)
#Задача третья
b = input()
if int(b[0])+int(b[1])+int(b[2]) == int(b[3])+int(b[4])+int(b[5]):
    print('yes')
else:
    print("no")
#Задача четвёртая
f,d,g = int(input()),int(input()),int(input())
if g<=f*d and (g%f==0 or g%d==0):
    print('yes')
else:
    print("no")