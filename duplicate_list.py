a=[1,2,3,2,3,5,4,6,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

