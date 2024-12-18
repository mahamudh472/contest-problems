for _ in range(int(input())):
    new_s = ""
    s = input()
    for i in s:
        if i == "p":
            new_s += "q"
        elif i == "q":
            new_s += "p"
        else:
            new_s += i
    print(new_s[::-1])