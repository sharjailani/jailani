n=int(input())
a,b=input().split()
a,b=int(a),int(b)
a=a+1
if n in range(a,b):
  print('yes')
else:
  print('no')
