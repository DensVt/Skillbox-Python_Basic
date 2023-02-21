def func(*args):
    def flatten(a_list):
        result = []
        for elem in a_list:
            if isinstance(elem, int):
                result.append(elem)
            else:
                result.extend(flatten(elem))
        return result

    return sum(flatten(args))


print("Ответ в консоли: ", func([[1, 2, [3]], [1], 3]))
print("Ответ в консоли: ", func(1, 2, 3, 4, 5))

"""
from typing import Iterable

def func(*args):
    return sum(func(*arg) if isinstance(arg, Iterable) else arg for arg in args)

print("Ответ в консоли: ", func([[1, 2, [3]], [1], 3]))
print("Ответ в консоли: ", func(1, 2, 3, 4, 5))
"""

"""
import re

def func(*args):
    return sum(map(int, re.findall(r'\d+', str(args))))

print("Ответ в консоли: ", func([[1, 2, [3]], [1], 3]))
print("Ответ в консоли: ", func(1, 2, 3, 4, 5))
"""

"""
# регулярка

import re

def func(*args):
    return sum(map(float, re.findall(r'\d*\.?\d+', str(args))))

print("Ответ в консоли: ", func([[1.2, 2.1, [3.3]], [1], 3]))
print("Ответ в консоли: ", func(1, 2, 3.2, 4, 5.1))
"""
