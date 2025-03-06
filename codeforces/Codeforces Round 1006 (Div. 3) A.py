for _ in range(int(input())):
    n, k, p = map(int, input().split())
    k = abs(k)
    if k == 0:
        print(0)
    else:
        res = k//p + (1 if k%p>0 else 0)
        if res<=n:
            print(res)
        else:
            print(-1)
        