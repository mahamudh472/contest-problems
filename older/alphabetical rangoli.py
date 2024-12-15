n = int(input())
l = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
m = 1
j = (n*2-1) + (n*2-2)
k = 1
lis = []
for i in range(n):
    string = ""
    for i in reversed(range(m, n+1)):
        string = string + l[i] + "-"
    for i in range(m+1, n+1):
        string = string + l[i] + "-"
    m += 1
    result = (string[:-1].center(j, "-"))
    lis.append(result)
for i in reversed(lis):
    print(i)

for i in lis:
    if i == lis[0]:
        pass
    else:
        print(i)