""" Вам доступен текстовый файл lines.txt из нескольких строк. 
Напишите программу, которая выводит на экран случайную строку из этого файла.
"""

from random import choice
file_name = 'lines.txt'

file_open = open (file_name,'rt',encoding = 'utf8')

file_read = list(map(str.strip,file_open.readlines()))

file_open.close()


print(choice(file_read))