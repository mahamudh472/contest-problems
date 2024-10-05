from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1>s2:
            return False
        sorted_s1 = sorted(s1)
        left, right = 0, len(s1)  
        while right <= len(s2):
            if sorted(s2[left:right])==sorted_s1:
                return True
            left += 1
            right += 1
        return False

sol = Solution()
sol.checkInclusion("abcdxabcde", "abcdeabcdx")