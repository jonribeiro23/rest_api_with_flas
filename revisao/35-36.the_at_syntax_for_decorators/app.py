from functools import wraps
user = {'username': 'Joe', 'access_level': 'admin'}


def make_secure(func):
    @wraps(func)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return 'Not allowed'
    return secure_function


@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure_pasword'
# when I use a decorator, the function in wich it is used,
# lost its name. get_admin_password() become secure_function()
# To solve this I need to use wraps. So it maintain its name.


# get_admin_password = make_secure(get_admin_password)
print(get_password('billing'))

