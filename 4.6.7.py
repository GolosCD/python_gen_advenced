
""" На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
 """
# put your python code here
size = [int(i) for i in input().split()]
n = size[0]
m = size[1]
matrix = [[  (i  + j) % m + 1 for j in range(m)] for i in range(n)]

for r in range(n):                     # выводим матрицу
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()