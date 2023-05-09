""" На шахматной доске 8 \times 88×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты ферзя на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номер строки (цифра от 11 до 88, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
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
            if dx==dy or x1 == i or y1 == j:#(dx <= 1 and dy <= 1)
                m[i][j]='*'
            if i==x1 and y1==j:
                m[i][j]='Q'
    fin=list()
    for i in range(l):
        a=list()#временный список
        for j in range(l):
            a.append(m[j][i])#поменял строку и столбец
                     
        fin.append(a)#сделал транспонирование, разворот матрицы
                       
    print_matrix(fin,l)




