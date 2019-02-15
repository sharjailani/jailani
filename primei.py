lower,upper=input().split()
lower,upper=int(lower),int(upper)
for n in range(lower+1,upper+1):
   if n > 1:
       for i in range(2,int(n)):
           if (n % i) == 0:
               break
       else:
           print(n,end=" ")
