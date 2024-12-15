class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_string = ""
        l = []
        for i in s:
            l.append(ord(i)-ord("a")+1)
        while k!=0:
            new_sum = sum(l)
            l = [int(i) for i in str(new_sum)]
            k-=1
        for x in l:
            num_string += str(x)
        return int(num_string)

sol = Solution()
print(sol.getLucky("iiii", 1))