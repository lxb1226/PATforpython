
nums = [x.split('/') for x in input().split(' ')]

a1,b1  = list(map(int,nums[0]))
a2,b2 = list(map(int,nums[1]))

sum = a1*b2 + a2*b1
value = sum % (b1*b2)
