# 1
# Выведите все числа от 1 до 10.
for i in range(1,11):
    print(i)
# 2
# Выведите все чётные числа от 2 до 50.
for i in range(2,51,2):
    print(i)
# 3
# Выведите числа от 10 до 1 в порядке убывания.
for i in range(10,0,-1):
    print(i)
# 4
# Дано число n. Найдите сумму всех чисел от 1 до n.
n1 = int(input())
sum = 0
for i in range(1,n1 + 1):
    sum += i
print(sum)
# 5
# Дано число n. Найдите его факториал.
n2 = int(input())
fk = 1
for i in range(1,n2+1):
    fk *= i
print(fk)
# 6
# Дано число n. Выведите таблицу умножения на n от 1 до 10.
n3 = int(input())
for i in range(1,11):
    print(f"{n3} * {i} = {n3*i}")
# 7
# Дан список чисел. Посчитайте, сколько в нём положительных чисел.
count = 0
lst = [-1,-2,5,4,0,-9,44,-6]
for i in lst:
    if i > 0:
        count += 1
print(count)
# 8
# Дана строка. Посчитайте, сколько в ней гласных букв.
string = input("Введите любое русское слово ")
glass=('ёуеыаоэяиюЁУЕЫАОЭЯИЮ')
ct = 0
for i in string:
    if i in glass:
        ct +=1
print(ct)
# 9
# Дан список чисел. Найдите наибольший элемент, не используя max().
l = [1,2,3,4,5,6,7,8,9,10]
max = l[4]
for i in l:
    if max < i:
        max = i
print(max)
# 10
# Выведите таблицу умножения от 1 до 9 в виде квадрата.
for i in range(1, 10):
    for j in range(1,10):
        print(i * j, end = "\t")
    print()