""" Напишите программу, которая возводит квадратную матрицу в mm-ую степень.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число mm.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела. """

""" Возведение в степень это умножение матрицы саму на себя n - раз.

В прошлом задание мы сделали умножение матриц.

А в этом уроке, нам надо просто повторить код из прошлого урока n-раз. 
 

Все. 

Я сделал функции:
Первая функция принимает ввод матрицы от пользователя.

Вторая функция умножает полученные матрицы друг на друга

Третья функция запускает вторую функцию n раз в цикле while уменьшая n каждый раз на 1.

Вот и весь перчик. 

Сложность возникнет только с третьей функцией.
Кстати если степень возведения будет 500-1000-1111111 т.е очень большой, то такой подход сжирает много ресурсов. Т.е тупое умножение матрицы на матрицу n раз, не лучший вариант. 
 """

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i])
        
# функция умножения матрицы саму на себя из предыдущего урока
def calc_matrix (matrix_name_1, matrix_name_2):
    n = len(matrix_name_1) #длинна строки Матрицы_1
    m = len(matrix_name_2[0]) #длинна строки Матрицы_2
    matrix_result = [[0]*m for _ in range(n)] # создаем матрицу куда будем записывать итоги
    for i in range(n):
        for j in range(m):
            for k in range(len(matrix_name_2)):
                matrix_result[i][j] += matrix_name_1[i][k] * matrix_name_2[k][j]# просто умножаем матрицы как в прошлом уроке
    return matrix_result

#Теперь нужна функция которая будет выполнять calc_matrix нужное кол-во раз
def calc_matrix_power(matrix_name, power):
    n = len(matrix_name)
    result = [[int(i==j) for i in range(n)] for j in range(n)] # создаем единичную матрицу
    while power > 0:# в цикле умножаем матрицу саму на себя n раз n уменьшаем каждый раз
        if power % 2 == 1:
            result = calc_matrix(result, matrix_name)
        matrix_name = calc_matrix(matrix_name, matrix_name)
        power //= 2
    return result


if __name__ == '__main__':
    #получаем матрицу А, ее длинну и степень    
    A,l=load_square_matrix()
    p=int(input())

    # запуск и печать
    print_matrix(calc_matrix_power(A,p),l)
