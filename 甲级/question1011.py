res = []
tmp = {0: 'W', 1: 'T', 2: 'L'}
for i in range(3):
    odds = [eval(x) for x in input().split(' ')]
    max = 0
    index = 0
    for j in range(3):
        if odds[j] > max:
            max = odds[j]
            index = j
    res.append((index, max))

profit = 1
result = []
for v in res:
    profit *= v[1]
    result.append(tmp[v[0]])

profit = (profit * 0.65 - 1) * 2
print(' '.join(result), end=' ')
print("{:.2f}".format(profit))
