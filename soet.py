n=input()
lst=[int(n) for n in input().split()]
if(lst==sorted(lst)):
  print('yes')
else:
    print('no')
