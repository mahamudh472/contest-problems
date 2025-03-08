n = int(input())
a = list(map(int, input().split()))

status = False
for i in range(len(a)-2):
    if a[i] == a[i+1] == a[i+2]:
        status = True
        break
if status:
    print('Yes')
else:
    print('No')

