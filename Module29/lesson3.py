# Задача 1. Createtime
#
# Реализуйте декоратор класса, который выдаёт дату и время создания, а также список всех методов объекта класса каждый раз,
# когда объект класса создаётся в основном коде.

import datetime

def decorator(cls):
	def wrapper(*args, **kwargs):
		instance = cls(*args, **kwargs)

		print("Время создания -", datetime.datetime.now())
		print("Методы: ", end=" ")
		for i_method in dir(cls):
			if i_method.startswith('__'):
				continue
			print(i_method, end=' ')
		print()
		return instance
	return wrapper

@decorator
class Example:
	def hello(self):
		print("Hello")
	def hello_2(self):
		print("Hello")

Example()
Example()