
a = [i for i in input()]
b = [i for i in input()]
i = 0
while i<len(b):
    if b[i] in a:
        a.remove(b[i])
        del b[i]
        i-=1
    i+=1
if len(b)==0:
    print("%s %d"%("Yes",len(a)),end = "")
else:
    print("%s %d"%("No",len(b)),end = "")





