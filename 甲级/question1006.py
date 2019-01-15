def transtime(time):
    h, m, s = [int(x) for x in time.split(':')]
    total_time = h * 3600 + m * 60 + s
    return total_time


N = int(input())
records = {}
for _ in range(N):
    ID, signin, signout = input().split(' ')
    records[ID] = (transtime(signin), transtime(signout))

max = 0
min = 1000000
for k, v in records.items():
    if v[0] < min:
        min = v[0]
        idIn = k
    if v[1] > max:
        max = v[1]
        idOut = k

print(idIn, idOut)
