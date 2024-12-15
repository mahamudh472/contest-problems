n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    inp = input().split()
    if len(inp) == 1:
        s.pop()
    else:
        command = inp[0]
        num = inp[1]
        num = int(num)

        if command == "remove":
            s.remove(num)
        if command == "discard":
            s.discard(num)
result = 0        
for i in s:
    result = result + i
    
print(result)