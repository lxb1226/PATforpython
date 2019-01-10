# A = list(map(float,input().split()))
# B = list(map(float,input().split()))

# m = int(A[0])
# n = int(B[0])
# res = [0]
# i = j = 1
# while i <= 2*m and j <= 2*n:
#     if A[i] > B[j]:
#         res.append(A[i])
#         res.append(A[i+1])
#         i += 2
#     elif A[i] == B[j]:
#         res.append(A[i])
#         res.append(A[i+1] + B[j+1])
#         i += 2
#         j += 2
#     else:
#         res.append(B[j])
#         res.append(B[j+1])
#         j += 2
# if i == 2*m:
#     for x in range(j,2*n,2):
#         res.append(B[x])
#         res.append(B[x+1])    
# else:
#     for y in range(i,2*m,2):
#         res.append(A[y])
#         res.append(A[y+1])


# res[0] = len(res)//2
# # print(res)
# for x in res[:-1]:
    
#     print(x,end=' ')
# print(res[-1],end='')

A = [eval(i) for i in input().split()[1:]]
B = [eval(i) for i in input().split()[1:]]
d = {}
for i in range(0,len(A),2):
    d[A[i]] = d.get(A[i],0) + A[i+1]

for i in range(0,len(B),2):
    d[B[i]] = d.get(B[i],0) + B[i+1]

for i in list(d.keys()):
    if d[i] == 0:
        del d[i]

d = sorted(d.items(),key=lambda x:x[0],reverse=True)
print(len(d),end='')
for x,y in d:
    print(" {} {:.1f}".format(x,y),end="")
