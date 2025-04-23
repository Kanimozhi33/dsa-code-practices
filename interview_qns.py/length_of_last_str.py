class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.split()
        last = t[-1]
        return len(last)
