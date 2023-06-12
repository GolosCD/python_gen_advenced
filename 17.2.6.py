""" Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами пробела и конца строки. 
Напишите программу, выводящую на экран сумму этих чисел.
"""

file_name = 'prices.txt'

file_open = open (file_name,'rt',encoding = 'utf8')

file_read = [int(dig.strip().split('\t')[-2])*int(dig.strip().split('\t')[-1]) for dig in file_open.readlines()]

file_open.close()


print(sum(file_read))