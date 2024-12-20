from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    o = Counter(s)
    common = o.most_common()
    most = common[0][0]
    low = common[-1][0]
    print(s.replace(low, most, 1))