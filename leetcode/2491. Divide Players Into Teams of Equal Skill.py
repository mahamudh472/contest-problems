class Solution:
    def dividePlayers(self, skill) -> int:
        s = sorted(skill)
        temp = None
        left = 0
        right = -1
        result = 0
        while left<len(skill)/2:
            if not temp:
                temp = s[left] + s[right]
            if temp == s[left] + s[right]:
                result += s[left] * s[right]
            else: return -1
            left += 1
            right -= 1
        return result
    
sol = Solution()
sol.dividePlayers([3,2,5,1,3,4])