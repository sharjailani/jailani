x,y=input().split()
x,y=int(x),int(y)
ist=[int(z)for z in input().split()]
sum=0
for i in range(y): 
  sum=sum+ist[i]
print(sum) 
