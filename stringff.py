num=list(input())
k1=[]
for x1 in num:
    if x1.isdigit():
        k1.append(x1)
print("".join(str(n) for n in k1))
