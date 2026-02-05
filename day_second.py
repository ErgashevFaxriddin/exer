# num = -9
# if num > 0:
#     print('--->')
# else:
#     print('<---')

# word = input('write any word: \n>>>')
# print(f"you wrote {len(word)} letters")

# sentence = input('write any sentence: ')
# words = sentence.split()
# print("you wrote", len(words), "words")
#
# ______________________________________
# print("WELCOME TO THE GAME😊")
# while True:
#
#     sentence = input('WRITE ANY SENTENCES: ')
#     words = sentence.split()
#     print("YOU WROTE", len(words), "WORDS")
#
#     again = input('WANNA PLAY AGAIN? (YES/NO)')
#
#     if again == 'YES'.lower():
#         continue
#     else:
#         print('THANK YOU!🫶')
#         break

# ___________________________________________
# import sqlite3  # sqlite3 kutubxonasini chaqiramiz, SQLite database bilan ishlash uchun
#
# # Database bilan ulanish
# conn = sqlite3.connect("people.db")  # "people.db" nomli database faylini yaratadi yoki unga ulanadi
# c = conn.cursor()  # SQL so‘rovlarini bajarish uchun cursor yaratamiz
#
# # Jadval yaratish
# c.execute("CREATE TABLE IF NOT EXISTS people(first TEXT, last TEXT, age INTEGER)")
# # Jadvalni yaratadi, agar mavjud bo‘lmasa:
# # first – ism, matn turi (TEXT)
# # last – familiya, matn turi (TEXT)
# # age – yosh, butun son (INTEGER)
#
# # Foydalanuvchi ma'lumot kiritadi
# f = input("WRITE YOUR FIRST NAME: ")  # foydalanuvchidan ism so‘raymiz
# l = input("WRITE YOUR LAST NAME: ")   # foydalanuvchidan familiya so‘raymiz
# a = int(input("WRITE YOUR AGE: "))    # foydalanuvchidan yosh so‘raymiz va butun songa aylantiramiz
#
# # Database-ga saqlash
# c.execute("INSERT INTO people VALUES(?, ?, ?)", (f, l, a))
# # INSERT – jadvalga yangi satr qo‘shadi, ? o‘rniga qiymatlar ketma-ket joylanadi
# conn.commit()  # o‘zgarishlarni database-ga saqlaymiz
#
# # Hammasini ko‘rsatish
# for row in c.execute("SELECT * FROM people"):  # jadvaldagi barcha satrlarni oladi
#     print("FIRST:", row[0], "| LAST:", row[1], "| AGE:", row[2])
#     # row[0] – first (ism)
#     # row[1] – last (familiya)
#     # row[2] – age (yosh)
#
# # Bog‘lanishni yopish
# conn.close()  # database bilan bog‘lanishni yopamiz
#
# ________________________________________________________________________________________________
import sqlite3

# Bazaga ulanish va cursor yaratish
conn = sqlite3.connect('people.db')
c = conn.cursor()

# Jadval mavjud bo'lmasa yaratish
c.execute('''
CREATE TABLE IF NOT EXISTS people (
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
''')
conn.commit()

while True:
    f = input("WRITE YOUR FIRST NAME: ")
    l = input("WRITE YOUR LAST NAME: ")

    # Age ni to'g'ri kiritish uchun tekshiruv
    while True:
        try:
            a = int(input("WRITE YOUR AGE: "))
            break
        except ValueError:
            print("Please enter a valid number for age.")

    c.execute("INSERT INTO people VALUES (?, ?, ?)", (f, l, a))
    conn.commit()

    again = input("Do you want to add another person? (yes/no): ").lower()
    if again != "yes":
        break

conn.close()
print("Data entry finished!")
