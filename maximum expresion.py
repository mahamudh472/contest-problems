for i in range(int(input())):
    m = int(input())
    inp = input()
    numbers = []
    plus = 0
    minus = 0
    for i in inp:
        if i == "+":
            plus += 1
        elif i == "-":
            minus += 1
        else:
            numbers.append(int(i))
    n = 1

    result = (sorted(numbers))[::-1]
    for i in range(minus):
        result.insert(-n, "-")
        n += 2
    for i in range(plus):
        result.insert(-n, "+")
        n += 1
    string = ""
    for i in result:
        string = string + "".join(str(i))
    print(string)
