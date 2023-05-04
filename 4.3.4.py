""" Треугольник Паскаля 2
На вход программе подается натуральное число nn. 
Напишите программу, которая выводит первые nn строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n \, (n \ge 1)n (n≥1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника 
Паскаля, каждую на отдельной строке в соответствии с образцом. """
l = [[1]]

def pascal(n):
    for i in range(1,n+1):
        tmp_row=[1]*(i+1)
        for j in range(i+1):
            if j!=i and j!=0:
                tmp_row[j] = l[i-1][j-1]+l[i-1][j]
        l.append(tmp_row)
    return l[n]    

n=int(input())
pascal(n)

for i in range(n):
    print(*l[i]) 