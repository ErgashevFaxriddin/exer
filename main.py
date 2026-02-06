from day_third import add_user, conn

name = input('enter name: ')
add_user(name)

conn.close()
print('saved!')