
num = int(input())
l = []
for i in range(num,0,-2):
    result = ("@" * (num-i+1)).center(num)
    l.append(result)

for i in range(3,num+1,2):
    result = ("@" * (num-i+1)).center(num)
    
string ="" 
for i in l:
    string = i + i
    print(string)
for i in reversed(l):
    if i == l[-1]:
        pass
    else:
        string = i + i
        print(string)