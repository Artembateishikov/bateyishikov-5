N = int(input("Введите количество чисел: "))
a = list(map(int, input("Введите числа через пробел: ").split()))

n = [x for x in a if x < 0]
p = [x for x in a if x > 0]

if len(n) == 0 or len(p) == 0:
    print("Нет отрицательных элементов")
else:
    max_n = max(n,key=abs)
    min_p = min(p, key=abs)

    result = abs(max_n) - abs(min_p)
    print('Разность:', result)
