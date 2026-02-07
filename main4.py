from day4 import *

name = input('YOUR NAME: '.title())
age = int(input('YOUR AGE: '))
subject = input('YOUR SUBJECT: ')

add_teacher(name, age, subject)

conn.close()
print('SAVED!')