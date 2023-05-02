'''
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению 
Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 
0
0.

'''

n = input()

for i in range(len(n), 0, -1):
    word = 'Р' * i
    if word in n:
        print(len(word))
        break
else:
    print(0)