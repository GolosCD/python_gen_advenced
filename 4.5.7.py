""" Напишите программу, которая поворачивает квадратную матрицу чисел на 90^{\circ}90 
∘
  по часовой стрелке.

Формат входных данных
На вход программе подаётся натуральное число nn — количество 
строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом. """

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i]) 
    


if __name__=='__main__':
    sqm,lsqm=load_square_matrix()
    
    fin=list()#итоговая спиоск после разворота
    
    for i in range(lsqm):
        a=list()#временный список
        for j in range(lsqm):
            a.append(sqm[j][i])#поменял строку и столбец
                     
        fin.append(a[::-1])#сделал транспонирование, разворот матрицы
                             
    print_matrix(fin,lsqm)