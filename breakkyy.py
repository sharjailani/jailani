string1,string2=input().split(' ')
c=0
for i in string1:
    if i in string2:
        print('yes')
        c+=1
        break
if c==0:print('no')
