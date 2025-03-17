class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        for i in range(len(s)):
            freq = Counter()
            for j in range(i,len(s)):
                freq[s[j]] += 1
                max_freq = max(freq.values())
                min_freq = min(v for v in freq.values() if v > 0)
                total_beauty += max_freq - min_freq
        return total_beauty