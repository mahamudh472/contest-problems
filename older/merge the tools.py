def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        result = "".join(string[i:k+i])
        l = []
        for i in result:
            
            l.append(i)
        stri = ""
        for i in l:
            if i not in stri:
                stri = stri + "".join(i)
        print(stri)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)