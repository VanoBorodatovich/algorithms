#! python

# https://habr.com/ru/post/142589/


def hs(seq, alphab, value):
    # делаем из строки кортеж чисел
    s = []
    for f in seq:
        ind = alphab.index(f)
        s.append(value[ind])
    s = tuple(s)

    # задаём переменные полиномиальной ф
    p = len(alphab) + 1

    # создаём массив степеней
    p_pow = [1]
    for f in range(1, len(seq)):
       p_pow.append(p_pow[f - 1] * p)

    # считаем хеши префиксов строки
    hsh = [s[0]]
    for f in range(1, len(s)):
        hsh.append(hsh[f - 1] + p_pow[f] * s[f])
    # возвращает два массива по кот потом быстровычисляются хэши двух любых подстрок
    return p_pow, hsh


def hash_of_substr(p_pow: list, hsh: list, start: int, end: int):
    m = (10 ** 5) + 9
    if start > len(p_pow) or end >= len(p_pow):
        return 'stopped'
    if start == 0:
        return hsh[end]
    else:
        return ((hsh[end] - hsh[start - 1]) / p_pow[start]) % m # на хабре написано что почему-то надо умножать(( на pstart
    # а деление по модулю и так автомотическое при превышении 2 ^ 64


def func(seq, length, alphab, value):
    arr1 = [] # массив для хэшей
    arr2 = [] # массив с массивами для коллизий и статистики
    for f in range((10 ** 5) + 9):
        arr2.append([])
    start = 0
    p_pow, hsh = hs(seq, alphab, value)
    #print('prehash', p_pow, hsh)
    while length <= len(seq):
        k_mer = seq[start: length] # сам кмер
        #print('>position is ', start + 1)
        k_hsh = hash_of_substr(p_pow, hsh, start, length - 1) # хеш для него
        if k_hsh not in arr1:
            #print(k_hsh, ' not found')
            position = len(arr1)
            arr1.append(k_hsh)
            #print('hash table ', arr1)
            arr2[position].append(k_mer)
            arr2[position].append(start + 1)# первое вхожден
            arr2[position].append(start + 1)# последнее
            arr2[position].append(start + 1)# сумма
            arr2[position].append(1)# количество
            #print('arr2 ', arr2[position])
        else:
            #print(k_hsh, ' HASH FOUND')
            ind1 = arr1.index(k_hsh)
            if k_mer not in arr2[ind1]:
                #print('collision!!!')
                arr2[ind1].append(k_mer)
                arr2[ind1].append(start + 1)
                arr2[ind1].append(start + 1)
                arr2[ind1].append(start + 1)
                arr2[ind1].append(1)
            else:
                ind2 = arr2[ind1].index(k_mer)
                arr2[ind1][ind2 + 2] = start + 1
                arr2[ind1][ind2 + 3] = arr2[ind1][ind2 + 3] + start + 1
                arr2[ind1][ind2 + 4] = arr2[ind1][ind2 + 4] + 1
                #print('POVTOR', arr2[ind1])
        start += 1
        length += 1
    # отображение
    f = 0
    while True:
        if not arr2[f]:
            break
        elif len(arr2[f]) == 4:
            print(arr2[f][0], '  ', arr2[f][1], '  ',  arr2[f][2], '  ', arr2[f][4], '  ', arr2[f][3] / arr2[f][4])
        else:
            for i in range(0, len(arr2[f]), 5):
                print(arr2[f][i], '  ', arr2[f][i + 1], '  ', arr2[f][i + 2], '  ', arr2[f][4], '  ', arr2[f][i + 3] / arr2[f][i + 4])
        f += 1


if __name__ == '__main__':
    import re

    i = str(input('file must lie in project1: '))
    leng = int(input('The length of K-mer: '))
    f = open(i, 'r')
    lines = f.readlines()
    lre = re.compile('^(\S+)$')
    seq = lre.search(lines[1])
    alphab = ['A', 'T', 'G', 'C']
    value = [1, 2, 3, 4]

    func(seq.group(1), leng, alphab, value)




