""" Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
 """

#  новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(n)]
    return final_list,len(final_list)

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i]) 
        
#matrix[::-1], i != j, matrix[i][j] != matrix[j][i]

if __name__ == '__main__':
    n = int(input())
    sqm,lsqm=load_square_matrix()
  
    flag='YES'
    for i in range(lsqm):
        for j in range(lsqm):
            if sqm[i][j] != sqm[n-1-j][n-1-i]:
                flag='NO'
                break
    print(flag)        