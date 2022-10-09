#! python

import string

dic_in = {}
count = 10
for f in string.ascii_uppercase:
  dic_in[f] = count
  count += 1
for f in range(10):
    dic_in[str(f)] = f

dic_out = {}
for f in range(0, 10):
    dic_out[f] = str(f)
count = 0
for f in range(10, 36):
    dic_out[f] = string.ascii_uppercase[count]
    count += 1


def to_decimal(num, base):
    count = 0
    num_in_dec = 0
    for f in range(len(num) -1, -1, -1):
        num_in_dec += dic_in[num[f]] * base ** count
        count += 1
    print('num_in _dec = ', num_in_dec)
    return num_in_dec


def to_oth(num_in_dec, new_base):
    in_oth = ''
    while num_in_dec % new_base != num_in_dec:
        in_oth += dic_out[num_in_dec % new_base]
        num_in_dec = num_in_dec // new_base
        if num_in_dec % new_base == num_in_dec:
            in_oth += dic_out[num_in_dec]

    num_in_oth = ''
    for f in range(len(in_oth) - 1, -1, -1):
        num_in_oth += in_oth[f]
    return num_in_oth


def funny_add(num1, num2, base, new_base):
    allright = num1 + num2
    bl = True
    for f in allright:
        if dic_in[f] >= base:
            bl = False
            print('are you okey with it ?? ', f)
    if bl == True:
        a = to_decimal(num1, base)
        b = to_decimal(num2, base)
        c = a + b
        return to_oth(c, new_base)


# input
base = int(input('Please, input your current base '))
num1 = (input('Your first number here, pls: '))
num2 = (input('And the second one: '))
new_base = int(input('The base of number system for out: '))
print(funny_add(num1, num2, base, new_base))