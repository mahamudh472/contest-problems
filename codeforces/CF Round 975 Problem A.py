for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    even = []
    odd = []
    for i in range(n):
        if i%2==0:
            even.append(l[i])
        else:
            odd.append(l[i])
    result1 = max(even) + len(even) if even else 0
    result2 = max(odd) + len(odd) if odd else 0
    print(max(result1, result2))