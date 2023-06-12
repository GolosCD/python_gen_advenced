""" Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число. 
Напишите программу, выводящую на экран сумму этих чисел.
"""


file_name = 'numbers.txt'

file_open = open (file_name,'rt',encoding = 'utf8')

file_read = list(map(int,file_open.readlines()))

file_open.close()


print(sum(file_read))