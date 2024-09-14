for _ in range(int(input())):
    x1, x2, x3 = map(int, input().split())
    add = lambda x, y, z, a: (abs(x-a)+abs(y-a)+abs(z-a))
    maximum = max(x1, x2, x3)
    smallest = maximum
    for i in range(maximum, 0, -1):
        op = add(x1, x2, x3, i)
        if op < smallest:
            smallest = op
    print(smallest)