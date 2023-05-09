""" На вход программе подается нечетное натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её символами . . Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе подается нечетное натуральное число n, \, (n \ge 3)n,(n≥3) — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи. """

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[['.' for i in range(n)] for _ in range(n)]
    return final_list,len(final_list)

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i]) 

if __name__ == '__main__':
    n = int(input())
    sqm,lsqm=load_square_matrix()
    
    for i in range(n):
        for j in range(n):
            if i==j or i+j+1==n or i==n//2 or j==n//2:
                sqm[i][j]='*'
    print_matrix(sqm,lsqm)
    