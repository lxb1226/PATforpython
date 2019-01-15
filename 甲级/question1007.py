def maxSum(A, N):
    left_index = 0
    right_index = N - 1
    sum = -1
    temp = 0
    temp_index = 0
    for i in range(N):
        temp += A[i]
        if temp < 0:
            temp = 0
            temp_index = i + 1
        elif temp > sum:
            sum = temp
            left_index = temp_index
            right_index = i
    if sum < 0:
        sum = 0
    print(sum, left_index, right_index)


if __name__ == '__main__':
    # A = [-10,0,1,2,3,4,-5,-23,3,7,-21]
    # A = [-10,0,-2,-3,-4,-5,-23,-3,-7,-21]
    # A =[-1,0,0,-1]
    N = int(input())
    A = [int(x) for x in input().split(' ')]
    maxSum(A, len(A))
