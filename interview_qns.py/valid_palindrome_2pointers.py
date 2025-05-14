class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reversed = removed[::-1]
        if removed == reversed:
            return True
        else:
            return False