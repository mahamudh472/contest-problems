import sys
 
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
	n = int(input())
	a = [int(x) for x in input().split()]
 
	m = [0] * (n-1)
	for i in range(1, n):
		m[i-1] = max(a[i], a[i-1])
 
	M = min(m)
 
	print(M-1)