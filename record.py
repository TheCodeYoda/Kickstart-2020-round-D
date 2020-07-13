t=int(input())

for _ in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	c=0
	l=[0]*n
	for i in range(n-1):
		if(a[i]>a[i+1]):
			c+=1
			l[i]=1
	l[n-1]=1
	mx=[a[0]]
	for i in range(1,n):
		if(a[i]>mx[-1]):
			mx.append(a[i])
		else:
			mx.append(mx[-1])
	l[0]+=1
	for i in range(1,n):
		if(a[i]>mx[i-1]):
			l[i]+=1
	#print(mx)
	print("Case #{}: {}".format(_+1,l.count(2)))