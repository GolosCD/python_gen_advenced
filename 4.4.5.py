""" Напишите программу, которая выводит максимальный элемент в нижней по диагонали области квадратной матрицы"""

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)

sqm,lsqm=load_square_matrix()
max_value=sqm[0][0]
for i in range(1,lsqm):
    for j in range(i+1):
        max_value=max(max_value,sqm[i][j])
print(max_value)        