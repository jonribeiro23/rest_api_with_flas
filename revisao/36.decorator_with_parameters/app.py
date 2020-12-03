from functools import wraps
user = {'username': 'Joe', 'access_level': 'admin'}


def make_secure(access_level):
    def decorator(func):
        @wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return 'Not allowed'
        return secure_function
    return decorator


@make_secure('admin')
def get_password():
        return '1234'


@make_secure('guest')
def get_dashboard_password():
    return 'User: user password'


print(get_password())
print(get_dashboard_password())