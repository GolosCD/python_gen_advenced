""" На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n \times mn×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. """
def load_matrix(n,m):
    final_list=[['*' for i in range(m)] for j in range(n)]
    s=0
    for i in range(n):
        for j in range(s,m,2):
            final_list[i][j]='.'
        s=(s+1)%2
        print(*final_list[i])
                
            
    #return final_list
   

if __name__=='__main__':
    size = [int(i) for i in input().split()]
    a=load_matrix(size[0],size[1])