
# s = '7+IE.'
# s1 = '7_This_is_a_test.'
s = input()
s1 = input()

res = ''
for x in s1:
    if x.isupper() and '+' in s:
        continue
    elif x.lower() and x.upper() in s:
        continue
    elif x in s1 and x in s:
        continue
    else:
        res = res + x

print(res)
