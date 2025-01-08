for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0
    for __ in range(n):
        x = len(input())
        m -= x
        if m >= 0:
            count += 1
        
    print(count)