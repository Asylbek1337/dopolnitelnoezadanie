def function2(array):
    total = 0
    for element in range(len(array)):
        total += array[element]

    return total

d = []
print('Введите элемент списка:')
k = int(input())
d.append(k)
print('Введите элемент списка:')
l = int(input())
d.append(l)
print('Введите элемент списка:')
c = int(input())
d.append(c)
print('Введите элемент списка:')
g = int(input())
d.append(g)
print('Введите элемент списка:')
e = int(input())
d.append(e)
print(d)

print(function2(d))