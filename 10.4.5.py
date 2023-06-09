# На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу, которая для каждого города выводит, в какой стране он находится.
# 
# Формат входных данных
# Программа получает на вход количество стран
# �
# n. Далее идет
# �
# n строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. В следующей строке записано число
# �
# m, далее идут
# �
# m запросов — названия каких - то
# �
# m городов, из перечисленных выше.
# Формат выходных данных
# Программа должна вывести название страны, в которой находится данный город в соответствии с примером.

# 2
# Германия Берлин Мюнхен Гамбург Дортмунд
# Нидерланды Амстердам Гаага Роттердам Алкмар
# 4
# Амстердам
# Алкмар
# Гамбург
# Гаага

#создал бд
database = dict()

#принимаю вход
for _ in range(int(input())):

    input_list = input().split()#принимаю строку и бью на слова и записываю в список

    database.setdefault(tuple(input_list[1:]), input_list[0]) #последние три слова в кортеж и это ключ, последнее слово это значение

# перебор словаря и поиск введеного значения в ключе
for _ in range(int(input())):
    city = input() #принял строку
    for key in database: #достаю ключ кортеж из базы данных
        if city in key:# проверяю что принятая строка есть в кортеже ключа
            print(database.get(key)) # если есть то печатаю
