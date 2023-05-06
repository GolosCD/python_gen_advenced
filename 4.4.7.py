""" Квадратная матрица разбивается на четыре четверти, 
ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую. 
Напишите программу, которая вычисляет сумму элементов: верхней четверти; 
правой четверти; нижней четверти; левой четверти."""

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)


if __name__=='__main__':
    sqm,lsqm=load_square_matrix()
    upper_quarter=0
    right_quarter=0
    lower_quarter=0
    left_quarter=0
    
    
    for i in range(lsqm):
        for j in range(lsqm):
            if i<j and i<lsqm-1-j: #если элемент[i][j] тут то, это верхняя четверть
                upper_quarter+=sqm[i][j]
            elif i<j and i>lsqm-1-j:   #если элемент[i][j] тут то, это правая четверть
                right_quarter+=sqm[i][j]
            elif i>j and i>lsqm-1-j:   #если элемент[i][j] тут то, это нижняя четверть 
                lower_quarter+=sqm[i][j]
            elif i>j and i<lsqm-1-j: #если элемент[i][j] тут то, это левая четверть
                left_quarter+=sqm[i][j]
            else:
                continue
 
    print(f'Верхняя четверть: {upper_quarter}',f'Правая четверть: {right_quarter}',\
          f'Нижняя четверть: {lower_quarter}',f'Левая четверть: {left_quarter}',sep='\n')