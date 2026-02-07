from day_third import add_student, conn

name = input('enter name: ')
age = int(input('enter oyur age: '))
add_student(name, age)

conn.close()
print('saved!')