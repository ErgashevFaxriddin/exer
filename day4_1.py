def login_check(username, password):
    saved_username = 'admin'
    saved_password = 'admin1234'

    if username == saved_username and password == saved_password:
        return True
    else:
        return False

while True:
    user = input('LOGIN: ')
    pwd = input('PASSWORD: ')

    if login_check(user, pwd):
        print('LOGGED IN SUCCESSFULLY!')
        break
    else:
        print('WRONG USER OR PASSWORD')