#! python
a = int(input('put your length here: ')) #длинна строки
c = int(input('put your height here: ')) #сколько строк (шаг)
num_out = 0
string = ''

for f1 in range(1, c + 1):
    num_out += 1
    num_in = num_out
    for f2 in range(1, a + 1):
        num_in = str(num_in)
        string += num_in
        string += ' '
        num_in = int(num_in)
        num_in += c
        #print('str', string, 'num', num)
    print(string)
    string = ''
