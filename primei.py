lower,upper=input().split()
lower,upper=int(lower),int(upper)
for n in range(lower,upper):
   if n > 1:
       for i in range(2,n+1):
           if (n % i) == 0:
               break
       else:
           print(n,end=" ")
