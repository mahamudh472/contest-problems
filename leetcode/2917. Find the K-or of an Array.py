class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new = ""
        result = ""
        for i in s:
            if i not in new:
                new+=i
                continue
            if len(new)>len(result):
                result = new
            new = i + new.split(i)[1]
        return len(result)

sol = Solution()
print(sol.lengthOfLongestSubstring("aabaab!bb")) #3