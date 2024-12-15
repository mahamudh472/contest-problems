for i in range(int(input())):
    p = input()
    inp = list(map(int, input().split()))
    inp.sort()
    l = []
    count = 100000000000000000000000000000000000000000000000000000000000000
    for i in range(len(inp)-2):
        result = (inp[i+2]-inp[i+1]) + (inp[i+1]-inp[i])
        if result<count:
            count = result
            l1 = [inp[i+2],inp[i+1],inp[i]]
            l = l1
    main_result = (l[0]-l[1])+(l[1]-l[2])
    print(main_result)
