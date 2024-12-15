for i in range(int(input())):
    def key(num, l):
        l  = l
        x = l[num-1]
        if x == "0":
            return False
        else:
            return x
    a = int(input())
    n = input().split()
    door1 = key(a, n)
    if key(a, n) == False:
        print("No")
    else:
        door2 = key(int(door1), n)
        if door2 == False:
            print("No")
        else:
            print("Yes")