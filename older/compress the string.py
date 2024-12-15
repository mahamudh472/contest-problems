def convert(inp, main_list):
    string = [i for i in inp]
    if "M" not in string:
        string.append("M")
    main_list = main_list + []
    l = []
    i = 1
    l.append(string[0])
    while string[i] == string[i-1]:
        l.append(string[i])
        i+=1
    main_list.append(l)
    n = len(l)
    for i in range(len(l)):
        string.remove(string[0])

    if len(string) != 1:
        string = "".join(i for i in string)
        if len(string) != 1:
            convert(string, main_list)
    else:
        c = []
        m = []
        for i in main_list:
            num = i[0]
            m.append(int(num))
            count = len(i)
            c.append(count)
        result = (list(zip(c,m)))
        for i in result:
            print(i, end=" ")


inp = input()
mai = []
convert(inp,mai)


