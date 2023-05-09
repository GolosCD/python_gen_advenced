""" Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый столбец которой содержат все числа от 11 до nn. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.
 """
# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(n)]
    return final_list,len(final_list)  

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i]) 

if __name__ == '__main__':
    n = int(input())
    sqm,lsqm=load_square_matrix()
    
    fin=list()#итоговая спиоск после разворота
    for i in range(lsqm):
        a=list()#временный список
        for j in range(lsqm):
            a.append(sqm[j][i])#поменял строку и столбец
                     
        fin.append(a[::-1])#сделал транспонирование, разворот матрицы
                             
    #print_matrix(sqm,lsqm)
    #print()
    #print_matrix(fin,lsqm)
    
    
    
    #решение
    flag='YES'
    for i in range(1,lsqm+1):
        if i not in sqm[i-1] or i not in fin[i-1]:
            #print(1)
            flag='NO'
            break
        elif len(set(sqm[i-1]))!=len(sqm[i-1]) or len(set(fin[i-1]))!=len(fin[i-1]):
            #print(2)
            flag='NO'     
            break
        for j in range(i-1):
            if sqm[i-1][j] not in range(1,lsqm+1) or fin[i-1][j] not in range(1,lsqm+1):
                #print(3)
                flag='NO'
                break
            
        

    print(flag)          