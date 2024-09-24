class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        s1 = set()
        s2 = set()
        for i in arr1:
            for x in range(len(str(i))):
                s1.add(str(i)[:x+1])
        for i in arr2:
            for x in range(len(str(i))):
                s2.add(str(i)[:x+1])
        common = max(s1.intersection(s2),key=len, default=0)
        if not common:
            return 0
        return len(common)
    
sol = Solution()
sol.longestCommonPrefix([13,27,45], [21,27,48])