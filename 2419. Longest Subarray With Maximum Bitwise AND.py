class Solution:
    def longestSubarray(self, nums) -> int:
        max_num = max(nums)
        length = 0
        i = 0
        for num in nums:
            if num == max_num:
                i += 1
                continue
            if i>length:
                length = i
            i = 0
        if i>length:
            length = i
        return length
    
sol = Solution()
print(sol.longestSubarray([8, 8,2,8, 4,6, 8, 8, 8, 2, 8, 8])) # 1)
