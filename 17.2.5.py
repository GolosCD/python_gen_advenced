""" Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами пробела и конца строки. 
Напишите программу, выводящую на экран сумму этих чисел.
"""

file_name = 'nums.txt'

file_open = open (file_name,'rt',encoding = 'utf8')

file_read = [int(dig) for dig in file_open.read().split()]

file_open.close()


print(sum(file_read))