#! python

# input
arr = []
while 0 == 0:
    latitude = input('latitude ')
    longitude = input('longitude ')
    if latitude == '' or longitude == '':
        break
    latitude = float(latitude)
    longitude = float(longitude)
    if latitude > 90 or latitude < -90 or longitude > 180 or longitude < -180:
        print('There is not such place on the Earth ')
        continue
    arr_cycl = [latitude, longitude]
    arr.append(arr_cycl)

# is this step needed?
#arr = [55.813949, 37.663833], [54.203344, 37.850854], [52.989674, 49.913877], [56.148962, 44.239890], [54.780190, 55.821042], [58.134365, 56.287397], [57.133909, 65.769952], [48.713038, 44.550793], [55.315703, 61.520937], [53.691432, 55.608373]]
for f in range(0, len(arr)):
    arr[f] = tuple(arr[f])

# making a dictionary
dic = {}
for f in range(0, len(arr)):
    dic[arr[f]] = 1

# count number of neighborhoods
for f in range(0, len(arr)):
    ant = arr[f]
    for i in range(f + 1, len(arr)):
        post = arr[i]
        if ant[0] - post[0] < 5 and ant[0] - post[0] > -5 and ant[1] - post[1] < 5 and ant[1] - post[1] > -5:
            dic[ant] += 1
            dic[post] +=1
            # для того, чтобы оставлять только одну точку из двух координаты второй в массиве можно заменить на (300, 300)

# search for higher
higher =0
for f in dic:
    if dic[f] > higher:
        higher = dic[f]
        place = f

print(higher, place)