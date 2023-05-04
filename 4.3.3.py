""" Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число nn. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).

 """

# Решаю через полное постреоние треуголника

n = 10
l = [[1]]

l = [[1]]

def pascal(n):
    for i in range(1,n+1):
        tmp_row=[1]*(i+1)
        for j in range(i+1):
            if j!=i and j!=0:
                tmp_row[j] = l[i-1][j-1]+l[i-1][j]
        l.append(tmp_row)
    return l[n]    

print(pascal(n))            