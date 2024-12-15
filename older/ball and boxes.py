for i in range(int(input())):
    n, k = map(int, input().split())
    res = (k*(k+1)/2)
    if res <= n:
        print("Yes")
    else:
        print("No")