class Solution:
    def countPrefixSuffixPairs(self, words) -> int:
        count = 0
        for i in range(len(words)):
            for x in words[i+1:]:
                if x.startswith (words[i]) and x.endswith(words[i]):
                    count += 1
        return count