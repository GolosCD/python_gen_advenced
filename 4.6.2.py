""" На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n и заполняет её по следующему правилу:

числа на побочной диагонали равны 11;
числа, стоящие выше этой диагонали, равны 00;
числа, стоящие ниже этой диагонали, равны 22.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Примечание. Побочная диагональ — это диагональ, идущая из правого верхнего в левый нижний угол матрицы.
 """
def load_matrix(n):
    final_list=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if j==n-1-i:
                final_list[i][j]=1
            elif i +j >= n:
                final_list[i][j]=2
        print(*final_list[i])
                
            
    #return final_list
   

if __name__=='__main__':
    size = int(input())
    a=load_matrix(size)