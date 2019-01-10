

# A = [10,16,27]
# P = [14,1,28]
P,A = input().split(' ')
P = list(map(int,P.split('.')))
A = list(map(int,A.split('.')))
tmp = [0,17,29]


num = 0
res = []
flag = False
if A < P:
    P,A = A,P
    flag = True


for i in range(len(A)-1,-1,-1):
    if A[i] + num >= P[i]:
        res.append(str(A[i] + num - P[i]))
        num = 0
    else:
        res.append(str(A[i] + tmp[i] + num - P[i]))
        num = -1
if flag:
    res[2] = '-' + res[2]

print('.'.join(res[::-1]))






