for i in range(int(input())):
    time = 0
    l = []
    a = input().split('%')
    num = int(a[0])


    for i in range (num,100):
        if i<60:
            time = time + 1
        elif i<80:
            time = time + 2
        else:
            time = time + 3
    print(time , "minutes")