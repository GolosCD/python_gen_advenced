""" Максимальный в области 2
Напишите программу, которая выводит максимальный элемент в нижней и правой области квадратной матрицы. """

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)


if __name__ == '__main__':
    sqm,lsqm=load_square_matrix()
    max_value=sqm[-1][-1]
    for i in range(lsqm):
        for j in range(lsqm):
            if (i>=j and i>lsqm-1-j) or (i<=j and i>lsqm-1-j) or (i+j+1==lsqm) :
                max_value=max(max_value,sqm[i][j])
    print(max_value)     
