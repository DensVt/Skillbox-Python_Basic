routes = {}


def callback(url):
    def decorator(func):
        routes[url] = func

        def wrapper():
            return func()
        return wrapper
    return decorator


def get(url):
    return routes.get(url)


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
