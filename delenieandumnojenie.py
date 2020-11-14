print('Меню')
print('1. Ввести значения a и b')
print('2. Умножить значения a и b')
print('3. Делить значение a на b')
print('4. Выйти')

userchoise = int(input())
a = -999999999
b = -9999999999
while userchoise != 4:
    if (userchoise < 1) | (userchoise > 4):
        print('Такого пункта нет, введите существующий пункт:')
        userchoise = int(input())
    else:
        if userchoise == 1:
            def show (x, y):
                return x, y

            print('Введите значение а:')
            a = int(input())
            print('Введите значение b:')
            b = int(input())
            print(show(a, b))


        elif userchoise == 2:
            if a != -999999999 and b != -9999999999:
                def multi (x, y):
                    return x*y

                print(multi(a, b))
            elif a == -999999999 and b == -9999999999:
                print('Значения не введены, введите значения.')
                print('Введите значение а:')
                a = int(input())
                print('Введите значение b:')
                b = int(input())


        elif userchoise == 3:
            if a != -999999999 and b != -9999999999:
                if b != 0:
                    def div(x, y):
                        return x/y
                    print(div(a, b))
                elif b == 0:
                    print('Значения не могут быть поделены.')
                    print('Введите значение а:')
                    a = int(input())
                    print('Введите значение b:')
                    b = int(input())


            elif a == -999999999 and b == -9999999999:
                print('Значения не введены, введите значения.')


        print('\n Меню')
        print('1. Ввести значения a и b')
        print('2. Умножить значения a и b')
        print('3. Делить значение a на b')
        print('4. Выйти')
        userchoise = int(input())
        