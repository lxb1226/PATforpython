
d = {0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
w = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]



nums = [
    '320124198808240056',
    '12010X198901011234',
    '110108196711301866',
    '37070419881216001X'
]

# nums = [
#     '320124198808240056',
#     '110108196711301862'
# ]

# N = int(input())
# nums = [input() for i in range(N)]
flag = False
for num in nums:
    if num[:-1].isdigit():
        value = 0
        for i in range(len(num[:-1])):
            value += int(num[i]) * w[i]
        z = value % 11
        if d[z] != num[-1]:
            flag = True
            print(num)
    else:
        flag = True
        print(num)
if  not flag:
    print("All passed")




