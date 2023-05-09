""" На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n и заполняет её по следующему правилу:

на главной диагонали на месте каждого элемента должно стоять число 00;
на двух диагоналях, прилегающих к главной, число 11;
на следующих двух диагоналях число 22, и т.д.
Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи. """

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[0 for i in range(n)] for _ in range(n)]
    return final_list,len(final_list)  

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i]) 

if __name__ == '__main__':
    n = int(input())
    sqm,lsqm=load_square_matrix()
    #решение
    for i in range(lsqm):
        for j in range(lsqm):
            if i==j: #на главной диагонали на месте каждого элемента должно стоять число 0
                sqm[i][j]=0
            elif sqm[i][j] == sqm[j][i]:
                 sqm[i][j]=abs(i - j) 
                 sqm[j][i]=abs(i - j)    
    print_matrix(sqm,lsqm)