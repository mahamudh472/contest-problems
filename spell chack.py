for i in range(int(input())):
    inpu = int(input())
    
    inp = input()
    m_l = ["T", "i", "m", "u", "r"]
    l = []
    result = 0
    for i in inp:           #passed testcase
        l.append(i)
    try:
        for i in l:
            m_l.remove(i)
    except:
        result += 1
    if inpu != 5:
        print("No")
    elif result > 0:
        print("No")
    else:
        print("Yes")
    