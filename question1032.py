


N = int(input())

scores = [(input().split(' ')) for i in range(N)]
# scores = [
#     [3,65],
#     [2,80],
#     [1,100],
#     [2,70],
#     [3,40],
#     [3,0]
# ]
d = {}
for i in range(len(scores)):
    d[scores[i][0]] = d.get(scores[i][0],0) + int(scores[i][1])
res = sorted(d.items(),key=lambda x:x[1])[-1]
print("{} {}".format(res[0],res[1]))


