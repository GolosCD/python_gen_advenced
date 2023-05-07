""" На шахматной доске 8 \times 88×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 11 до 88, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами. """

""" 
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2) # модуль разницы координат X
dy = abs(y1 - y2) # модуль разницы координат Y
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
# если разность X1 и X2 равна одной клетке а Y1 и Y2 двум или наоборот X1 и Y1
# двум клектам а Y1 и Y2 одной клетке то выводим на экран YES
    print('YES')
else:
    print('NO')
"""

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[['.' for i in range(8)] for _ in range(8)]
    return final_list,len(final_list)

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i]) 

if __name__ == '__main__':
    start_position = input()
    x1,y1 = ('abcdefgh'.index(start_position[0])), ('87654321'.index(start_position[1]))
    #print(x1,y1)
    m,l=load_square_matrix()

    for i in range(l):
        for j in range(l):
            dx = abs(x1-i) # модуль разницы координат X
            dy = abs(y1-j) # модуль разницы координат Y
            if dx == 1 and dy == 2 or dx == 2 and dy == 1:
                m[i][j]='*'
            elif i==x1 and y1==j:
                m[i][j]='N'
    fin=list()
    for i in range(l):
        a=list()#временный список
        for j in range(l):
            a.append(m[j][i])#поменял строку и столбец
                     
        fin.append(a)#сделал транспонирование, разворот матрицы
                       
    print_matrix(fin,l)
