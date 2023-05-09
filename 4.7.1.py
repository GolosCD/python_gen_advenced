""" Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
 """

if __name__=='__main__':
    size = [int(i) for i in input().split()]
    n = size[0]
    m = size[1]
    #print(n,m)
    A=list()
    A=[[int(i) for i in input().split()] for j in range(n)]
    input()
    B=[[int(i) for i in input().split()] for j in range(n)]
    for i in range(n):
        C=list()
        for j in range(m):
            C.append(A[i][j]+B[i][j])
        print(*C)