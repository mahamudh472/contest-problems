for _ in range(int(input())):
    n, k = map(int, input().split())
    l = [0 for i in range(n)]
    if k == 1:
        for i in range(1, n+1):
            l[i-1] = i
    elif k>1:
        start = 1
        for x in range(1, n//k+1):
            l[(x*k)-1] = start
            start += 1
        start -= 1
        for y in range(n):
            if l[y] == 0:
                l[y] = start +1
                start += 1
    s = ""
    for i in l:
        s += str(i)+" "
    print(s)