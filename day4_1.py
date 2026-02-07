saved_username = 'admin'
saved_password = 'admin1234'

max_attempts = 3
attempts = 0

def login_check(username, password):

    if username == saved_username and password == saved_password:
        return True
    else:
        return False

while attempts < max_attempts:
    user = input('LOGIN: ')
    pwd = input('PASSWORD: ')

    if login_check(user, pwd):
        print('LOGGED IN SUCCESSFULLY!')
        break
    else:
        attempts += 1
        print(max_attempts - attempts, 'ATTEMPTS LEFT')
        if attempts == 1:
            print('max_attempts - attempts', 'ATTEMPT LEFT')

        print('LOG IN FAILED\nTRY AGAIN: ')
if attempts == max_attempts:
    print('TOO MANY FAILED ATTEMPTS\nTRY AGAIN LATER')