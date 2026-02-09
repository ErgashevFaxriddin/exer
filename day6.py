# add = lambda a, b : a + b
# print(add(1,2))

# multiply = lambda a, b: a *b
# x = int(input('first digit: '))
# y = int(input('second digit: '))
# print(x, 'x', y, '=', multiply(x, y))

# check = lambda x: 'positive' if x>0 else 'negativ or zero'
# n = int(input('enter a number: '))
# print(check(n))

# blue = "\033[94m"
# red = "\033[91m"
# reset = "\033[0m"
#
# while True:
#     try:
#         check = lambda x: f"{blue}POSITIVE{reset}" if x>0 else f"{red}NEGATIVE OR ZERO{reset}"
#
#         n = int(input('ENTER A NUMBER: '))
#         print(check(n))
#
#         count = int(input('WANNA CONTINUE?\n(1 / 0)\n>>>'))
#         if count != '1':
#             break
#
#     except ValueError:
#         print(f"{red}VALUE ERROR!\n PLEASE ENTER A NUMBER}!{reset}")
#
blue = "\033[94m"
red = "\033[91m"
reset = "\033[0m"

while True:
    try:
        check = lambda x: f"{blue}POSITIVE{reset}" if x>0 else f"{red}NEGATIVE OR ZERO{reset}"

        n = int(input('ENTER A NUMBER: '))
        print(check(n))

        count = int(input('WANNA CONTINUE?\n(1 / 0)\n>>>'))
        if count != int(1):
            break

    except ValueError:
        print(f"{red}VALUE ERROR!\n PLEASE ENTER A NUMBER!{reset}")
