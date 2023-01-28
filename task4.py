# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
m = int(input("enter m:"))
n = int(input("enter n:"))
k = int(input("enter k:"))

result = False

if m * n >= k and (k % m == 0 or k % n == 0):
    result = True

print(result)












