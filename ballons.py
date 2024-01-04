for i in range(int(input())):
    input()
    inp = input()
    l1 = []
    for i in inp:
        l1.append(i)
    set_ = set(l1)
    result = len(set_) + len(l1)   
    print(result)