l = [0 for i in range(100)]
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a[0] == 1:
        l.append(a[1])
    else:
        print(l[-1])
        l.pop()

