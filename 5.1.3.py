""" Напишите программу, которая транспонирует квадратную матрицу.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести транспонированную матрицу.

Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

Примечание 2. Задачу можно решить без использования вспомогательного списка.  """

# put your python code here
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i])



if __name__ == '__main__':
    sqm,lsqm=load_square_matrix()
    
    fin=list()#итоговая спиоск после разворота
    
    for i in range(lsqm):
        a=list()#временный список
        for j in range(lsqm):
            a.append(sqm[j][i])#поменял строку и столбец                  
        fin.append(a)
                             
    print_matrix(fin,lsqm)
    