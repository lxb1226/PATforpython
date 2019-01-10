
#
N = int(input())
scores = list(input().split(' '))
Searched = list(input().split(' '))
K = int(Searched[0])

# N = 10
# scores = [60,75,90,55,75,99,82,90,75,50]
# Searched = [3,75,90,88]
# K = Searched[0]
tmp = {x: 0 for x in Searched[1:]}

for score in scores:
    if score in tmp.keys():
        tmp[score] += 1

cnt = 0
for v in tmp.values():
    cnt += 1
    if cnt == K:
        break
    print("{} ".format(v),end='')

print('{}'.format(list(tmp.values())[-1]),end='')




