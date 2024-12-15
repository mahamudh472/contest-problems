n = int(input())
for i in range(n):
    string = ""
    string = string + (" # "* i) + (" @ " ) + " # "*(n-i-1) 
    print(string)