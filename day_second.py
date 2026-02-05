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

print("WELCOME TO THE GAME😊")
while True:

    sentence = input('WRITE ANY SENTENCES: ')
    words = sentence.split()
    print("YOU WROTE", len(words), "WORDS")

    again = input('WANNA PLAY AGAIN? (YES/NO)')

    if again == 'YES'.lower():
        continue
    else:
        print('THANK YOU!🫶')
        break
