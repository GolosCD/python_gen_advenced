# На вход программе подается строка, содержащая строки - идентификаторы. Напишите программу, которая исправляет их так,
# чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
# 
# Формат входных данных
# На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.
# 
# Формат выходных данных
# Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.+

s = [i for i in input().split()] #принимаем входные данные

database=dict()# пустой словарь

for i in range(len(s)):
    if s[i] not in database:
            database[s[i]] = database.get(s[i], 0) + 1
            print(s[i], end=' ')
    else:
        print(f'{s[i]}_{database.get(s[i])}', end=' ')
        database[s[i]] = database.get(s[i], 0) + 1        
