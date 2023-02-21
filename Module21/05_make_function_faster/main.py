# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result




from math import factorial, pow

def calc(data):
    return pow((factorial(data) / pow(data, 3)), 10)

print(calc(10))




"""
def calc_f(num):
    if num in factorials:
        res = factorials[num]
    else:
        res = max(factorials.values())
        for index in range(max(factorials.keys()) + 1, num + 1):
            res *= index
            factorials[index] = res
    res /= num ** 3
    res = res ** 10
    return res


factorials = {1: 1}
print(calc_f(10))
"""