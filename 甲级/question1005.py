s = input()

temp = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
        '8': 'eight', '9': 'nine'}
sum = 0
res = []
for i in range(len(s)):
    sum += int(s[i])
sum = str(sum)
for j in range(len(str(sum))):
    res.append(temp[sum[j]])

print(' '.join(res), end='')
# print(sum)
