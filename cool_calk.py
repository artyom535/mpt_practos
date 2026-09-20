print("Это калькулятор, у него 2 режима")
process = True
while process is True:
    print("\n")
    print("Выберите тип калькулятора:\n1. Арифметический\n2. Геометрический\nЧтобы выйти, выберите 3")
    print("\n")
    calk = int(input("Введите цифру, калькулятором которой будете пользоваться! "))
    if calk == 1:
        print("Тип калькулятора - арифметический\nЭтот калькулятор может выполнять простые арифметические операции")
        print("\n")
        operation = input("Введите тип операции:\n+ - сложение\n- - вычитание\n* - умножение\n/ - деление\n// - целочисленное деление\n% - остаток от деления\n** - возведение 1 числа в степень 2\n> ")
        
        if operation not in "+-*/" and operation != "//" and operation != "%" and operation != "**":
            print("Введённый символ не входит в набор допустимых операций")
            continue
            
        if operation in "+-*/" or operation == "//" or operation == "%" or operation == "**":
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            if operation == '+':
                print(f"Ответ: {num1 + num2}")
            elif operation == '-':
                print(f"Ответ: {num1 - num2}")
            elif operation == '*':
                print(f"Ответ: {num1 * num2}")
            elif operation == '/':
                if num2 != 0:
                    print(f"Ответ: {num1 / num2}")
                else:
                    print("Делить на ноль нельзя, введите по-другому")
            elif operation == '//':
                if num2 != 0:
                    print(f"Ответ: {num1 // num2}")
                else:
                    print("Делить на ноль нельзя, введите по-другому")
            elif operation == '%':
                if num2 != 0:
                    print(f"Ответ: {num1 % num2}")
                else:
                    print("Делить на ноль нельзя, введите по-другому")
            elif operation == '**':
                print(f"Ответ: {num1 ** num2}")
            else:
                print("Неверный знак операции, введите другой")
                
    elif calk == 2:
        print("Тип калькулятора - геометрический\nЭтот калькулятор на основе введённых вами сторон говорит всё о треугольнике с такими сторонами")
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        c = float(input("Введите сторону c: "))
        print("\n")
        triangle = True
        
        if a <= 0 or b <= 0 or c <= 0:
            print("Стороны треугольника должны быть больше нуля!")
            triangle = False
        elif not (a + b >= c and a + c >= b and b + c >= a):
            print("Треугольник не соответствует теореме о неравенстве треугольника, а значит такого набора сторон не может быть, введите другие стороны!")
            triangle = False
        if triangle is True:
            if a == b and b == c:
                print("Треугольник РАВНОСТОРОННИЙ")
            elif a == b or b == c or a == c:
                print("Треугольник РАВНОБЕДРЕННЫЙ")
            elif not (a == b or b == c or a == c):
                print("Треугольник РАЗНОСТОРОННИЙ")
                
            if a > b and a > c:
                print(f"Самая большая сторона: a = {a}")
            elif b > a and b > c:
                print(f"Самая большая сторона: b = {b}")
            elif c > a and c > b:
                print(f"Самая большая сторона: c = {c}")
                
            if a < b and a < c:
                print(f"Самая маленькая сторона: a = {a}")
            elif b < a and b < c:
                print(f"Самая маленькая сторона: b = {b}")
            elif c < a and c < b:
                print(f"Самая маленькая сторона: c = {c}")    
            if a >= b and a >= c:
                max_side = a
                side1, side2 = b, c
            elif b >= a and b >= c:
                max_side = b
                side1, side2 = a, c
            else:
                max_side = c
                side1, side2 = a, b    
            if side1**2 + side2**2 == max_side**2:
                print("Треугольник ПРЯМОУГОЛЬНЫЙ (a² + b² = c²)")
            elif side1**2 + side2**2 > max_side**2:
                print("Треугольник ОСТРОУГОЛЬНЫЙ (a² + b² > c²)")
            elif side1**2 + side2**2 < max_side**2:
                print("Треугольник ТУПОУГОЛЬНЫЙ (a² + b² < c²)")
            else:
                print("Введены некорректные данные")
                
            per = a + b + c
            print(f"Периметр: {per}")
            
        elif triangle is not True:
            continue

    elif calk == 3:
        print("Выход из программы, спасибо за пользование(-__-)")
        process = False
    else:
        print("!!!Введите ЧИСЛО от 1 до 3, ни больше, ни меньше!!!")
