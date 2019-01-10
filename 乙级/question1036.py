
N,a = input().split(' ')

N = int(N)
if N % 2 == 1:
    row  = N //2 + 1
else:
    row = N//2

print(a*N)
for i in range(1,row-1):
    for j in range(N):
        if j == 0 or j == N - 1:
            print(a,end='')
        else:
            print(' ',end='')
        if j == N - 1:
            print()
print(a*N)