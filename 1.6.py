'''
Дано пятизначное или шестизначное натуральное число. 
Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
'''
def reverc_five(dig):
    if len(str(dig))<=5:
        print(int(str(dig)[::-1]))
    else: 
        print(int(str(dig)[:-5]+str(dig)[:-6:-1]))

    
y = int(input())

reverc_five(y)