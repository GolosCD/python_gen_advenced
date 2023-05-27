
# На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
# 
# Формат входных данных
# На вход программе подаются два предложения, каждое на отдельной строке.
# 
# Формат выходных данных
# Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.
# 
# Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.

# William Shakespeare
# I am a weakish: speller,


#принимаем, отрезаем знаки, склеиваем в одну str
word1=''.join([i.strip('(.,;:-?!)').lower() for i in input().split()])
word2=''.join([i.strip('(.,;:-?!)').lower() for i in input().split()])

# создаем базы данных
dict1={}
dict2={}

# запись в одну бд
for i in word1:
    dict1.setdefault(i,word1.count(i))
    
# запись во вторую бд    
for i in word2:
    dict2.setdefault(i,word2.count(i))    

#сравнение и печать    
print('YES' if dict1==dict2 else 'NO')