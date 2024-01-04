num = int(input())

for i in range(0,num,2):
    result = ("@" * (num-i)).center(num)
    print(result)
for i in range(num-1,0,-2):
    result = ("@" * (num-i+2)).center(num)
    print(result)