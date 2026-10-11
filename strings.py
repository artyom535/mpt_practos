# 1
# Дана строка. Выведите её длину, первый и последний символы.
text = "banananananana"
print(f"Длина: {len(text)}")
print(f"Первый символ: {text[0]}")
print(f"Последний символ: {text[-1]}")
# 2
# Выведите символ, стоящий в середине строки. Для строки чётной длины
# выведите оба средних.
string = "Macalala"
n = len(string)
if n % 2 == 0:
    print(f"Средние символы: {string[n // 2 - 1]}{string[n // 2]}")
else:
    print(f"Средний символ: {string[n // 2]}")
# 3
# Из строки получите: первые три символа, последние три, все символы с
# чётными индексами, строку в обратном порядке.
words = "Jackpot"
print(f"Первые три: {words[:3]}")
print(f"Последние три: {words[-3:]}")
print(f"Четные индексы: {words[::2]}")
print(f"В обратном порядке: {words[::-1]}")
# 4
# Дана строка. Выведите её в верхнем регистре, в нижнем регистре и с
# заглавной первой буквой.
texts = "BACON"
print(texts.upper())       # HELLO WORLD
print(texts.lower())       # hello world
print(texts.capitalize())  # Hello world
# 5
# Дана строка и символ c. Выведите, есть ли c в строке, сколько раз он
# встречается и индекс первого вхождения.
t = "avada ke dabra"
c = "a"
if c in t:
    print(f"Символ '{c}' встречается {t.count(c)} раз")
    print(f"Индекс первого вхождения: {t.index(c)}")
else:
    print(f"Символа '{c}' нет")
# 6
# Дана строка. Замените в ней все пробелы на подчёркивания.
txt = "а и б сидели на трубе"
new_txt = txt.replace(" ", "_")
print(new_txt)
# 7
# Дана строка с лишними пробелами в начале и в конце. Удалите их и
# выведите длину результата.
tt = "   Words are necessary   "
cleaned_text = tt.strip() # Удаляет пробелы только по краям
print(f"Результат: '{cleaned_text}'")
print(f"Длина: {len(cleaned_text)}")
# 8
# Дана строка из имени и фамилии через пробел. Выведите сначала
# фамилию, потом имя, а затем инициалы.
name = "Artyom Ivanov"
parts = name.split() # Разбиваем по пробелу в список ['Ivan', 'Ivanov']
name = parts[0]
surname = parts[1]
print(f"{surname} {name}")
print(f"Инициалы: {name[0]}.{surname[0]}.")
# 9
# Дана строка. Определите, является ли она палиндромом без учёта
# регистра.
tix = "Bob"
norm_text = tix.lower()
if norm_text == norm_text[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")
# 10
# Дана строка из слов через пробел. Выведите количество слов, первое
# слово и последнее слово.
tired = "banana kivi apple carrot"
wods = text.split() # Получаем список слов
print(f"Количество слов: {len(wods)}")
print(f"Первое слово: {wods[0]}")
print(f"Последнее слово: {wods[-1]}")