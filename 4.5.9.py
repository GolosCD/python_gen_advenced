""" Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 1, 2, 3, \ldots, n^21,2,3,…,n 
2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
 """
""" Пример функционального подхода к решению задачи.
Создаю три мелких функций которые проверяют отдельные части матрицы.
если в конце все выдали True то печатаем YES """

# новая функция загрузки квадратных матриц
def load_square_matrix():
    final_list=[[int(i) for i in input().split()] for _ in range(int(input()))]
    return final_list,len(final_list)   

# функция печати матриц с распаковкой строк
def print_matrix(matrix_name,matrix_lenght):
    for i in range(matrix_lenght):
        print(*matrix_name[i])

#Функция проверки элементов матрицы        
def check_element(matrix_name,matrix_lenght):
    flag_true_false = True # создаем флаг который всегда Истина
    # в список а я распаковываю матрицу, что бы потом проверить на повторыне элементы
    a=list()
    #проверяем что элементы матрицы всегда в диапазоне от 1 до n**2
    for i in range(matrix_lenght):
        for j in range(matrix_lenght):
            a.insert(0,matrix_name[i][j])
            if matrix_name[i][j] not in range(1,(matrix_lenght**2)+1):
                #print('matrix_name[i][j]:>> ',matrix_name[i][j])
                #print('range(1,matrix_lenght**2):>> ',range(1,(matrix_lenght**2)+1))
                flag_true_false= False
                break #если найден хоть один элемент который не в диапазоне, то меняем флаг и стопаем цикл
            # если в матрице хоть один элемент встречается больше 1 раза, то она не магическая    
            if a.count(matrix_name[i][j])>1:
                flag_true_false= False
                break
        
    return flag_true_false            
                
# функция проверки что сумма чисел по диагоналям равна        
def calc_matrix_diagonal(matrix_name,matrix_lenght):
    main_diag_matrix=0
    second_diag_matrix=0
    for i in range(matrix_lenght):
        for j in range (matrix_lenght):
            if i==j:
                main_diag_matrix+=matrix_name[i][j]
    #print('main_diag_matrix',main_diag_matrix) 
    
    for i in range(matrix_lenght):
        for j in range (matrix_lenght):        
            if j==matrix_lenght-i-1:
                second_diag_matrix+=matrix_name[i][j]
    #print('second_diag_matrix',second_diag_matrix)            
    return main_diag_matrix==second_diag_matrix

# функция проверки что сумма по строкам и столбцам сходится.
def calc_matrix_row_col(matrix_name,matrix_lenght):
    falg_true_false = True
    one_sum=sum(matrix_name[0])
    #print('one_sum:>> ',one_sum)
    #print('matrix_name[0]:>> ',matrix_name[0])
    for i in range(matrix_lenght):
        sum_col=0
        if one_sum!=sum(matrix_name[i]):
            #print('sum(matrix_name[i]):>> ',sum(matrix_name[i]))
            falg_true_false = False
            break
        for j in range(matrix_lenght):
            sum_col+=matrix_name[j][i]
                      
        if one_sum!=sum_col:
            #print('sum_col:>> ',sum_col)
            falg_true_false =False
            break
    return falg_true_false                      
                    
    

if __name__ == '__main__':
    
    sqm,lsqm=load_square_matrix()
    flag_result ='NO'
    #print('calc_matrix_diagonal:>> ',calc_matrix_diagonal(sqm,lsqm))
    #print('check_element:>> ',check_element(sqm,lsqm))
    #print('calc_matrix_row_col:>> ',calc_matrix_row_col(sqm,lsqm))
    if calc_matrix_diagonal(sqm,lsqm) and check_element(sqm,lsqm) and calc_matrix_row_col(sqm,lsqm):
        flag_result = 'YES'
    print(flag_result) 