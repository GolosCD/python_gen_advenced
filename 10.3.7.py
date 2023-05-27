<<<<<<< HEAD
import string
import random

LETTER = list((set(string.printable[: string.printable.rindex('!')])) - set('lI1oO0'))

print(LETTER)

# generate_str: str = string.printable[: string.printable.rindex('!')]


# for i in '1Ilo0O':
#     generate_str = generate_str.replace(i,'')

# generate_str = list(generate_str)

# def generate_password(length):
#     return length

# def generate_passwords(count:int, length:int):
    
#     for _ in range(count):
#         random.shuffle(generate_str)
#         password = random.sample(generate_str,length)
#         print(''.join(password))



# if __name__ == '__main__':
#               n, m = int(input()), int(input())
              
#               generate_passwords(n,generate_password(m))
=======
# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# 
# Формат входных данных
# На вход программе подается строка текста.
# 
# Формат выходных данных
# Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.
# 
# Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.
# 
# Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.

result = dict()

s=[i.strip('(.,;:-?!)').lower() for i in input().split()]

for i in sorted(s):
    result.setdefault(s.count(i),i)

print(result.get(min(result)))
>>>>>>> 15c055b879b56efcbcc465aba3adefda8332bcdb
