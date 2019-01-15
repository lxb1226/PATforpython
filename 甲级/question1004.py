def dfs(node, res, index, depth):
    global maxDepth
    if len(node[index]) == 0:
        res[depth] += 1
        if maxDepth < depth:
            maxDepth = depth
        return
    for i in range(len(node[index])):
        dfs(node, res, node[index][i], depth + 1)


M, N = [int(x) for x in input().split(" ")]
node = [[] for _ in range(100)]
res = [0 for _ in range(100)]
maxDepth = 0
for i in range(N):
    temp = [int(x) for x in input().split(' ')]
    ID = temp[0]
    K = temp[1]
    node[int(ID)] = temp[2:]
# print(node)

dfs(node, res, 1, 0)
for i in range(maxDepth):
    print(res[i], end=" ")
print(res[maxDepth], end="")
