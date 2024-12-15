class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        d = dict()
        result = []
        s1 = s1.split()
        s2 = s2.split()
        temp = set(s1+s2)
        for i in temp:
            d[i] = s1.count(i)+s2.count(i)
        for key, value in d.items():
            if value==1:
                result.append(key)
        return result
    
sol = Solution()
print(sol.uncommonFromSentences("apple apple", "banana"))