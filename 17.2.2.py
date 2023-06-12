""" На вход программе подается строка с именем текстового файла. 
Напишите программу, которая выводит на экран его ПРЕДпоследнюю строку. """

file_name = input()

file_open = open (file_name,'rt',encoding = 'utf8')

file_read = list(map(str.strip,file_open.readlines()))

file_open.close()


print(file_read[-2])