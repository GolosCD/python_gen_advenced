""" На вход программе подается строка с именем текстового файла. 
Напишите программу, которая выводит на экран его содержимое. """

file_name = input()

file_open = open (file_name,'rt',encoding = 'utf8') #открываю файл в кодировке utf8

file_read = list(map(str.strip,file_open.readlines())) #получу список строк

file_open.close() #обязательное закрытие файла


print(*file_read) #печать списка с распаковкой