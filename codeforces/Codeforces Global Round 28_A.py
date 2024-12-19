
for _ in  range(int(input())):
    num = int(input())
    while num>=33:
        num_str = str(num)
        if '33' in  num_str:
            num_str = num_str.replace('33', '', 1)
            num = int(num_str) if num_str else 0
        elif num>=33:
            num -= 33
    if num == 0:
        print('Yes')
    else:
        print('No')