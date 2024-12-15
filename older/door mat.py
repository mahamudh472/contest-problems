n, m = map(int, input().split())
inp = ".|."
md = inp.center(21, "-")
for i in range(1, int(n/2)+1):
    p = i*2-1
    inp = (".|."*p).center(m, "-")
    print(inp)
print("welcome".center(m,'-'))
for i in reversed(range(1, int(n/2)+1)):
    p = i*2-1
    inp = (".|."*p).center(m, "-")
    print(inp)