#! python

print('Print nothing for exit ')
a = 0
arr = []
while a != '':
    a = input('Put your number here (only integers, please): ')
    if a == '':
        break
    else:
        a = int(a)
        arr.append(a)

arr_even = []
arr_odd = []
count = 0

for f in range(1, len(arr) + 1):
    if arr[count] % 2 == 0:
        arr_even.append(arr[count])
        count += 1
    else:
        arr_odd.append(arr[count])
        count += 1

count2 = 0
while count2 < len(arr_even) or count2 < len(arr_odd):
    if count2 >= len(arr_even):
        print(arr_odd[count2])
    elif count2 >= len(arr_odd):
        print(arr_even[count2])
    else:
        print(arr_even[count2], arr_odd[count2])
    count2 += 1
