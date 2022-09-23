#! python
a = int(input('put your number here: '))
count = 0

if a == 1:
    num1, num2 = 1, 1
else:
    for f in range(1, a + 1):
        for d in range(1, f + 1):
            if f % d != 0 and d != f:
                continue
            if f % d == 0 and f != d and d != 1:
                break
            if f / d == 1:
                count += 1
                if count % 2 != 0: #odd
                    num1 = f
                    #print('num1 is ', num1, count)
                if count % 2 == 0: #even
                    num2 = f
                    #print('num2 is ', num2, count)
print(num1, num2)

count2 = 0
while count2 < 7:
    num1 = num1 + num2
    print(num1)
    if count2 < 6:
        num2 = num1 + num2
        print(num2)
    count2 += 1
