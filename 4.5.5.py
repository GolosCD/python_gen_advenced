""" Дана квадратная матрица чисел. Напишите программу, которая меняет местами 
элементы, стоящие на главной и побочной диагонали, при этом каждый элемент 
должен остаться в том же столбце (то есть в каждом столбце нужно поменять 
местами элемент на главной диагонали и на побочной диагонали).

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в 
матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести матрицу с элементами главной и побочной диагонали, 
поменявшимися своими местами. """
# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)


if __name__=='__main__':
    sqm,lsqm=load_square_matrix()
    
    for i in range(lsqm):
        for j in range(lsqm):
            if i==j:
                sqm[i][j],sqm[lsqm-1-i][j]=sqm[lsqm-1-i][j],sqm[i][j]
                
    for i in range(lsqm):
        print(*sqm[i])       