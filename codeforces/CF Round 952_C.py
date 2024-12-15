for _ in range(int(input())):
	n=int(input())
	array = list(map(int,input().split()))
	count=0
	total=0
	m=-1
	for i in range(n):
		total+=array[i]
		m=max(m,array[i])
		if total==(2*m):
			count+=1
	print(count)