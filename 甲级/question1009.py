A = [eval(i) for i in input().split()[1:]]
B = [eval(i) for i in input().split()[1:]]

d = {}
for i in range(0, len(A), 2):
    for j in range(0, len(B), 2):
        d[A[i] + B[j]] = d.get(A[i] + B[j], 0) + A[i + 1] * B[j + 1]

for i in list(d.keys()):
    if d[i] == 0:
        del d[i]

d = sorted(d.items(), key=lambda x: x[0], reverse=True)
print(len(d), end='')
for x, y in d:
    print(" {} {:.1f}".format(x, y), end="")
