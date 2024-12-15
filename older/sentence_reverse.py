for i in range(int(input())):
    inp = input().split()
    result = ""
    for i in reversed(inp):
        result = result+i+" "

    print(result)