""" 
Следом квадратной матрицы называется сумма элементов главной диагонали. 
Напишите программу, которая выводит след заданной квадратной матрицы.
"""

# put your python code here
n = int(input())

#функция загрузки квадратной матрицы            
def load_square_matrix(n):
    final_list=list()
    for i in range(n):
        final_list.append([int(i) for i in input().split()])
    return final_list    

#функция расчета следа матрицы
def calc_matrix_step(l):
    n= len(l)
    sum_step_matrix=0
    for i in range(n):
        for j in range (n):
            if i==j:
                sum_step_matrix+=l[i][j]
    return sum_step_matrix            
            

if __name__=='__main__':
    print(calc_matrix_step(load_square_matrix(n)))