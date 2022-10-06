#! python

arr_raw = []
arr_cycl = []

while 0 == 0:
    p_start = input('Write start point of segment ')
    p_end = input('Write end point of segment ')
    if p_start == '' or p_end == '':
        break
    p_start = int(p_start)
    p_end = int(p_end)
    if p_start <= p_end:
        arr_cycl = list(range(p_start, p_end + 1))
    else:
        arr_cycl = list(range(p_end, p_start + 1))
    arr_raw.extend(arr_cycl)
    #print('arr_cycl is ', arr_cycl, 'arr_raw is ', arr_raw)

sss = set(arr_raw)

while sss != set():
    min = 0
    #print('sss_before', sss)
    for f in range(1, len(arr_raw)):
        if arr_raw[min] < arr_raw[f]:
            continue
        else:
            min = f
    #print('arrmin', arr_raw[longest])

    var = int(arr_raw[min])
    for i in range(0, len(arr_raw)):
        for f in range(0, len(arr_raw)):
            if var + 1 == arr_raw[f]:
                var = int(arr_raw[f])
                #print('var', var)

    print('longest', arr_raw[min], 'max', var)
    found_segment = list(range(arr_raw[min], var + 1))
    #print('found_segment', found_segment)
    sss2 = set(found_segment)
    sss = sss - sss2
    #print('sss_after', sss)
    arr_raw = list(sss)
    #print('arr_after', arr_raw)