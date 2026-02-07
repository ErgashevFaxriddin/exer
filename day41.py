def login_check(username, password):
    saved_username = 'admin'
    saved_password = 'admin1234'

    if username == saved_username and password == saved_password:
        return 'logged in successfully'
    else:
        return 'login failed'

user = input('login: ')
pwd = input('password: ')
result = login_check(user, pwd)
print(result)