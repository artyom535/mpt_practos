# 1
# Создайте словарь из трёх учеников и их оценок. Выведите оценку одного
# ученика по его имени.
school_dict = {"Ванечкин":2,"Артём":5,"Денис":4}
print(f"Оценка Ванечки - {school_dict['Ванечкин']}")
# 2
# Дан словарь. Добавьте в него новую пару, измените значение одного из
# ключей, удалите другой ключ и выведите результат.
dict0 = dict(name="Костя",age=16,city="Москва")
dict0["money"]=9999
dict0["age"]=17
del dict0["city"]
print(dict0)
# 3
# Дан словарь и ключ. Выведите значение по этому ключу, а если такого
# ключа нет, выведите «Нет такого ключа».
dict1 = {"ванечкин": 4, "егор": 5, "стёпа": 3}
key = input()
if key in dict1:
 print(dict1[key])
else:
 print("нет такого ключа")
# 4
# Дан словарь. Выведите отдельно все его ключи, все значения и количество
# пар.
dict2 = {"дом": "пентхаус", "машина": "бугати", "телефон": "сеоми"}
print(f"Ключи: {list(dict2.keys())}")
print(f"Значения: {list(dict2.values())}")
print(f"Число пар: {len(dict2)}")
# 5
# Дан словарь товаров и их цен. Выведите каждый товар и его цену с новой
# строки.
dict3 = {"молоко": 119, "батон хлеба": 45, "маунти дью": "бесценно"}
for key, value in dict3.items():
    print(key, value)
# 6
# Дан словарь товаров и их цен. Найдите сумму всех цен и название самого
# дорогого товара.
dict4 = {"молоко": 119,"батон хлеба": 45,"маунти дью": 999}
total_sum = sum(dict4.values())
most_expensive = max(dict4, key=dict4.get)
max_price = dict4[most_expensive]
print(f"Сумма всех цен: {total_sum}")
print(f"Самый дорогой товар: {most_expensive} цена: {max_price}")
# 7
# Дана строка. Посчитайте, сколько раз в ней встречается каждый символ, и
# сохраните результат в словарь.
string = "banana"
dict5 = {}
for c in string:
    if c in dict5:
        dict5[c] +=1
    else:
        dict5[c] = 1
print(dict5)
# 8
# Дана строка из слов через пробел. Посчитайте, сколько раз встречается
# каждое слово, и выведите самое частое.
sting = 'apple kivi orange melon orange orange melon'
g = sting.split(" ")
dict6 = {}
max_c = 0
for t in g:
    dict6[t] = dict6.get(t, 0) + 1
best_fruit = None
max_c = 0
for word, count in dict6.items():
    if count > max_c:
        max_c = count
        best_fruit = word
print(f"Самое частое: {best_fruit}, встречается {max_c} раз")
print(dict6)
# 9
# Дан словарь. Создайте новый словарь, в котором ключи и значения
# поменяны местами.
dict7 = {"дом":"пентхаус","машина":"бугати","телефон":"сеоми","радость":"не в деньгах"}
reverse_dict7 = {}
for key, value in dict7.items():
    reverse_dict7[value] = key
print(reverse_dict7)
# 10
# Даны два списка одинаковой длины: страны и их столицы. Составьте из
# них словарь и выведите столицу страны, которую введёт пользователь.
country = ["Россия","Америка","Англия","Франция"]
capital = ["Москва","Вашингтон","Лондон","Париж"]
dict8 = {}
for h in range(len(country)):
        dict8[country[h]] = capital[h]
variant = input("Введите название страны, столицу которой хотите узнать ")
if variant in dict8:
    print(dict8[variant])
else:
    print("Страна не найдена в словаре.")
