# 解法一：
a, b = map(int, input().split())
res = []
sum = a + b
flag = False
if sum < 0:
    flag = True
    sum = abs(sum)
s = str(sum)
for i in range(len(s) - 1, -1, -3):
    if i < 2:
        res.append(s[:i + 1])
    else:
        res.append(s[i - 2:i + 1])
if flag:
    res[-1] = '-' + res[-1]
print(','.join(res[::-1]), end='')

# 解法二：
# a,b = map(int,input().split())
# print(format(a+b,','))
