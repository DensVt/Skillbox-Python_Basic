# Задача 1. Счётчик 2
#
# Как-то мы уже создавали декоратор counter, который считает и выводит количество вызовов декорируемой функции.
# Для этого мы использовали интересную особенность классов. В этот раз реализуйте тот же декоратор,
# но уже с использованием знаний о локальных и глобальных переменных.
#
# Реализуйте декоратор двумя способами:
#
# используя глобальную переменную count;
# используя локальную переменную count внутри декоратора.
#
#
# Дополнительно: найдите команду (в интернете или даже сами), которая перечисляет все функции и методы,
# находящиеся во встроенном пространстве имён в Python.
# Результат выполнения команды:
#
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__'  ну и так далее.


global_count = {}

def decorator_counter(func):
	def wrapped_func(*args, **kwargs):
		wrapped_func.count += 1
		global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
		return func(*args, **kwargs)
	wrapped_func.count = 0
	return wrapped_func

@decorator_counter
def hello():
	print("Hello")

@decorator_counter
def hello_2():
	print("Hello")

print(global_count, hello.count, hello_2.count)
hello()
print(global_count, hello.count, hello_2.count)
hello_2()
print(global_count, hello.count)

print('*' * 100)
print(dir('.'))

