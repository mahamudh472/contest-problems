from itertools import combinations_with_replacement as cwr
class Solution:
    def maximumStrongPairXor(self, nums) -> int:
        return max([ i^j for i,j in (cwr(nums, 2)) if abs(i-j)<= min(i, j)])
        


sol = Solution()
sol.maximumStrongPairXor([1,2,3,4,5])