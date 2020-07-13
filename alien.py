t=int(input())

for _ in range(t):
	k=int(input())
	a=list(map(int,input().split()))
	c=1
	res=0
	for i in range(1,k):
		if(a[i-1]<a[i]):
			c+=1
		elif(a[i-1]>a[i]):
			c=1
		if(c>4):
			res+=1
			c=1
	c=1
	for i in range(1,k):
		if(a[i-1]>a[i]):
			c+=1
		elif(a[i-1]<a[i]):
			c=1
		if(c>4):
			res+=1
			c=1
	print("Case #{}: {}".format(_+1,res))