def longestCommonPrefix( strs) -> str:
    s = ""
    test = ""
    shortest = min(strs, key=len)
    i = 1
    cond = True
    if shortest == "" or len(strs)==1 or i>len(shortest):
        return shortest
    while cond:
        test = shortest[:i]
        for x in strs:
            if x.startswith(test):
                continue
            else:
                cond = False
                break
        i+=1
        if len(shortest)<i:
            return shortest
    return test[:-1]

print(longestCommonPrefix(["ab", 'a']))