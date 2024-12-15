class Solution:
    def xorQueries(self, arr, queries):
        result = []
        prev = None
        final = []
        for item in arr:
            if prev:
                cur = prev^item
                result.append(cur)
                prev = cur
            else:
                result.append(item)
                prev = item
        for left, right in queries:
            if left==0:
                final.append(result[right])
            else:
                final.append(result[right]^result[left-1])
            return final
sol = Solution()
sol.xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]])