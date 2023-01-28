# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("enter number:"))
sum = 0
while n > 0:
    sum = sum + n % 10
    n //= 10
print(sum)


