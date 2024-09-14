class Solution:
    def similarPairs(self, words) -> int:
        d = dict()
        count = 0
        for word in words:
            unique = set([i for i in word])
            unique_string = "".join(sorted(unique))
            if unique_string in list(d.keys()):
                d[unique_string] = d[unique_string] + 1
            else:
                d[unique_string] = 1
        for key, value in d.items():
            if value>1:
                count += value
        return count
    
sol = Solution()
sol.similarPairs(["aba","aabb","abcd","bac","aabc"])