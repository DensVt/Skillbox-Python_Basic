user_permissions = ['admin']


def check_permission(required_permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if required_permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(
                    "У пользователя недостаточно прав, чтобы выполнить функцию {}".format(func.__name__))
        return wrapper
    return decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


try:
    delete_site()
    add_comment()
except PermissionError as exc:
    print("PermissionError: {}".format(str(exc)))
