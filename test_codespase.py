# from functools import reduce
# import operator

# def flatten(data):
#     return reduce(operator.concat, data, [])

# result = flatten([[1, 2], [3, 4], [], [5]])

# print(result)

# def product_of_odds(data):   # data - список целых чисел
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result

def arithmetic_operation(operation):
    def f(a,b):
        if operation=='-':
            return a-b
        elif operation =='+':
            return a+b
        elif operation =='*':
            return a*b        
        else:
            return a+b
    return f    
add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))        