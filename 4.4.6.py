""" Напишите программу, которая выводит максимальный элемент в левой и правой области квадратной матрицы."""
""" У меня немного но другой подход к задаче. 
Мне важно попасть в нужный диапазон в любой стороне матрицы. 
Как только я в него попал, я зеркально сравниваю числа из этого ряда и записываю максимальное в переменную. 
Мне не нужно проверять два условия, я проверяю одно и делаю расчет.  """

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)


if __name__=='__main__':
    sqm,lsqm=load_square_matrix()
    
    max_value=max(sqm[0][0],sqm[0][-1])
    
    for i in range(1,lsqm):
        for j in range(i+1):
            if (i>=j and i<=lsqm-1-j):
                max_value=max(max_value,max(sqm[i][j],sqm[i][-j-1]))
    print(max_value)         