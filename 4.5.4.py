""" Напишите программу, которая проверяет симметричность квадратной матрицы относительно 
главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем 
элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной 
диагонали, и слово NO в противном случае.
 """
# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)


if __name__=='__main__':
    sqm,lsqm=load_square_matrix()
    
    flag = 'YES'
    
    for i in range(lsqm):
        for j in range(i):
            if i>j and sqm[i][j]!=sqm[j][i]:
                flag='NO'
                break
    print(flag)    