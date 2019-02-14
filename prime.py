x = int(input())
for i in range(2, int(x/2)):
	if x % i  == 0:
		print("not")
		break
else:
	print("yes")
