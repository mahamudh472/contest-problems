for _ in range(int(input())):
    n , k = map(int, input().split())
    l = list(map(int, input().split()))
    sum = 0
    for i in range(k):
        sum += max(l[i::k])
    print(sum)