temp = [i**2 for i in range(1, 101, 2)]
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    happy = 0
    for x in l:
        count += x
        if count in temp:
            happy += 1

    print(happy)