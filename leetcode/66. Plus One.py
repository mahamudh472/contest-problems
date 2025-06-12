class Solution:
    def plusOne(self, digits):
        n = int("".join(digits)) + 1
        result = [int(i) for i in str(n)]
        return result

# Example usage:
sol = Solution()
print(sol.plusOne(["1", "2", "3"]))  # Output: [1, 2, 4]