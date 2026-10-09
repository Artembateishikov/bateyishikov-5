N = int(input("Введите количество чисел: "))
a = list(map(int, input("Введите числа через пробел: ").split()))

a.sort()
result = a[-2] - a[1]

print("Разность: ", result)