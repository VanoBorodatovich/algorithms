#! python

arr_raw = []
arr_cycl = []

# input and creating arr of segmants
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
    arr_raw.append(arr_cycl)
    print('arr_cycl is ', arr_cycl, 'arr_raw is ', arr_raw)

trr_inp = tuple(arr_raw)

# intersection of all segments
for f in range(0, len(arr_raw)):
    for i in range(f + 1, len(arr_raw)):
        if (set(arr_raw[i]) & set(arr_raw[f])) != set():
            # print('f=', f, arr_raw[f], 'i=', i, arr_raw[i])
            new_seg = list((set(arr_raw[i]) | set(arr_raw[f])))
            arr_raw[i] = new_seg
            # print('arr_raw', arr_raw)

# search for longest
longest = 0
for f in range(1, len(arr_raw)):
    if len(arr_raw[f]) > len(arr_raw[longest]):
        longest = f
# print('longest', arr_raw[longest])
# print('trr_inp', trr_inp)
lng = set(arr_raw[longest])
# print('lng', lng)

# count coverage
count = 0
for f in range(0, len(trr_inp)):
    if (lng & set(arr_raw[f])) != set():
        count += 1
print('fuckin coverage is ', count, ' for the fuckin longest (or the first of those that have the greatest length) segment: ', lng)