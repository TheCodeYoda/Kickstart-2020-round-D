t=int(input())

for _ in range(t):
	n,q=map(int,input().split())
	d=list(map(int,input().split()))
	dp=[]
	for j in range(1,n+1):
		x=[j]
		l=j
		r=j
		for i in range(n-1):
			if(l==1):
				x.append(r+1)
				r+=1
			elif(r==n):
				x.append(l-1)
				l-=1
			else:
				if(d[l-1-1]<d[r-1]):
					x.append(l-1)
					l-=1
				else:
					x.append(r+1)
					r+=1
		dp.append(x)
	res=[]
	for i in range(q):
		s,k=map(int,input().split())
		res.append(dp[s-1][k-1])
	print("Case #{}:".format(_+1),end=" ")
	print(*res)