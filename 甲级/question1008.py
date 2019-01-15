floors = [int(x) for x in input().split(' ')]
N = floors[0]
floors[0] = 0
total_time = 0

for i in range(N):
    diff = floors[i + 1] - floors[i]
    if diff > 0:
        total_time += 6 * diff
    else:
        total_time -= 4 * diff

total_time += 5 * N

print(total_time)
