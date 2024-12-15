class Solution:
    def kthDistinct(self, arr: str, k: int) -> str:
        result = []
        for i in arr:
            if arr.count(i)==1:
                result.append(i)
        try:
            return result[k-1]
        except:
            return ""