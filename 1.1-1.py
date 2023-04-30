'''
На вход программе подаются два целых числа aa и bb. Напишите программу, которая выводит:

сумму чисел aa и bb;
разность чисел aa и bb;
произведение чисел aa и bb;
частное чисел aa и bb;
целую часть от деления числа aa на bb;
остаток от деления числа aa на bb;
корень квадратный из суммы их 1010-х степеней: \sqrt{a^{10} + b^{10}} a 10 +b 10 ​
'''
import math as m

def calc(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = float(x)/y
    e = x//y
    i = x%y
    j = m.sqrt(x**10+y**10)
    return a,b,c,d,e,i,j

n1 = int(input())
n2 = int(input())

l = list(calc(n1,n2))

print(*l,sep='\n')