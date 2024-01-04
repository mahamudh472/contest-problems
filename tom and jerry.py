for i in range(int(input())):
    n = input().split('0')
   
    tom = 0
    num = 0
    for i in n:
        num += 1
        if num%2 != 0:
            m = len(i)
            tom = tom + m
    print(tom)
