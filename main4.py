from day4 import add_teacher, conn

while True:
    name = input('YOUR NAME: ')

    while True:
        age = input('YOUR AGE: ')
        if age.isdigit():
            age = int(age)
            break
        else:
            print("PLEASE, ENTER YOUR AGE: ")

    subject = input('YOUR SUBJECT: ')

    add_teacher(name, age, subject)

    ask = int(input('RO\'YXATNI DAVOM ETTIRASIZMI? \nHa: 1 \nYo\'q: 0\n>>>'))
    if ask == 1:
        continue
    else:
        break

conn.close()
print('SAVED!')