
n = input()
inp = input().split()
l = []
count = 0
for i in inp:
    i = int(i)
    l.append(i)
num = max(l)
for i in l:
    if i == num:
        count += 1
print(count)